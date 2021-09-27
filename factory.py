
# factory of all the neccessary objects
# This class manages components like 
from core.da.dal import DataAccessLayer
from core.bl import BusinessLayer
from core.rl import ReportingLayer
from core.da.sqlite_dal import SQLiteDataAccessLayer
from core.da.mysql_dal import MySQLDataAccessLayer
from core.csv_generator import CSVGenerator

class XManFactory:

    def __init__( self ):
        # default configuration set to SQLite
        self.dbconfig =  { 'dbtype' : 'SQLITE' } 

    def createObjects( self, dbargs : dict  ) -> None:
        self.dbconfig = dbargs

        # DA is set based on the parameter passed (from command line)        
        if self.dbconfig[ 'dbtype'] == 'SQLITE':
            self.dal = SQLiteDataAccessLayer() 
        elif self.dbconfig[ 'dbtype'] == 'MYSQL':
            self.dal = MySQLDataAccessLayer( self.dbconfig )     
        else:
            self.dal = SQLiteDataAccessLayer() 

        self.bl = BusinessLayer() 
        self.rl = ReportingLayer()
        self.csv_generator = CSVGenerator()
        self.bl.setDALayer( self.dal ) 
        self.rl.setDALayer( self.dal )


    def getBusinessLayer( self ) -> BusinessLayer:
        return self.bl 

    def getReportingLayer( self ) -> BusinessLayer:
        return self.rl

    def getCSVGenerator( self ) -> CSVGenerator:
        return self.csv_generator
