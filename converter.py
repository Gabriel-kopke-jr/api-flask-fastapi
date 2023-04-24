import pandas as pd
from pandas import DataFrame


def convert_csv_to_json(data_frame: DataFrame):
  lista_output = [
    {'Number':data_frame['Number'][i], 'Name': data_frame['Name'][i], 'Age': data_frame['Age'][i], 'City': data_frame['City'][i], 'Country': data_frame['Coutry'][i]}
    for i in range(data_frame.shape[0])
    ]
  return lista_output