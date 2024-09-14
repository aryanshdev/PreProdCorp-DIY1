"""
    Created by Aryansh (aryanshdev)

    This file contains a class having various methods to enrich data directly from CSV files stored in directories,
    ________________________________________________________________________

    Dependecies:
        Enviroment :
            Python 3.11.4 [MSC v.1934 64 bit (AMD64)] on win32
            Windows 11

            Tested On :
            Kali Linux 2022 (Custom Image) - Debian Based Linux

        Modules :
            pandas
            requests
            csv
            scikit-learn

        Module Installation : No Specific, Built-In Library Modules Used
"""


import pandas as pd
import requests as req
import sqlite3
import sklearn.linear_model


# class containing various Data Enriching functionalities
class EnrichData():

    # Function to Get IP data
    def GetIPData(this, ip):
        url = f'https://ipwhois.app/json/{ip}'      # Free IP Lookup
        try:
            res = req.get(url)                      # Request IP Lookup
            data = res.json()
            # Return Data as Dictonary
            return {
                'city': data.get('city', ''),
                'region': data.get('region', ''),
                'country': data.get('country', ''),
            }
        except req.RequestException:
            return None

    # Funtion to Enrich Data with IP Info
    def EnrichIP(this, inputfile):
        # Create Pandas Dataframe From File Data
        data = pd.DataFrame(pd.read_csv(inputfile))
        attributes = data.head()                        # Get Attributes
        print("All Fields :\n" + ", ".join(attributes))
        # Input IP Containing Attribute From User
        ipAddCol = input("Enter Column Name Containing IP Address : ")
        ipInfo = []
        # Find IP Info For All IP Addresses
        for i in data[ipAddCol].tolist():
            ipInfo.append(this.GetIPData(i))

        # New Dataframe containing IP Info for each IP
        infoDF = pd.concat([data, pd.DataFrame(ipInfo)], axis=1)
        # Save The Eriched Data Back To File
        infoDF.to_csv(inputfile, index=False)
        print("CSV File Updated")

    # Function to enrich data from SQL Databse
    def EnrichFromSQLDatabase(this, inputfile, dbpath, manualselect=False):
        data = pd.DataFrame(pd.read_csv(inputfile))
        datafields = data.head()
        dbcon = sqlite3.connect(dbpath)
        dbcur = dbcon.cursor()
        # Fetch ALl Tables
        tableList = [i[0] for i in dbcur.execute(
            "SELECT name FROM sqlite_master WHERE type='table';").fetchall()]
        if (not manualselect):
            targetTables = []
            # Find table with similar data fields
            for i in tableList:

                fields = [i[1] for i in dbcur.execute(
                    f"PRAGMA table_info({i})").fetchall()]
                if set(datafields).issubset(set(fields)):
                    targetTables.append(i)
            if (len(targetTables) == 0):
                print(
                    "No Suitable Table Found In Database. Run This Method with manualselect=True to Manually select table")
                return
            print("Tables Suitable For Data Collection : \n" +
                  ", ".join(targetTables))
        else:
            print("All Tables :\n"+", ".join(tableList))
        target = input("Enter Table Name To Collect Data From : ")
        if (not manualselect):
            colString = (", ").join(datafields)
        else:
            colString = input(
                "Enter Columns Names, Comma Seprated, To Collect Data From : ")
        tempDFFromDB = pd.read_sql_query(
            f"SELECT {colString} FROM {target} ;", dbcon)
        enrichedData = pd.concat([data, tempDFFromDB], ignore_index=True)
        # Save The Eriched Data Back To File
        enrichedData.to_csv(inputfile, index=False)
        print("CSV File Updated")

    # Function to enrich data from SQL Databse
    def EnrichFromCSV(this, inputfile, datafile):
        data = pd.read_csv(inputfile)
        collected = pd.read_csv(datafile)
        if (data.head() == collected.head()):
            final = pd.concat([data, collected], ignore_index=True)
            final.to_csv(inputfile)
            print("Saved Data To File")
        else:
            askUser = input("Headers Mismatch, Force Continue Merge ? (y/n)")
            if (askUser != "n"):
                final = pd.concat([data, collected], ignore_index=True)
                final.to_csv(inputfile)
                print("Saved Data To File")


# Example Usage
# enricher = EnrichData()
# enricher.EnrichFromSQLDatabase("./test.csv", "./test.db", manualselect=True)
