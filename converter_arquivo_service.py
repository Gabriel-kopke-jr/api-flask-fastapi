import pandas as pd
def get_data_from_request(data:bytes):
    data_str = data.decode('utf-8')
    headers = data_str.split('\n')[0]
    headers_adjusted = headers.split(',')
    content = data_str.split('\n')[1:]
    content_adjusted = [tuple(element.split(',')) for element in content]
    df_data = pd.DataFrame(data=content_adjusted, columns=headers_adjusted)
    return df_data