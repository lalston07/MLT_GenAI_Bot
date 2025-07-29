"""
    PROJECT: BUILDING A CIK LOOKUP MODULE

    The SEC has a page where CIK data is in 3 formats: 
    (1) company_tickers.json - data file for ticker, CIK, EDGAR conformed company name associations
    (2) company_tickers_exchange.json - data file for EDGAR conformed conpany name, CIK, ticker, exchange associations
    (3) company_tikers_mf.json - fund CIK, series, class, ticker

    This Python Module will be a class that initializes and stroes the EDGAR company data into a dictionary.
    Once we store the data we can use it to go from company name or ticker to the CIK number

    Objectives:
    (1) write a class that initializes two dictionaries
        (a) one where the company name is the key
        (b) one where the stock ticker is the key
    (2) when the method initializes it should retrieve a fresh copy of the data form the URLs provided
        by SEC EDGAR; this will allow your function to always have the latest/correct data
    (3) the class should have two methods (method names should follow PEP8 style guide)
        (a) ex: name_to_cik
        (b) ex: ticker_to_cik
        (c) return values should at least include CIK, Name, Ticker, but can include more
"""

import numpy as np
np.log