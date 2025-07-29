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
        self.namedict = {}
        self.tickerdict = {}

        headers = {'user-agent': 'MLT <intials> <user.gmail.com>'}
        r = requests.get(self.fileurl, headers=headers)

        self.filejson = r.json

        print(r.text)
        print(self.filejson)

        self.cik_json_to_dict()

    def cik_json_to_dict(self):
        self.name_dict = {}
        self.ticker_dict = {}

se = SecEdgar('https://www.sec.gov/files/company_tickers.json')