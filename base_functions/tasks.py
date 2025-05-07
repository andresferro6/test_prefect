import pandas as pd
from prefect import task

@task
def process_dataframe():
    df = pd.DataFrame()
    return df