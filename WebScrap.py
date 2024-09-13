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
            requests
            BeautifulSoup
            csv
            os

        Module Installation : pip install -r requirements.txt
"""


# Module Imports
import requests as req
from bs4 import BeautifulSoup
import csv
import os


# Function Defination
def Web_Table_To_CSV(url):
    """
    Input : URL Of Webpage containing table
    Output : Path to Generated CSV
    """
    # Create Normal HTTPS-GET Request
    content = req.get(url)
    # .text returns the entire HTML document as string
    data = BeautifulSoup(content.text, 'html5lib')
    # Use CSS Selectors to get elements
    allTables = data.find_all("table")
    print("ENTER TABLE NUMBER TO EXTRACT DTA FROM")
    for i in range(len(allTables)):     # Loop All Tables
        tab = allTables[i]
        # Get First Row of table containing headers
        firstRow = tab.find("tr")
        # Checks wheater table uses th tags or td tags for headers and then saves them to a var
        firstEntry = firstRow.find_all("th") if type(
            firstRow.find("th")) != None else firstRow.find_all("td")
        # Temp variable to diplay headers of each table to allow user to choose target table
        rowDisp = ""
        for d in firstEntry:
            rowDisp += d.text + " | "
        print(f"Table Number : {i} \n Fields: {rowDisp}")
    try:
        targetTab = allTables[int(input("Enter Target Table Number : "))]
    except IndexError:
        # Return none and exit if user enters wrong index for tables
        print("Invalid Number")
        return None
    # Not extract data from target table
    # First get all rows in target table
    allTargetRows = targetTab.find_all("tr")
    # Now get it's headers; similar to previous checking
    firstEntry = allTargetRows[0].find_all("th") if type(
        allTargetRows[0].find("th")) != None else allTargetRows[0].find_all("td")
    # Array to store all data row-wise
    outputArr = []
    # Loop below will store all heraders from table
    outputArr.append([])
    for i in firstEntry:
        outputArr[0].append(i.text)
    # Now add all data from table to output array row-wise
    for i in allTargetRows[1:]:
        outputArr.append([])
        for j in i:
            if j.text.strip() != "":
                outputArr[-1].append(j.text)

    # Saving Data to CSV
    path = os.path.join(os.path.curdir, "output.csv")   # Path for file in CWD
    csvFile = open(path, "w", newline="")               # Create New CSV File
    csvHandler = csv.writer(csvFile)                    # CSV Handler For File
    csvHandler.writerows(outputArr)                     # Write All Data
    csvFile.close()                                     # Close And Save File
    print("Dataset CSV Saved At : "+path)               # Output Echo to user
    return path


# Example Usage
# Web_Table_To_CSV(
#     "https://anakin.ai/blog/groq-llama-3-1-api-pricing/#comparing-llama-31-models-on-groq")
