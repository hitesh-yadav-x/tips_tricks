### Pandas Tips tricks and Issues
---
1. String integers are read incorrectly in pandas.read_json  
   The issue is related to how pandas converts the values to integers. It's a known [issue](https://github.com/pandas-dev/pandas/issues/20608#) and is open.
   Fis is to explicity set the dtype for the integer field. Exmaple code [here](read_json.py).