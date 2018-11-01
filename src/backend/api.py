import pandas as pd
import json


THE_FILE = "./vehicles.csv"

if __name__ == "__main__":
    # open the csv with pandas
    csv_obj = pd.read_csv(THE_FILE, sep=",")

    # test filter/search string
    SEARCH_QUERY = 'mercedes'
    FILTER_VEHICLE_MAKE = csv_obj['Make'].str.contains(SEARCH_QUERY.upper())

    # test 5 rows first
    filter_output = csv_obj[FILTER_VEHICLE_MAKE].head()

    # print out dataframe test, run with $ python api.py
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(filter_output)

    # convert to json, test print
    jsoned = filter_output.to_json(orient='index')
    print(jsoned)

    json_data = json.loads(jsoned)
    # print(json_data['1'])

    # iterate json data
    for item in json_data:
        ret_id = json_data[item]['Vehicle ID']
        ret_make = json_data[item]['Make']
        ret_model_s = json_data[item]['Short Model']
        ret_model_l = json_data[item]['Long Model']
        ret_trim = json_data[item]['Trim']
        ret_derivative = json_data[item]['Derivative']
        ret_year = json_data[item]['Year introduced']
        ret_discontinued = json_data[item]['Year discontinued']
        print("ID: {} Derivative: {}".format(ret_id, ret_derivative))

