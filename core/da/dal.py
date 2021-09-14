import abc 

from core.expense import Expense 
from core.expense_category import ExpenseCategory
from core.store import Store
from core.person import Person 
from core.payment_type import PaymentType

class DataAccessLayer (metaclass=abc.ABCMeta):
    
    def __init__( self ) :
        pass
    
    # Expense methods
    @abc.abstractmethod 
    def addExpense( self, expense: Expense ) -> None:
        raise NotImplementedError 

    @abc.abstractmethod 
    def deleteExpense( self, id : str ) -> None :
        raise NotImplementedError 

    @abc.abstractmethod 
    def listExpenses( self ) -> list:
        raise NotImplementedError

    # Expense Category methods
    @abc.abstractmethod 
    def addExpenseCategory( self, expense_category : ExpenseCategory ) -> None :
        raise NotImplementedError 

    @abc.abstractmethod 
    def deleteExpenseCategory( self, id : str ) -> None :
        raise NotImplementedError     

    @abc.abstractmethod 
    def listExpenseCategories( self ) -> list :
        raise NotImplementedError 

    # Store(s) methods
    @abc.abstractmethod 
    def addStore( self, store : Store ) -> None :
        raise NotImplementedError 

    @abc.abstractmethod 
    def deleteStore( self, Id : str ) -> None :
        raise NotImplementedError     

    @abc.abstractmethod 
    def listStores( self ) -> list :
        raise NotImplementedError 

    # Payment Types 
    @abc.abstractmethod 
    def addPaymentType( self, payment_type : PaymentType ) -> None:
        raise NotImplementedError 

    @abc.abstractmethod
    def deletePaymentType( self, id : str ) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def listPaymentTypes( self ) -> list:
        raise NotImplementedError

    # Person methods 
    @abc.abstractmethod 
    def addPerson( self, person : Person ) -> None:
        raise NotImplementedError 

    @abc.abstractmethod 
    def deletePerson( self, id : str ) -> None :
        raise NotImplementedError     

    @abc.abstractmethod
    def listPeople( self ) -> list:
        raise NotImplementedError

    # Other utility methods
    @abc.abstractmethod
    def getPersonByShortName( self, short_name : str ) -> Person:
        raise NotImplementedError

    @abc.abstractmethod
    def getStoreByStoreName( self, store_name : str ) -> Store:
        raise NotImplementedError

    @abc.abstractmethod
    def getPaymentTypeByMode( self, payment_mode : str ) -> PaymentType:
        raise NotImplementedError

    @abc.abstractmethod
    def getExpenseCategoryByExpenseType( self, expense_type : str ) -> ExpenseCategory:
        raise NotImplementedError
    
    # All reporting functions
    @abc.abstractmethod
    def getExpenseSummaryForMonth( self, search_string : str ) -> tuple:
        raise NotImplementedError

    @abc.abstractmethod
    def getMonthwiseExpenseSummary( self ) -> list:
        raise NotImplementedError

    @abc.abstractmethod
    def getMonthwiseCategoryExpense( self ) -> list:
        raise NotImplementedError

    @abc.abstractmethod
    def getMonthwisePaymentTypeSummary( self ) -> list:
        raise NotImplementedError

    @abc.abstractmethod
    def getMonthwisePersonSummary( self ) -> list:
        raise NotImplementedError