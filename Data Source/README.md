# Data Sources


## What is a Data Source?

Data Source is any location, file, system, database etc that can provide data for a specific requirement. They enable the collection, storage, and access of information for analysis or operational usage. Data sources can be diverse and vary in structure, complexity, form and type. They serve as the origin of data used in processes like Data Enrichment, Machine Learning, or Forecasting.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfXZLIftwuh5nYnchpf8Wayeyc_UsoSYGD-ysC2MWEwLPXKc_xbuIW3Or4YM7FW3Aek_D7FFz-Vb-ggODAsbrKTT2pJEzyPlkMKvKsnSdYUSyFE_ggtVEBWYpfEpsW_n_YnywOfVFKDlkil2T76jVImT4DQ?key=BVxHPz3ZOVW22nPAYBM1eQ)

Img src: [https://www.joinblogarama.com/](https://www.joinblogarama.com/)

  
## Why Is a Data Source Important?

Data sources are essential because they provide the raw material needed to generate insights, make decisions, and run various operations. Here are some key reasons why data sources are important:

1.  Basis Of Analysis: Data sources provide the necessary data and information for conducting analysis, ensuring decisions are backed by factual data.
    
2.  Reliability: Verified data sources helps maintain the accuracy and reliability of the data used in various processes.
    
3.  Comprehensive View: Multiple data sources allow for a broader and more complete understanding of the situation, leading to better outcomes.
    
4.  Consistency: Reliable data sources ensure consistency across different reports and analyses, avoiding discrepancies in information.
    
5.  Operational Efficiency: Good data sources streamline processes by automating data collection, saving time, and reducing errors.
    

  

## Data Source Types

There are many distinct types of data sources, and each one has a unique role to play in the gathering of data. Here are a few typical categories of data sources:

  

### Based On Location:

1.  Internal Data Sources: Information gathered from within the organization, including customer, sales data and staff details etc. Internal data sources are more easily accessible and usually more organized.
    
2.  External Data Sources: Information gathered from sources outside the company, including competition and market analyses, market reports, and publicly accessible information like economic and meteorological statistics. A wider view is offered by external sources, which supplement internal data.
    

  

### Based On Structure:

1.  Structured Data Sources: Information that is organized and easily searchable in databases. Example Relational databases like SQL, Spreadsheets, and Data Warehouses. Structured data is typically stored in rows and columns, making it straightforward to analyze and query.
    
2.  Unstructured Data Sources: Information that lacks a predefined format or structure. Examples include text documents, emails, social media posts, videos, and images. Unstructured data is more challenging to process and analyze due to its varied formats and lack of organization.
    
3.  Semi-Structured Data Sources: Information that does not conform to a rigid structure but contains tags or markers to separate data elements. Examples include XML files, JSON files, and NoSQL databases. Semi-structured data strikes a balance between structured and unstructured data, offering some level of organization while maintaining flexibility.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXflUekfznZHOzPekTJSFWZgs_LgQw0D43DyjsKvKCFwajB9wFpP9WbMUmxI-bTdfhpMsWhpT6fJoeMJWzteleCy5rLxLrqRZysYbKZel20RNepNk-OEeg50NDn94kTgfeoRtsQUNLJ2mJzFUbnCUBeyAaLZ?key=BVxHPz3ZOVW22nPAYBM1eQ)

Img src: [https://opensourceforu.com/2018/01/can-big-data/](https://opensourceforu.com/2018/01/can-big-data/)

# Code

The program developed during this DIY Sprint provides Three classes for Data Gathering that further contains several methods to perform data gathering and generation. More details are described below.
  

## Class and Its Methods

### WebScrapper
The WebScrapper class is the used for gathering data from Internet using WebScrapping technique.

    scapper = WebScraper()
  

#### Methods :
 `Web_Table_To_CSV`: This method scraps webpage to find all tables in it, then asks user to selet a table to get data from, based on user selection, data is gathered and stored as a CSV file.
It takes a URL for target webpage as input and returns the path of generated CSV.

Usage Example:

    scrapper.Web_Table_To_CSV('www.example.com')
<br/>

> ⚠️ENSURE TO FIRST OPEN THE DIRECTORY CONTAINING ALL FILES AND THEN RUN webscrap.py AS THE PATH FOR DRIVER IS RELATIVE AND IF YOU NOT OPEN THE CORRECT DIRECTORY BEFORE RUNNING,GetECommData WILL CRASH <br/> Like : if all files are in extracted/Data Source, first use `cd './extracted/Data Source'` then use ```python webscrap.py```

 `GetECommData`: This method allows us to collect data about a category of products from 2 Popular E-Commerce website- Amazon and Flipkart.
It takes a product category as input and has 2 optionals, Amazon and Flipkart, which take True/False as input values and are used to select the eccom website to gather data from, by default Amazon is True and Flipkart is False.
It returns path of saved CSV files

Usage Example:

    scrapper.GetECommData('laptop',Amazon=True,Flipkart=True)

  
  ---

### FTPDataSource
The FTPDataSource class is the used for gathering data from FTP servers. It takes FTP server hostname, FTP username and Password to instantiate

    source = FTPDataSource("ftp.dlptest.com", "exampleuser",  "examplepassword")

  

Methods :

 `FetchFileWithName`: This method Searches the entire FTP server to find the file with specified name and then asks user which file to get from server.
    It takes a file name as input and returns the path of generated CSV.
    
Usage Example:
 

       source.FetchFileWithName(‘test.csv')
  <br/>
  
`FetchFileFromPath`: This method saves the specified file from provided location to local system.
It returns path of saved CSV files

Usage Example:

    source.FetchFileFromPath("data.csv")

  

### DatabaseSource
The DatabaseSource class is the used for gathering data from various types of databases

  

    source = DatabaseSource()

  

#### Methods :

 `GetDataFromSQL`: This method is used to get data from SQL table and save it into a local csv file
 It takes database path as input and returns the path of generated CSV.

Usage Example:

    source.GetDataFromSQL("./test.db")

  
  

 `GetDataFromMongoAtlas`: This method is used to get data from MongoDB Cluster and save it into a local csv file
It takes database username, password and host as input and returns the path of generated CSV.

Usage Example:

    source.GetDataFromMongoAtlas("username","password","host")
