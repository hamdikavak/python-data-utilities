# python-data-utilities
Collection of utilities to conduct simple data operations using python over PostgreSQL and more. I do not promise super efficient and elegant code as I publish this while I am learning python.

## 1. pgsql2csv

Usage (required parameters):
```sh
python pgsql2csv.py -h <postgresql db host name> -u <db user> -n <db name> -p <db password> -t <tablename>
```

optional parameters:
```sh
... -s <select statement> -o <output file path>
```
