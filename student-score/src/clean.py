import pandas as pd
from pandas.conftest import index


def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)
    print('===缺失值情况===')
    print(df.isnull().sum)

    df_filled = df.fillna(df.mean(numeric_only=True)) #缺失值用平均值填补， 只用数字做平均
    print('===缺失值已填补===')
    print(df_filled)

    df_filled.to_csv(output_file, index=True)

