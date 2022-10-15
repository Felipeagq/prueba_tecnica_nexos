import pandas as pd
from app.db.postgres.pg_core import engine

def load_csv(path_csv):
    df = pd.read_csv(path_csv)
    return df

def load_to_sql(
    df:pd.DataFrame,
    table_name:str,
    motor
):
    try:
        df.to_sql(
            table_name,
            motor,
            index=False,
            index_label="id",
            if_exists="append"
        )
        return True
    except Exception as e:
        print(f"{e} - {e.__class__}")
        return f"{e} - {e.__class__}"