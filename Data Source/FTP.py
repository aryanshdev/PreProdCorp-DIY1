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
    def __init__(this, url, username, password):
        # Create a Connection Object
        this.connOBJ = ftplib.FTP(url, username, password)
        this.homeDir = this.connOBJ.pwd()
        this.dirStack = []
        this.visited = []

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

    def FindAllSubDirs(this, filename, ignoreHomeLoop=False):
        if (this.connOBJ.pwd() == '/' and len(this.visited) != 0 and not ignoreHomeLoop):
            allPossible = this.connOBJ.nlst()
            allPossible = [i for i in allPossible if i.count(".") == 0]
            allPossible = [
                i for i in allPossible if ("/"+i) not in this.visited]
            print(allPossible)
            if allPossible == []:
                print("Entire Server Scanned")
                return
            this.dirStack.pop()
            this.dirStack.append(allPossible[0])
            this.FindAllSubDirs(filename, ignoreHomeLoop=True)

        this.connOBJ.cwd(this.homeDir)
        if ("/".join(this.dirStack) in this.visited):
            this.dirStack.pop()
            this.visited.append(this.connOBJ.pwd())
        print(this.dirStack)
        this.connOBJ.cwd("/".join(this.dirStack))

        allPossible = this.connOBJ.nlst()
        allPossible = [i for i in allPossible if i.count(".") == 0]
        allPossible = [
            i for i in allPossible if this.connOBJ.pwd()+"/"+i not in this.visited]
        if allPossible == []:
            this.FindFileInDir(filename)
            this.dirStack.pop()
            this.visited.append(this.connOBJ.pwd())
        else:
            this.dirStack.append(allPossible[0])
        this.FindAllSubDirs(filename)

    def FindFileInDir(this, fileName):
        # print all csv files in directory
        try:
            for file in this.connOBJ.nlst():
                # Check if file is named same as required file, if yes then print it's complete location
                if file == fileName:
                    print("Found File With Same Name In : \n" +
                          this.connOBJ.pwd()+"\\" + file)
                    return this.connOBJ.pwd()+"\\" + file

        except ftplib.error_perm:
            # Empty Dir
            print("No File In This Dir, Returning")
            return None

    def list_all_subdirs(this, current_dir):
        """
        Recursively list all subdirectories in the given directory on the this.connOBJ server.

        :param this.connOBJ: An instance of this.connOBJlib.this.connOBJ connected to the server.
        :param current_dir: The directory to start listing from.
        """
        # Change to the current directory
    def FetchFileWithName(this, filename):
        this.FindAllSubDirs(filename)


# Example Usage
# source = FTPDataSource("ftp.dlptest.com", "dlpuser",
#                        "rNrKYTX9g7z3RgJRmxWuGHbeu")
# source.FetchFileWithName("readme.txt")
