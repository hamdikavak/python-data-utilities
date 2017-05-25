# python-data-utilities
Collection of utilities to conduct simple data operations using python over PostgreSQL databases and more. I do not promise super efficient and elegant code as I publish this while I am learning python.

## pgsql2csv
Exports a PostgreSQL table to a .csv file.

Usage (required parameters):
```sh
python pgsql2csv.py -h <db host address> -u <db user> -n <db name> -p <db password> -t <tablename>
```

optional parameters:
```sh
... -s <select statement> -o <output file path> -w <where statement>
```
