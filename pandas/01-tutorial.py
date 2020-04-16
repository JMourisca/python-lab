#!/usr/bin/env python3
# Source https://realpython.com/pandas-python-explore-dataset/
import requests
import pandas as pd

# def download():
#     download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
#     target_csv_path = "nba_all_elo.csv"

#     response = requests.get(download_url)
#     response.raise_for_status() # Check it the request was successful

#     with open(target_csv_path, "wb") as f:
#         f.write(response.content)

#     print("Download finished")


# nba = pd.read_csv("nba_all_elo.csv") # nba.shape returns a tuple with # of rows and # of columns
# pd.set_option("display.precision", 2)
# # print(nba.head(2))
# # print(nba.tail(3))
# # print(nba.info())
# print(nba.describe())

path = "/Users/juliana/Work/Code/COVID-19/"
source = "csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"

cov = pd.read_csv(path + source)

print(cov.loc[cov["Country/Region"] == "Brazil", "3/20/20"].value_counts())