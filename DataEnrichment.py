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
import csv
import sklearn.linear_model

# class containing various Data Enriching functionalities
class EnrichData():
    # Function to Add IP data
    def AddIPData(this, ip):
        url = f'https://ipwhois.app/json/{ip}'
        try:
            res = req.get(url)
            data = res.json()
            return {
                'city': data.get('city', ''),
                'region': data.get('region', ''),
                'country': data.get('country', ''),
                'org': data.get('org', ''),
            }
        except req.RequestException:
            return None

    def EnrichFromSQLDatabase(inputfile, dbpath):
        with open(inputfile, "r") as f:
            headers = csv.reader(f)


