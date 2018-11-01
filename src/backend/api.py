import pandas as pd
import json
import hug

THE_FILE = "./vehicles.csv"

def cors_support(response, *args, **kwargs):
    response.set_header('Access-Control-Allow-Origin', '*')

@hug.cli()
@hug.local()
@hug.get("/get_vehicle", examples="info=12345", requires=cors_support)
def get_vehicle(info: hug.types.number):
    csv_obj = pd.read_csv(THE_FILE, sep=",", index_col=False)


    # test filter/search string
    FILTER_VEHICLE_MAKE = csv_obj['Vehicle ID'] == info

    # test 5 rows first
    filter_output = csv_obj[FILTER_VEHICLE_MAKE]

    # print out dataframe test, run with $ python api.py
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(filter_output)

    # convert to json, test print
    jsoned = filter_output.to_json(orient='index')
    json_data = json.loads(jsoned)
    print(json_data)
    return {'data': json_data}
