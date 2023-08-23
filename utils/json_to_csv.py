import pandas as pd
import json
from pathlib import Path


def json_to_csv():
    """
    Convert json file into a csv file.
    """
    path_to_open = Path.cwd() / "data" / "properties_data.json"
    path_to_save = Path.cwd() / "data" / "properties_data.csv"

    with open(path_to_open, "r", encoding="utf-8") as file:
        data = json.load(file)

    df = pd.DataFrame.from_dict(data, orient='index')
    df.to_csv(path_to_save, index_label="id", encoding="utf-8")
    print(df.head())
