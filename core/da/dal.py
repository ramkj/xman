

import abc 

from core.expense_category import ExpenseCategory


class DataAccessLayer (metaclass=abc.ABCMeta):
    
    def __init__( self ) :
        pass

    @abc.abstractmethod 
    def addExpenseCategory( self, expense_category : ExpenseCategory ) -> None :
        raise NotImplementedError 
    
    @abc.abstractmethod 
    def listExpenseCategories( self ) -> list :
        raise NotImplementedError 
