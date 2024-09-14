
# Data Enrichment
 

## What is Data Enrichment?

Data enrichment is a practice that improves the quality of already available data to make it more comprehensive, meaningful and useful. It enhances or improves raw data by adding relevant information or attributes from external or known sources. It enhances data’s utility, accuracy, and richness, making it more reliable.

  
## Why Is Data Enrichment Required?

Data enrichment is required for numerous reasons, especially when raw data is inadequate or lacks the critical features to provide useful insights or drive decision-making. There are several reasons to perform Data Enrichment.

1.  Improving Quality Of Data: It helps in filling up missing data, correcting inaccuracies, and making data consistent.
    
2.  Improves Decision-making: It increases the accuracy and consistency of data allowing better, more informed decisions. This enriched data can also be used for analysis and forecasting.
    
3.  Performance: By providing more accurate and reliable data, data enrichment could improve the quality and efficiency of processes and operations. Eg. Data enrichment can be used to remove errors and inconsistencies from data to improve data analysis and reporting.
    
4.  Enhanced Reporting and Forecasting: Leveraging multiple data sources can lead to better reporting and forecasting by providing a more comprehensive view of the business landscape.
    

  

## Types of Data Enrichment

1.  Demographic Enrichment: Adding information such as age, gender, income level, education, etc., to customer data.
    
2.  Geographic Enrichment: Adding location-related information like latitude, longitude, or even more detailed geographic segmentation.
    
3.  Behavioural Enrichment: Enhancing data with insights into user behaviour, like browsing history, purchase patterns, or interactions.
    
4.  External Data Enrichment: Incorporating external data from other sources, such as business databases or industry reports, to fill it in existing datasets.
    

## Sources Used

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd8qOEjYpetI8Busc6Qc17GzYfdXj-B1tGdXLj45kplCQsr0N45DrjYeiQdKI6G8iS1eWAr-JXdDW8nyrIjNpLUMBS-kNK70w4hdm7ntEE2FHTeKC-ek1i2imH6EB0m6lMVjgT1voCkWYByrVB98-XEsZ5R?key=ndRBfUbM0KWIGmo3udO9Mw)

Img src: [https://mytechmanager.com/the-complete-guide-to-data-enrichment/](https://mytechmanager.com/the-complete-guide-to-data-enrichment/)

  

Many sources can be used for Data Enrichment, some are :

1.  Databases: Databases are crucial as they can provide data that is not usually available outside the organization. They provide important insights like customer behaviour and transaction history, which can enhance your analysis by integrating with external data.
    
2.  APIs: External APIs can provide essential data from the internet and the world based on certain inputs. They can deliver real-time information from various online sources, such as weather, financial, or social media data. This helps keep your datasets current and relevant, improving applications like fraud detection or market analysis.
    
3.  Other Datasets: Combining multiple datasets provides randomness and increases consistency. This method adds depth and accuracy to information. This approach helps uncover trends and validate data by cross-referencing other available datasets.
    

  

# Code

The program developed during this DIY Sprint provides One class for Data Enrichment that further contains several methods to perform data enrichment on a dataset. More details are described below.

  
  

## Class and Its Methods

### EnrichData
The EnrichData class is the main class, to perform data enrichment user has to create an object of this class.

  

    enricher = EnrichData()

  

#### Methods :

 `EnrichIP`: This method adds details related to IP Addresses present in the dataset.
It takes a CSV file containing data as input.
It writes all updated data back to the input file and returns None

Usage Example:

    enricher.EnrichIP('./data.csv')

  <br/>
  
`EnrichFromSQLDatabase`: This method adds more entries into the dataset using the data stored in an SQL Database.
It takes a CSV file containing data and database location as input.
It writes all updated data back to the input file and returns None

Usage Example:

    enricher.EnrichFromSQLDatabase('./data.csv',"./company/employee.db")

  <br/>

`EnrichFromCSV`: This method adds more entries into the dataset using the data stored in another CSV data file.
It takes a CSV file containing data that needs to be updated and another CSV file containing additional data input.
It writes all updated data back to the input file and returns None

Usage Example:

    enricher.EnrichFromCSV('./data.csv',"./datasets/imp.csv")

  
  <br/>

 `FillMissingNumericValues`: This method is used to fill missing numerical values present in the entries of the dataset using the Linear Regression Model.
It takes a CSV file containing data as input.
It writes all updated data back to the input file and returns None

Usage Example:

    enricher.FillMissingNumericValues('./data.csv')
