"""
File:           main.py
Author:         Dibyaranjan Sathua
Created on:     03/05/21, 4:42 pm
"""
from src.coin_crawler import CoinCrawler


def main():
    """ Main function """
    crawler = CoinCrawler()
    crawler.crawl()
    print(crawler.gainers_df)
    print(crawler.losers_df)


if __name__ == "__main__":
    main()
