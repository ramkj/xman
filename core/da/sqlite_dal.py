
from core.expense_category import ExpenseCategory
from core.store import Store 
from core.expense import Expense
from core.person import Person 
from core.expense_category import ExpenseCategory
from core.payment_type import PaymentType

from core.da.dal import DataAccessLayer
from core.da.sqlitedriver import SQLiteDriver

class SQLiteDataAccessLayer( DataAccessLayer ):

    def __init__( self ) :
        # TODO: The following line should not be hard coded and should come from param
        self.data_file = './db/expenses.db'
    
    def addExpenseCategory( self, expense_category : ExpenseCategory ) -> None :
        expense_type : str = expense_category.getExpenseType() 
        expense_type_detail : str = expense_category.getExpenseDetail() 

        with SQLiteDriver( self.data_file ) as cursor:
            _SQL = """INSERT INTO EXPENSE_CATEGORY(expense_type, expense_type_detail ) VALUES( ?, ? )"""
            cursor.execute(_SQL, (expense_type, expense_type_detail))
    
    def addStore( self, store : Store ) -> None :
        store_name = store.getStoreName() 
        store_detail = store.getStoreDetail()
        home_delivery = store.getHomeDeliveryString() 

        with SQLiteDriver( self.data_file ) as cursor:
            _SQL = """INSERT INTO STORE(STORE_NAME, STORE_DETAIL, HOME_DELIVERY ) VALUES( ?, ?, ? )"""
            cursor.execute(_SQL, (store_name, store_detail, home_delivery))
    
    def addExpense( self, expense: Expense ) -> None:
        print( 'sqlite_dat: add Expense' )
        expense_detail = expense.getExpenseDetail() 
        expense_date = expense.getExpenseDate() 
        expense_amount = expense.getExpenseAmount() 
        person_id = expense.getPerson().getId() 
        store_id = expense.getStore().getId()
        expense_category_id = expense.getExpenseCategory().getId()
        payment_type_id = expense.getPaymentType().getId() 

        with SQLiteDriver( self.data_file ) as cursor:
            _SQL = """INSERT INTO EXPENSE( EXPENSE_DETAIL, EXPENSE_DATE, EXPENSE_AMOUNT, EXPENSE_CATEGORY_ID, PAYMENT_TYPE_ID, PERSON_ID, STORE_ID ) VALUES( ?, ?, ?, ?, ?, ?, ? )"""
            cursor.execute(_SQL, (expense_detail, expense_date.strftime( '%s' ), expense_amount, expense_category_id, payment_type_id, person_id, store_id )) 

    def listExpenses( self ) -> list:
        contents = [] 
        with SQLiteDriver( self.data_file ) as cursor:
            _SQL = """ SELECT ID, EXPENSE_DETAIL, EXPENSE_DATE, EXPENSE_AMOUNT, 
                        EXPENSE_CATEGORY_ID, PAYMENT_TYPE_ID, PERSON_ID, STORE_ID FROM EXPENSE """
            _ORDERBY = " ORDER BY EXPENSE.EXPENSE_DATE, ID "
            cursor.execute(_SQL + _ORDERBY)
            contents = cursor.fetchall()
        print( contents ) 
        return contents  

    def listExpenseCategories( self ) -> list :
        contents = [] 
        with SQLiteDriver( self.data_file ) as cursor:
            _SQL = """ SELECT ID, expense_type, expense_type_detail FROM expense_category  """
            _ORDERBY = """ ORDER BY expense_type """
            cursor.execute(_SQL + _ORDERBY)
            contents = cursor.fetchall()
        return contents 

    def listStores( self ) -> list :
        contents = [] 
        with SQLiteDriver( self.data_file ) as cursor:
            _SQL = """ SELECT ID, STORE_NAME, STORE_DETAIL, HOME_DELIVERY FROM STORE  """
            _ORDERBY = """ ORDER BY STORE_NAME """
            cursor.execute(_SQL + _ORDERBY)
            contents = cursor.fetchall()
        return contents 
    
    def listPeople( self ) -> list:
        contents = [] 
        with SQLiteDriver( self.data_file ) as cursor:
            _SQL = """SELECT ID, PERSON_FIRST_NAME, PERSON_LAST_NAME, PERSON_SHORT_NAME  from PERSON  """
            cursor.execute( _SQL ) 
            contents = cursor.fetchall() 
        return contents 

    def listPaymentTypes( self ) -> list:
        contents = [] 
        with SQLiteDriver( self.data_file ) as cursor:
            _SQL = """SELECT ID, PAYMENT_MODE, PAYMENT_MODE_DETAIL from PAYMENT_TYPE  """
            cursor.execute( _SQL ) 
            contents = cursor.fetchall() 
        return contents 
    
    def getPersonByShortName( self, short_name : str  ) -> Person:
        contents = [] 
        with SQLiteDriver( self.data_file ) as cursor:
            _SQL = """SELECT ID, PERSON_FIRST_NAME, PERSON_LAST_NAME, PERSON_SHORT_NAME  from PERSON  """
            _WHERE = "WHERE PERSON_SHORT_NAME = ? "
            cursor.execute( _SQL + _WHERE, (short_name,) ) 
            contents = cursor.fetchall() 
        print( contents ) 
        if contents:
            content = contents[ 0 ]
            return Person( content[ 0 ], content[ 1 ], content[ 2 ], content[ 3 ])
        else:
            return None

    def getStoreByStoreName( self, store_name : str ) -> Store:
        contents = [] 
        with SQLiteDriver( self.data_file ) as cursor:
            _SQL = """ SELECT ID, STORE_NAME, STORE_DETAIL, HOME_DELIVERY FROM STORE  """
            _WHERE = """ WHERE STORE_NAME = ? """
            cursor.execute(_SQL + _WHERE, (store_name, ) ) 
            contents = cursor.fetchall()
        if contents:
            content = contents[ 0 ]
            return Store( content[ 0 ], content[ 1 ], content[ 2 ], content[ 3 ])
        else:
            return None

    def getPaymentTypeByMode( self, payment_mode : str ) -> PaymentType:
        contents = [] 
        with SQLiteDriver( self.data_file ) as cursor:
            _SQL = """SELECT ID, PAYMENT_MODE, PAYMENT_MODE_DETAIL from PAYMENT_TYPE  """
            _WHERE = """ WHERE PAYMENT_MODE = ?  """ 
            cursor.execute( _SQL + _WHERE, (payment_mode, ) ) 
            contents = cursor.fetchall() 
        if contents:
            content = contents[ 0 ]
            return PaymentType( content[ 0 ], content[ 1 ], content[ 2 ])
        else:
            return None

    def getExpenseCategoryByExpenseType( self, expense_type : str ) -> ExpenseCategory:
        contents = [] 
        with SQLiteDriver( self.data_file ) as cursor:
            _SQL = """ SELECT ID, EXPENSE_TYPE, EXPENSE_TYPE_DETAIL FROM expense_category  """
            _WHERE = """ WHERE EXPENSE_TYPE = ? """
            cursor.execute(_SQL + _WHERE, ( expense_type, ))
            contents = cursor.fetchall()

        print( contents ) 
        if contents:
            content = contents[ 0 ]
            return ExpenseCategory( content[ 0 ], content[ 1 ], content[ 2 ]  )
        else:
            return None
