import pandas as pd

json_content = """
{ 
    "1": {
        "id": "9999999999999998", 
    }, 
    "2": {
        "id": "9999999999999999", 
    },
    "3": {
        "id": "10000000000000001", 
    },
    "4": {
        "id": "10000000000000002", 
    }
}
"""
# Large integers are converted to incorrect values.
df = pd.read_json(json_content,
                  orient='index',  # read as transposed
                  convert_axes=False,  # don't convert keys to dates
                  )
print(df.info())
print(df)

# Fix is to explicitly pass the dtypes in read_json method
df2 = pd.read_json(json_content,
                  orient='index',  # read as transposed
                  convert_axes=False,  # don't convert keys to dates
                  dtype= {'id': 'int64'}
                  )
print(df2.info())
print(df2)
