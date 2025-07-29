"""
    PROJECT: SEC EDGAR API LIBRARY

    For this project, we are going to expand our CIK Lookup Module to add additional methods to make 
    it a client we can use to find and retrieve the 10K and 10Q documents.

    Objectives:
    (1) Read through the links in the course site and test the API by making calls with cURL and inspecting the results
    (2) Find a Company 10Q
        (a) search for a company
        (b) find the least 10Q they submitted
        (c) open the 10Q
        (d) skim through it to better understand the type of information included
"""

import requests

class SecEdgar:
    def __init__(self, fileurl):
        self.fileurl = fileurl
        self.name_dict = {}
        self.ticker_dict = {}

        headers = {'user-agent': 'MLT LA leilaalston07@gmail.com'}  # replace with your information
        r = requests.get(self.fileurl, headers=headers)

        if r.status_code == 200: 
            self.filejson = r.json()
            self.cik_json_to_dict()
        else:
            print(f"Error fetching data: {r.status_code}")
            self.filejson = {}

    def cik_json_to_dict(self):
        for entry in self.filejson.values():
            cik = str(entry['cik_str']).zfill(10)
            name = entry['title'].strip().upper()
            ticker = entry['ticker'].strip().upper()
            info = (cik, name, ticker)
            self.name_dict[name] = info
            self.ticker_dict[ticker] = info
    
    def name_to_cik(self, name):
        return self.name_dict.get(name.strip().upper())
    
    def ticker_to_cik(self, ticker):
        return self.ticker_dict.get(ticker.strip().upper())

se = SecEdgar('https://www.sec.gov/files/company_tickers.json')

print(se.ticker_to_cik('AAPL'))
print(se.name_to_cik('Apple Inc.'))