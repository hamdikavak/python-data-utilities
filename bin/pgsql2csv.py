import sys
from optparse import OptionParser
import data_utils.db as du

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

du.postgresqlToCSV(options.dbhost, options.dbname, options.dbuser,
                   options.dbpass, options.tablename, 
                   outputfile=options.outputfile, 
                   selectstatement=options.selectstatement, 
                   wherestatement=options.wherestatement)
