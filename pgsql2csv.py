#!/usr/bin/python

#===============================================================================
# MIT License
# 
# Copyright (c) 2017 Hamdi Kavak
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#===============================================================================

import sys
from optparse import OptionParser
import psycopg2
import csv

parser = OptionParser(add_help_option=False)

# adding parameters can be passed from command line
parser.add_option("-h", "--host", action="store", dest="dbhost", 
                  type="string", help="Database host address")
parser.add_option("-n", "--name", dest="dbname", 
                  type="string", help="Database name")
parser.add_option("-u", "--user", dest="dbuser", 
                  type="string", help="Database user")
parser.add_option("-p", "--password", action="store", dest="dbpass", 
                  type="string", help="Database password")
parser.add_option("-t", "--table", dest="tablename", 
                  type="string", help="Table name")
parser.add_option("-o", "--out", dest="outputfile", 
                  type="string", help="Output file (default=table name)")
parser.add_option("-s", "--select", dest="selectstatement", default="*", 
                  type="string", help="Select columns to be included")
parser.add_option("-w", "--where", dest="wherestatement", 
                  type="string", help="Filter data through WHERE statement. " + 
                  "Do not include WHERE")

(options, args) = parser.parse_args()

# making sure all required db connection parameters are passed
if options.dbhost is None or options.dbname is None or \
   options.dbuser is None or options.dbpass is None:
   parser.print_help()
   sys.exit()

# table name is required
if options.tablename is None:
    print "Please identify a table name"
    parser.print_help()
    sys.exit()

# lets use the provided filename or use the table name
if options.outputfile is None:
    outputfile = options.tablename + ".csv"
else:
    outputfile = options.outputfile + ".csv"
    
# checking where statement
if options.wherestatement is None:
    wherestatement = ""
else:
    wherestatement = " WHERE "+ options.wherestatement

# connecting to the DB
try:
    conn = psycopg2.connect("dbname=" + options.dbname + " " +
                            "user=" + options.dbuser + " " +
                            "host=" + options.dbhost + " " + 
                            "password=" + options.dbpass)
except:
    sys.exit("Database connection failed")
    
print "Database connection established"

cur = conn.cursor()

# get all data from the db table
cur.execute("SELECT " + options.selectstatement + " FROM " + 
            options.tablename + wherestatement)
rows = cur.fetchall()

# write data to a csv file
with open(outputfile, 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

conn.close()