import ftplib

def FetchDataFromServer(url,username,password,filename):
    conn = ftplib.FTP(url,username,password)
    
