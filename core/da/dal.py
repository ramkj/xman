import abc 

from core.expense_category import ExpenseCategory
from core.store import Store
from core.person import Person 
from core.payment_type import PaymentType

class DataAccessLayer (metaclass=abc.ABCMeta):
    
    def __init__( self ) :
        pass

    @abc.abstractmethod 
    def addExpenseCategory( self, expense_category : ExpenseCategory ) -> None :
        raise NotImplementedError 

    @abc.abstractmethod 
    def addStore( self, store : Store ) -> None :
        raise NotImplementedError     

    @abc.abstractmethod 
    def listExpenseCategories( self ) -> list :
        raise NotImplementedError 
    
    @abc.abstractmethod 
    def listStores( self ) -> list :
        raise NotImplementedError 
    
    @abc.abstractmethod 
    def listExpenses( self ) -> list:
        raise NotImplementedError

    @abc.abstractmethod
    def listPeople( self ) -> list:
        raise NotImplementedError
    
    @abc.abstractmethod
    def listPaymentTypes( self ) -> list:
        raise NotImplementedError

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
