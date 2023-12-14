# Values could be SQLITE or MYSQL - these are the 2 supported databases
DBTYPE=MYSQL

# There are no specific configurations for SQLite - the data file will be placed in the db folder

# DB Parameters required for MySQL
USERNAME=xmanapp
PASSWORD=xmanapp
HOST=localhost
DB=xman

# Calling the main controller code to start the web application
python3 controller.py $DBTYPE $USERNAME $PASSWORD $HOST $DB 
