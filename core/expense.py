
from core.payment_type import PaymentType
from core.person import Person
from core.store import Store
from core.expense_category import ExpenseCategory
import datetime 

class Expense:
    def __init__( self, id : int, expense_detail : str, expense_date, expense_amount : float, \
                    person : Person, store : Store, expense_category : ExpenseCategory, \
                    payment_type : PaymentType ):
        self.id = id 
        self.expense_detail = expense_detail
        self.expense_date = expense_date 
        self.expense_amount = expense_amount 
        self.person = person 
        self.store = store 
        self.expense_category = expense_category 
        self.payment_type = payment_type
    
    def getId( self ) -> int:
        return self.id

    def getExpenseDetail( self ) -> str:
        return self.expense_detail 
    
    def getExpenseDate( self ) -> datetime:
        return self.expense_date

    def getExpenseAmount( self ) -> float:
        return self.expense_amount
    
    def getPerson( self ) -> Person:
        return self.person 
    
    def getStore( self ) -> Store:
        return self.store 
    
    def getExpenseCategory( self ) -> ExpenseCategory:
        return self.expense_category
    
    def getPaymentType( self ) -> PaymentType:
        return self.payment_type

