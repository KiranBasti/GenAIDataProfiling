import pandas as pd
import csv

def readCSV(fileName):
    rowArray = []
    with open(fileName, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            rowArray.append(row)
            print(row)
    return rowArray

def isValidCurrency(currency, currencyCodes):
    currencyFlag = []
    for data in currency:
        #print(data)
        #print (data in currencyCodes)
        currencyFlag.append(data in currencyCodes)
    return currencyFlag

def isCrossCountry(inputCountryCurrencyMap, countryCurrencyMap):
    crossBorderFlag = []
    for data in inputCountryCurrencyMap:
        print(data + ":" + inputCountryCurrencyMap[data])
        crossBorderFlag.append(data in countryCurrencyMap and countryCurrencyMap[data] == inputCountryCurrencyMap[data])
    print(crossBorderFlag)
    crossBorderFlag.append(True)
    return crossBorderFlag
   
# Load dataset

transactionRows = readCSV('transaction_data.csv')
print (transactionRows)

file_path = r'F:\GitHub\GenAIDataProfiling\InputFiles\transaction_data.csv'
currenyCodes_file_path = r'F:\GitHub\GenAIDataProfiling\InputFiles\ISO_4217_Currency_Codes.csv'


df = pd.read_csv(file_path)
currenyCodes_df = pd.read_csv(currenyCodes_file_path)
currencyCodes = currenyCodes_df['Currency Code']
countryCodes = currenyCodes_df['Country Code']
countries = df['Country']
currencies = df['Currency']

currencyArray=[]
countryCurrencyMap = {}
print(len(currencyCodes))
for i in range (0, len(currencyCodes)):
    currencyArray.append(currencyCodes[i])
    entry = {currencyCodes[i]:countryCodes[i]}
    countryCurrencyMap.update(entry)


inputCountryCurrencyMap = {}
print(len(currencyCodes))
for i in range (0, len(countries)):
    entry = {currencies[i]:countries[i]}
    inputCountryCurrencyMap.update(entry)
    
print(countryCurrencyMap)
print(inputCountryCurrencyMap)


df['Account_Balance_Flag'] = df['Account_Balance'] < 0
df['Currency_Flag'] = isValidCurrency(df['Currency'], currencyArray)
df['Transaction_Amount_Flag'] = df['Transaction_Amount'] >= 10000

from datetime import datetime, timedelta

df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])
max_date = datetime.today() - timedelta(days=365)
df['Old_Transaction_Flag'] = df['Transaction_Date'] < max_date
df['Cross_Border_Flag'] = isCrossCountry(inputCountryCurrencyMap, countryCurrencyMap)

print(df.info())
print(df.head())

df.to_csv(r'F:\GitHub\GenAIDataProfiling\InputFiles\flagged_transactions.csv', index=False)


