"""
File:           coin_crawler.py
Author:         Dibyaranjan Sathua
Created on:     03/05/21, 3:58 pm
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd


class CoinCrawler:
    """ Scrap top gainers and losers from coin website """
    BASE_URL = "https://coinmarketcap.com/gainers-losers/"

    def __init__(self):
        self._session = requests.session()
        self._soup = None
        self._gainers_df = None
        self._losers_df = None

    def crawl(self):
        """ Crawl the page """
        gainer_records = []
        loser_records = []
        response = self._session.get(url=self.BASE_URL)
        if not response.ok:
            print(f"Error getting response from {self.BASE_URL}")
        self._soup = BeautifulSoup(response.text, "html.parser")
        div_row = self._soup.find("div", attrs={"class": "uikit-row"})
        for child in div_row.children:
            h3_tag = child.find("h3")
            if h3_tag is not None and h3_tag.text == "Top Gainers":
                gainer_records = self.get_table_data(child)
            if h3_tag is not None and h3_tag.text == "Top Losers":
                loser_records = self.get_table_data(child)

        if gainer_records:
            self._gainers_df = pd.DataFrame(gainer_records)
        if loser_records:
            self._losers_df = pd.DataFrame(loser_records)

    @staticmethod
    def get_table_data(child):
        """ Extract table data and store as a list of dict """
        records = []
        headers = [x.text for x in child.select("thead tr th")]
        # Get the tbody
        tbody = child.find("tbody")
        for tr in tbody.children:
            row_data = [x.text for x in tr.select("td")]
            records.append(dict(zip(headers, row_data)))
        return records

    @property
    def gainers_df(self):
        return self._gainers_df

    @property
    def losers_df(self):
        return self._losers_df
