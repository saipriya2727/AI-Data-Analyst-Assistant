import pandas as pd

def load_data(uploaded_file):

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    return df


def get_dataset_summary(df):

    summary = f"""
Dataset Summary

Number of Rows : {df.shape[0]}
Number of Columns : {df.shape[1]}

Column Names:
{list(df.columns)}

Missing Values:
{df.isnull().sum().to_string()}

Duplicate Rows:
{df.duplicated().sum()}

Data Types:
{df.dtypes.to_string()}
"""

    return summary


def answer_data_question(df, question):

    question = question.lower()

    if "rows" in question:
        return f"The dataset has {df.shape[0]} rows."

    elif "columns" in question:
        return f"Columns are:\n{', '.join(df.columns)}"

    elif "missing" in question:
        return str(df.isnull().sum())

    elif "duplicate" in question:
        return f"Duplicate rows: {df.duplicated().sum()}"

    elif "shape" in question:
        return f"Dataset shape: {df.shape}"

    else:
        return None