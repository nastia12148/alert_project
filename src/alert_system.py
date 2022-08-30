import pandas as pd
from datetime import datetime
import pyspark
#from pyarrow import StructType
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, IntegerType, StringType, BooleanType, DoubleType, StructType


def log_reader(filepath):
    df = pd.read_csv(filepath , names=['error_code',
                                                               'error_message',
                                                               'severity',
                                                               'log_location',
                                                               'mode',
                                                               'model',
                                                               'graphics',
                                                               'session_id',
                                                               'sdkv',
                                                               'test_mode',
                                                               'flow_id',
                                                               'flow_type',
                                                               'sdk_date',
                                                               'publisher_id',
                                                               'game_id',
                                                               'bundle_id',
                                                               'appv',
                                                               'language',
                                                               'os',
                                                               'adv_id',
                                                               'gdpr',
                                                               'ccpa',
                                                               'country_code',
                                                               'date'],
                     dtype={'test_mode': str, 'gdpr': str, 'ccpa': str},
                     skiprows=1)


    df = df[['severity', 'bundle_id', 'date']]

    print(df.head())

    return df


def alert(df: pd.DataFrame):
    df = df[df["severity"] == "Error"]
    row_number = 0
    beg_time = df["date"].head(1)[0]
    alert_counter = 0

    while row_number < len(df) - 10:
        error_list = df[(beg_time - df["date"]) <= 60].head(10)
        if len(error_list) >= 10:
            # print("Alert!")
            # if go_next():
            row_number += 10
            alert_counter += 1
            beg_time = df.iloc[row_number, 23]
        else:
            row_number += 1
            beg_time = df.iloc[row_number, 23]

    return alert_counter


def alert_by_id(df: pd.DataFrame, bundle_id: str):
    df = df[df["bundle_id"] == bundle_id]
    df = df[df["severity"] == "Error"]

    row_number = 0
    beg_time = df["date"].head(1)[0]

    while True:
        error_list = df[(beg_time - df["date"]) <= 3600].head(10)
        if len(error_list) >= 10:
            print("Alert!")
        if go_next():
            row_number += 1
            beg_time = df.iloc[row_number, 23]
        else:
            break

    return error_list


def go_next():
    yes_or_no = input("Do you want to continue?[yes/no]: ")
    if yes_or_no == "yes":
        return True

    return False



df = log_reader('/home/nastia12148/PycharmProjects/data/data.csv')




print(alert(df))
