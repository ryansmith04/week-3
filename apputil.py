import seaborn as sns
import pandas as pd
import numpy as np


url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)


# update/add code below ...


def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def to_binary(n):
    """Return the binary representation of a non-negative integer."""
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return to_binary(n // 2) + str(n % 2)


def task_1():
    """Return column names sorted by number of missing values."""
    print("Checking gender values:")
    print(df_bellevue['gender'].value_counts(dropna=False))

    gender = df_bellevue['gender'].replace(
        ['?', 'g', 'h'], np.nan
    )

    missing_values = df_bellevue.isna().sum()
    missing_values['gender'] = gender.isna().sum()

    return missing_values.sort_values().index.tolist()


def task_2():
    """Return the total number of admissions for each year."""
    dates = pd.to_datetime(df_bellevue['date_in'], errors='coerce')

    if dates.isna().any():
        print("Some date values are invalid or missing and were excluded.")

    return (
        dates.dropna()
        .dt.year
        .value_counts()
        .sort_index()
        .rename_axis('year')
        .reset_index(name='total_admissions')
    )


def task_3():
    """Return the average age for each gender."""
    if df_bellevue['age'].isna().any():
        print("Some age values are missing and excluded from the average.")
    return df_bellevue.groupby('gender')['age'].mean()


def task_4():
    """Return the five most common professions."""
    return (
        df_bellevue['profession']
        .value_counts()
        .head(5)
        .index
        .tolist()
    )
    