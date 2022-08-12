import pandas as pd

df = pd.read_csv("webautomation_coursera.csv")
df
df.shape()

unicompany = df["associated-university-institution-company"].value_counts()
unicompany

wt = df.loc[(df["associated-university-institution-company"]=="-")]
wt

category = df["category-subject-area"].value_counts()
category

sum(category)

lang = df["language"].value_counts()
lang

turk = df.loc[(df["language"]=="Turkish")]
turk

level = df["level"].value_counts()
level

rat = df.sort_values("rating")
rat

rating = df["rating"].value_counts()
rating

df.loc[(df["rating"]=="4.1")]
