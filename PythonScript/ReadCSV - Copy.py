import pandas as pd

def isValidCurrency(currency, currencyCodes):
    currencyFlag = []
    for data in df['Currency']:
        currencyFlag.append(data in CurrencyCode)
    return currencyFlag
    
# Load dataset
file_path = r'F:\GitHub\GenAIDataProfiling\InputFiles\transaction_data.csv'
currenyCodes_file_path = r'F:\GitHub\GenAIDataProfiling\InputFiles\ISO_4217_Currency_Codes.csv'

CurrencyCode = ["AFN", "EUR", "ALL", "DZD", "USD", "EUR", "AOA", "XCD", "ARS", "AMD", "AWG",
        "AUD", "AZN", "BHD", "BHD", "BDT", "BBD", "BYN", "BZD", "XOF", "BMD",
        "BTN", "BOB", "BOV", "BAM", "BWP", "NOK", "BRL", "BND", "BGN", "BIF",
        "CVE", "KHR", "XAF", "CAD", "KYD", "CLP", "CLF", "CNY", "COP", "KMF",
        "CDF", "NZD", "CRC", "CUP", "CUC", "ANG", "CZK", "DKK", "DJF", "DOP",
        "EGP", "SVC", "ERN", "EUR", "ETB", "FKP", "FJD", "XPF", "EUR", "EUR",
        "XAF", "GMD", "GEL", "EUR", "GHS", "GIP", "EUR", "GTQ", "GNF", "GYD",
        "HTG", "HNL", "HKD", "HUF", "ISK", "INR", "IDR", "XDR", "IRR", "IQD",
        "EUR", "ILS", "EUR", "JMD", "JPY", "JOD", "KZT", "KES", "KPW", "KRW",
        "KWD", "KGS", "LBP", "LSL", "LRD", "LYD", "CHF", "EUR", "EUR", "MOP",
        "MKD", "MGA", "MWK", "MYR", "MVR", "MRO", "MUR", "MXN", "MDL", "MNT",
        "EUR", "MAD", "MZN", "MMK", "NAD", "NPR", "EUR", "TWD", "NIO", "NGN",
        "NZD", "OMR", "PKR", "PAB", "PGK", "PYG", "PEN", "PHP", "PLN", "EUR",
        "QAR", "RON", "RUB", "RWF", "SHP", "WST", "STD", "SAR", "RSD", "SCR",
        "SLL", "SGD", "EUR", "EUR", "SBD", "SOS", "ZAR", "SSP", "EUR", "LKR",
        "SDG", "SRD", "SZL", "SEK", "SYP", "TJS", "TZS", "THB", "TOP", "TTD",
        "TND", "TRY", "TMT", "UGX", "UAH", "AED", "GBP", "USD", "UYU", "UZS",
        "VUV", "VEF", "VND", "YER", "ZMW", "ZWL"]
    


df = pd.read_csv(file_path)
currenyCodes_df = pd.read_csv(currenyCodes_file_path)
CurrencyCode = currenyCodes_df['Currency Code']


df['Account_Balance_Flag'] = df['Account_Balance'] < 0
df['Currency_Flag'] = isValidCurrency(df['Currency'], CurrencyCode)
df['Transaction_Amount_Flag'] = df['Transaction_Amount'] >= 10000

from datetime import datetime, timedelta

df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])
max_date = datetime.today() - timedelta(days=365)
df['Old_Transaction_Flag'] = df['Transaction_Date'] < max_date

print(df.info())
print(df.head())

df.to_csv(r'F:\GitHub\GenAIDataProfiling\InputFiles\flagged_transactions.csv', index=False)


