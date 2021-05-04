
# core business logic is initiated from this class

from core.da.dal import DataAccessLayer
from core.expense_category import ExpenseCategory

class BusinessLayer:

    def __init__( self ):
        pass 

    def setDALayer( self, dal : DataAccessLayer ) -> None:
        self.dal = dal 
    
    def addExpenseCategory( self, expense_category : ExpenseCategory ):
        # TODO : any business logic? and then call the DA layer
        self.dal.addExpenseCategory( expense_category ) 

    def listExpenseCategories( self ) -> list :
        return [ ExpenseCategory( row[ 1 ], row[ 2 ] ) for row in self.dal.listExpenseCategories() ] 

    def addStore( self ):
        pass 

    def listStores( self ):
        pass 
