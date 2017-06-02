# Data utilities for pyhton
Collection of utilities to conduct simple data operations using python over PostgreSQL databases and more. I do not promise super efficient and elegant code as I publish this while I am learning python.

## installation
```sh
python setup.py install
```

## usage
### pgsql2csv
Exports a PostgreSQL table to a .csv file.

w/ required parameters:
```sh
python pgsql2csv.py -h <db host address> -u <db user> -n <db name> -p <db password> -t <tablename>
```

w/ optional parameters:
```sh
... -s <select statement> -o <output file path> -w <where statement>
```

## Troubleshooting

`Error: pg_config executable not found.` 

If you come across the above error, you need to install a postgresql instance and export its `bin` folder address to the `PATH` variable. In MacOS, you can install using `brew install postgresql` 