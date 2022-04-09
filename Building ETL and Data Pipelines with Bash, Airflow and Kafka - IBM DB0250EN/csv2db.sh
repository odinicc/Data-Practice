# This script
# Extracts data from /etc/passwd file into a CSV file.

# The csv data file contains the user name, user id and 
# home directory of each user account defined in /etc/passwd

# Transforms the text delimiter from ":" to ",".
# Loads the data from the CSV file into a table in PostgreSQL database.

# Extract phase

echo "Extracting data"

# Extract the columns 1 (user name), 2 (user id) and 
# 6 (home directory path) from /etc/passwd

cut -d":" -f1,3,6 /etc/passwd > extracted-data.txt

# Transform phase
echo "Transforming data"
# read the extracted data and replace the colons with commas.

tr ":" "," < extracted-data.txt > transformed-data.csv

echo "Loading data"

echo "\c template1;\COPY users  FROM '/home/project/transformed-data.csv' DELIMITERS ',' CSV;" | psql --username=postgres --host=localhost