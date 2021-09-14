
# factory of all the neccessary objects
# This class manages components like 
from core.da.dal import DataAccessLayer
from core.bl import BusinessLayer
from core.rl import ReportingLayer
from core.da.sqlite_dal import SQLiteDataAccessLayer
from core.csv_generator import CSVGenerator

class XManFactory:

    def __init__( self ):
        self.db = 'SQLITE'

    def createObjects( self, dbname : str  ) -> None:
        self.db = dbname 
        
        if str == 'SQLITE':
            self.dal = SQLiteDataAccessLayer() 
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
