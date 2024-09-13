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
import pymongo
import csv
import os


class DatabaseSource():

    # Method to get data from local SQLite3 database
    def GetDataFromSQL(this,dbpath):
        conn = sqlite3.connect(dbpath)
        cur = conn.cursor()
        tableList = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        for ind, name in enumerate(tableList):
            print(ind , ":", name[0])
        targetTable = int(input("Enter Number Corresponding to Table Name To Get Data From : "))
        colNames = cur.execute(f"PRAGMA table_info({tableList[targetTable][0]})").fetchall()
        colNames = ",".join([i[1] for i in colNames])
        print("All Fields : \n" + colNames)
        targetCols = input("Enter Field Names, Comma Seprated, To Generate Data : ")
        try:
            targetData = cur.execute(f"SELECT {targetCols} from {tableList[targetTable][0]}").fetchall()
            with open("output.csv", "w", newline="") as f:
                csv.writer(f).writerow(targetCols.split(','))
                csv.writer(f).writerows(targetData)
            print("File Saved as : " + os.path.join(os.path.curdir, "output.csv"))
            return os.path.join(os.path.curdir, "output.csv")
        except sqlite3.OperationalError:
            print("Check Target Fields Again")
            return None

    # Method to get data from Mongo database
    def GetDataFromMongo(this, mongoURL):
        client = pymongo.MongoClient(mongoURL)
        allDB = client.list_databases()
        
        


source = DatabaseSource()

source.GetDataFromMongo("mongodb+srv://aryanshdev:qwertyasdf123+-@notecraft.co24v.mongodb.net/?retryWrites=true&w=majority&appName=NoteCraft")