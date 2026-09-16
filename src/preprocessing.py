import pandas as pd


def check_data_quality(df):
    print("Shape:", df.shape)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nData types:")
    print(df.dtypes)


def add_crop_features(df):
    df = df.copy()

    df["Yield_per_Hectare"] = (
        df["Production_Tonnes"] /
        df["Area_Hectares"]
    )

    df["Fertilizer_per_Hectare"] = (
        df["Fertilizer_Kg"] /
        df["Area_Hectares"]
    )

    return df
