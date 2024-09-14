"""
    Created by Aryansh (aryanshdev) 

    This file contains a function that takes a url as parametric input and then scrapes that page
    to find all tables in it. It then diplays headers of all tables on the page and allows user to choose 
    any one table to get data from.

    Extracted data is stored as a CSV file. The function returns the path of generated CSV file
    ________________________________________________________________________
    
    Dependecies:

        Enviroment : 
            Python 3.11.4 [MSC v.1934 64 bit (AMD64)] on win32
            Windows 11

            Tested On :
            Kali Linux 2022 (Custom Image) - Debian Based Linux

        Modules :
            sqlite3
            pymongo
            csv
            os

        Module Installation : pip install -r requirements.txt
"""

# Import
import sqlite3
import urllib.parse
import pymongo
import csv
import os
import urllib


class DatabaseSource():
    # Method to get data from local SQLite3 database
    def GetDataFromSQL(this, dbpath):
        conn = sqlite3.connect(dbpath)      # Connect DB
        cur = conn.cursor()                 # Create Cursor
        # Fetch ALl Tables
        tableList = cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        # Print all tables
        for ind, name in enumerate(tableList):
            print(ind, ":", name[0])
        # Take desired table as inp from user
        targetTable = int(
            input("Enter Number Corresponding to Table Name To Get Data From : "))
        # display all attributes to user
        colNames = cur.execute(
            f"PRAGMA table_info({tableList[targetTable][0]})").fetchall()
        colNames = ",".join([i[1] for i in colNames])
        print("All Fields : \n" + colNames)
        targetCols = input(
            "Enter Field Names, Comma Seprated, To Generate Data : ")
        try:
            # try getting all column data from table
            targetData = cur.execute(
                f"SELECT {targetCols} from {tableList[targetTable][0]}").fetchall()
            with open("output.csv", "w", newline="") as f:
                csv.writer(f).writerow(targetCols.split(','))
                csv.writer(f).writerows(targetData)
            print("File Saved as : " + os.path.join(os.path.curdir, "output.csv"))
            return os.path.join(os.path.curdir, "output.csv")
        except sqlite3.OperationalError:
            print("Check Target Fields Again")
            return None

    # Method to get data from Mongo database
    def GetDataFromMongoAtlas(this, username, password, host):
        # make username password url firendly -> Mongo Docs Mentioned to do so
        # else connection issues
        username = urllib.parse.quote_plus(username)
        password = urllib.parse.quote_plus(password)
        # prep url for connection
        urlTransformed = f"mongodb+srv://{username}:{password}@{host}/?retryWrites=true&w=majority&appName=NoteCraft"
        client = pymongo.MongoClient(urlTransformed)        # connect to Mongo
        allDB = client.list_database_names()                # Get All DBs
        print("Cluster Contains Following Databases : \n"+"\t".join(allDB))
        targetDB = client.get_database(
            input("Enter Database Name To Get Data From : "))   # Ask user for db to get data from
        # Get all collections in that db
        allCollections = (targetDB.list_collection_names())
        print("Database Contains Following Collections : \n" +
              "\t".join(allCollections))
        targetColl = targetDB.get_collection(
            input("Enter Database Name To Get Data From : "))     # Ask user for target collection
        # Fetch All Data From Collection
        data = list(targetColl.find({}))
        client.close()  # Close Mongo Connection
        # Save to local CSV
        with open("output.csv", "w", newline="") as f:
            csv.writer(f).writerow(dict(data[0]).keys())
            data = [dict(i).values() for i in data]
            csv.writer(f).writerows(data)
        print("File Saved as : " + os.path.join(os.path.curdir, "output.csv"))
        return os.path.join(os.path.curdir, "output.csv")


# Example usage
# source = DatabaseSource()
# source.GetDataFromSQL("./test.db")
