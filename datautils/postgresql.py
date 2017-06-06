# Hamdi Kavak
# 
# MIT License
# Postgresql utilities

import sys
import psycopg2
import csv

## this function saves a postgresql table content to csv file.
def postgresqlToCSV(dbhost, dbname, dbuser, dbpass, tablename,
                    outputfile=None, selectstatement=None, 
                    wherestatement=None):
    # checking all user inputs
    
    # output file name
    if outputfile is None:
        outputfile = tablename
    
    if outputfile.lower().endswith(".csv") is False:
        outputfile = outputfile + ".csv"
    
    # where statement
    if wherestatement is None:
        wherestatement = ""
    elif wherestatement.lower().trim().startswith("where"):
        wherestatement = " " + wherestatement
    else:
        wherestatement = " WHERE " + wherestatement
    
    # select statement
    if selectstatement is None:
        selectstatement = "SELECT * "
    elif selectstatement.lower().trim().startswith("select"):
        selectstatement = " " + selectstatement
    else:
        selectstatement = "SELECT " + selectstatement
    
    # connecting to the DB
    try:
        conn = psycopg2.connect("dbname=" + dbname + " " +
                                "user=" + dbuser + " " +
                                "host=" + dbhost + " " + 
                                "password=" + dbpass)
    except:
        sys.exit("Database connection failed")
    
    print "Database connection established"
    
    cur = conn.cursor()

    # get all data from the db table
    cur.execute(selectstatement + " FROM " + tablename + 
                wherestatement)
    rows = cur.fetchall()

    # write data to a csv file
    with open(outputfile, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    
    conn.close()
    return 









