"""
    Created by Aryansh (aryanshdev) 

    This file contains a function that connects to remote/local FTP server and searches for csv file in all directories,
    and lists them to user. User then can choose which file to download.
    ________________________________________________________________________
    
    Dependecies:

        Enviroment : 
            Python 3.11.4 [MSC v.1934 64 bit (AMD64)] on win32
            Windows 11

            Tested On :
            Kali Linux 2022 (Custom Image) - Debian Based Linux

        Modules :
            ftplib
            os

        Module Installation : No Specific, Built-In Library Modules Used
"""

# Import required Modules
import ftplib
import os

# Create FTP Data Source Class
class FTPDataSource():
    def __init__(this , url, username, password):
        # Create a Connection Object
        this.connOBJ = ftplib.FTP(url, username, password)
        this.homeDir = this.connOBJ.pwd()

    # Method to get file from specific Directory
    def FetchFileFromPath(this, filePath):
        # Check if complete path to file
        if filePath.endswith(".csv") or filePath.endswith(".csv\\"):
            # Saving FTP Data to CSV
            # Path for file in local CWD
            path = os.path.join(os.path.curdir, "output.csv")
            with open(path, 'wb') as f:
                # Download the file from the FTP server
                this.connOBJ.retrbinary(f"RETR {filePath}", f.write)
            this.connOBJ.close()
            print("File Saved as : " + path)
            return path
        else:
            # this executes when path is given but exact file not given
            # it will iterate through all files to find possible data files (CSV)

            # go to mentioned path to find all possible data files
            this.connOBJ.cwd(filePath)
            print("Choose Which CSV File To Download")
            # print all csv files in directory
            try:
                for file in this.connOBJ.nlst():
                    # Check if file is CSV File, if yes then print it's name
                    if (file.endswith(".csv")):
                        print(file)
            except ftplib.error_perm:
                # Empty Dir
                print("No File In This Dir, Returning")
                return None
            # Ask user to choose desired file
            name = input("Enter Name Of CSV File : ")
            # Saving FTP Data File to local CSV
            # Path for file in local CWD
            path = os.path.join(os.path.curdir, "output.csv")
            with open(path, 'wb') as f:
                # Download the file from the FTP server
                this.connOBJ.retrbinary(f"RETR {name}", f.write)
            this.connOBJ.close()
            print("File Saved as : " + path)
            return path

    def FindAllSubDirs(this, currentLoc):
        try:
            this.connOBJ.cwd(currentLoc)
        except:
            temp = "/".join(this.connOBJ.pwd().split('/')[:-1])
            this.connOBJ.cwd(this.homeDir)
            this.connOBJ.cwd(temp)
            allPossible = this.connOBJ.nlst()
            allPossible = [i for i in allPossible if i.count(".") == 0]
            return allPossible
        
        allPossible = this.connOBJ.nlst()
        allPossible = [i for i in allPossible if i.count(".") == 0]
        return allPossible

    def FindFileInSubDir(this, subdirArr, fileName):
        # print all csv files in directory
        try:
            outArr = []
            for file in this.connOBJ.nlst():
                # Check if file is named same as required file, if yes then print it's complete location
                if file == fileName:
                    print(this.connOBJ.pwd()+"\\" + file)
                    outArr.append(this.connOBJ.pwd()+"\\" + file)
            return outArr
        except ftplib.error_perm:
            # Empty Dir
            print("No File In This Dir, Returning")
            return None
        finally:
           for i in subdirArr:
               print(subdirArr)
               this.FindFileInSubDir(this.FindAllSubDirs(i), fileName)
  
    def list_all_subdirs(this, current_dir):
        """
        Recursively list all subdirectories in the given directory on the this.connOBJ server.
        
        :param this.connOBJ: An instance of this.connOBJlib.this.connOBJ connected to the server.
        :param current_dir: The directory to start listing from.
        """
        # Change to the current directory
        this.connOBJ.cwd(current_dir)
        # Get the list of files and directories in the current directory
        items = this.connOBJ.nlst()
        
        # Iterate over each item in the current directory
        for item in items:
            try:
                # Try to change to the directory (if successful, it's a folder)
                this.connOBJ.cwd(item)
                print(f"Directory: {item}")
                # Recurse into the subdirectory
                this.list_all_subdirs(this.connOBJ, item)
                # Go back to the parent directory after finishing
                this.connOBJ.cwd('..')
            except Exception as e:
                # If it fails, it's a file (or permission error), skip it or just print it
                print(f"File: {item}")

# Example Usage
source = FTPDataSource("ftp.dlptest.com", "dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu")
with open("./output.csv", 'rb') as file:
    source.connOBJ.storbinary(f'STOR output.csv', file)

source.FindFileInSubDir(source.homeDir, "output.csv")