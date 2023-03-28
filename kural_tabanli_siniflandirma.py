
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("hafta1(Python)/persona.csv")

def check_df(dataframe, head=5):
    print("############################ SHAPE ###########################")
    print(dataframe.shape)
    print("########################### TYPES ############################")
    print(dataframe.dtypes)
    print("############################ HEAD ###########################")
    print(dataframe.head())
    print("############################ NULL ###########################")
    print(df.isna().sum())

check_df(dataframe=df)


agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values(by="PRICE", ascending=False)
agg_df


agg_df.reset_index(inplace=True)
agg_df.head()


lst = [0, 18, 24, 31, 40, 70]
myLabels = ["0_18", "19_23", "24_30", "31_40", "41_70"]
agg_df["age_cat"] = pd.cut(agg_df["AGE"], lst, labels=myLabels)
agg_df.head()


agg_df["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" +row[2].upper() + "_" +row[5].upper() for row in agg_df.values]
agg_df = agg_df[["customers_level_based", "PRICE"]]

agg_df = agg_df.groupby("customers_level_based").aggregate({"PRICE": "mean"})
agg_df = agg_df.reset_index()
agg_df.head()


agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.head()


new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]


musteri1 = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == musteri1]
