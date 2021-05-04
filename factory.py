
# factory of all the neccessary objects
from core.da.dal import DataAccessLayer
from core.bl import BusinessLayer
from core.da.sqlite_dal import SQLiteDataAccessLayer

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
        self.bl.setDALayer( self.dal ) 

    def getBusinessLayer( self ) -> BusinessLayer:
        return self.bl 
