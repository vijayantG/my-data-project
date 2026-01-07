def normalize_salary(df):
    df["salary"] = df["salary"].fillna(0)
    return df
