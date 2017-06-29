Collection of utilities to conduct simple data operations using python over PostgreSQL databases and more. I do not promise super efficient and elegant code as I publish this while I am learning python.

# Installation
```sh
python setup.py install
```

# Troubleshooting

`Error: pg_config executable not found.` 

If you come across the above error, you need to install a postgresql instance and export its `bin` folder address to the `PATH` variable. In MacOS, you can install using `brew install postgresql` 

# Usage
## 1. pgsql2csv
Exports a PostgreSQL table to a .csv file.

*as a command line tool*
w/ required parameters:
```sh
pgsql2csv.py -h <db address> -u <db user> -n <db name> -p <db password> -t <tablename>
```

w/ optional parameters:
```sh
... -s <select statement> -o <output file path> -w <where statement>
```

*as a python package*
```python
import datautils as du

du.postgresqlToCSV("db_address","db_name", "db_user",
                   "db_pass", "table_name", 
                   outputfile="output_file_name", # optional
                   selectstatement="comma separated column names", # optional
                   wherestatement="conditional statements") # optional
```

## 2. plotting utilities

```python
import numpy as np
from pandas import Series, DataFrame
import datautils as du

rownames = ['row1', 'row2', 'row3', 'row4', 'row5']
colnames = ['col1', 'col2']
rowdata = np.random.randn(5, 2)*100
df_obj = DataFrame(rowdata, 
                   index=rownames,  
                   columns=colnames)

bar_prop = {'col1':{'color': 'r', 'label': 'Col 1 values'},
            'col2':{'color': 'g', 'label': 'Col 2 values'}}

du.makeBarPlot(df_obj, bar_prop, ylim=None)
```
