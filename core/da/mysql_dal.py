#######################################################################
# Module: SQLiteDataAccessLayer
# Purpose: This class has all the data access code specific to SQLite
#######################################################################

from core.expense_category import ExpenseCategory
from core.store import Store 
from core.expense import Expense
from core.person import Person 
from core.expense_category import ExpenseCategory
from core.payment_type import PaymentType
from core.da.dal import DataAccessLayer
from core.da.mysqldriver import MySQLDriver
from core.constants import _DATE_STR_DISPLAY_FORMAT_
from core.constants import _DATE_STR_STORAGE_FORMAT_


class MySQLDataAccessLayer( DataAccessLayer ):

    def __init__( self, dbconfig : dict ) :
        self.config =  dbconfig 


    # All expense methods     
    def addExpense( self, expense: Expense ) -> None:
        print( 'mysql_dat: add Expense' )
        expense_detail = expense.getExpenseDetail() 
        expense_date = expense.getExpenseDate().strftime( _DATE_STR_STORAGE_FORMAT_ )
        expense_amount = expense.getExpenseAmount() 
        person_id = expense.getPerson().getId() 
        store_id = expense.getStore().getId()
        expense_category_id = expense.getExpenseCategory().getId()
        payment_type_id = expense.getPaymentType().getId() 

        with MySQLDriver( self.config ) as cursor:
            _SQL = """INSERT INTO EXPENSE( EXPENSE_DETAIL, EXPENSE_DATE, EXPENSE_AMOUNT, EXPENSE_CATEGORY_ID, PAYMENT_TYPE_ID, PERSON_ID, STORE_ID ) VALUES( %s, %s, %s, %s, %s, %s, %s )"""
            cursor.execute(_SQL, (expense_detail, expense_date, expense_amount, expense_category_id, payment_type_id, person_id, store_id )) 

    def deleteExpense( self, id : str ) -> None :
        with MySQLDriver( self.config ) as cursor:
            _SQL = """DELETE FROM EXPENSE WHERE ID = %s """
            cursor.execute(_SQL, (id, ))

    def listExpenses( self ) -> list:
        contents = [] 
        with MySQLDriver( self.config ) as cursor:
            _SQL = """ SELECT ID, EXPENSE_DETAIL, EXPENSE_DATE, EXPENSE_AMOUNT, 
                        EXPENSE_CATEGORY_ID, PAYMENT_TYPE_ID, PERSON_ID, STORE_ID FROM EXPENSE """
            _ORDERBY = " ORDER BY EXPENSE.EXPENSE_DATE DESC "
            cursor.execute(_SQL + _ORDERBY)
            contents = cursor.fetchall()
        print( contents ) 
        return contents  

    # Expense category methods
    def addExpenseCategory( self, expense_category : ExpenseCategory ) -> None :
        expense_type : str = expense_category.getExpenseType() 
        expense_type_detail : str = expense_category.getExpenseDetail() 

        with MySQLDriver( self.config ) as cursor:
            _SQL = """INSERT INTO EXPENSE_CATEGORY(expense_type, expense_type_detail ) VALUES( %s, %s )"""
            cursor.execute(_SQL, (expense_type, expense_type_detail))
    
    def deleteExpenseCategory( self, id : str ) -> None :
        with MySQLDriver( self.config ) as cursor:
            _SQL = """DELETE FROM EXPENSE_CATEGORY WHERE ID = %s """
            cursor.execute(_SQL, (id, ))

    def listExpenseCategories( self ) -> list :
        contents = [] 
        with MySQLDriver( self.config ) as cursor:
            _SQL = """ SELECT ID, EXPENSE_TYPE, EXPENSE_TYPE_DETAIL FROM EXPENSE_CATEGORY  """
            _ORDERBY = """ ORDER BY expense_type """
            cursor.execute(_SQL + _ORDERBY)
            contents = cursor.fetchall()
        return contents 

    # Store(s) methods
    def addStore( self, store : Store ) -> None :
        store_name = store.getStoreName() 
        store_detail = store.getStoreDetail()
        home_delivery = store.getHomeDeliveryString() 

        with MySQLDriver( self.config ) as cursor:
            _SQL = """INSERT INTO STORE(STORE_NAME, STORE_DETAIL, HOME_DELIVERY ) VALUES( %s, %s, %s )"""
            cursor.execute(_SQL, (store_name, store_detail, home_delivery))

    def deleteStore( self, id : str ) -> None :
        with MySQLDriver( self.config ) as cursor:
            _SQL = """DELETE FROM STORE WHERE ID = %s """
            cursor.execute(_SQL, (id, ))

    def listStores( self ) -> list :
        contents = [] 
        with MySQLDriver( self.config ) as cursor:
            _SQL = """ SELECT ID, STORE_NAME, STORE_DETAIL, HOME_DELIVERY FROM STORE  """
            _ORDERBY = """ ORDER BY STORE_NAME """
            cursor.execute(_SQL + _ORDERBY)
            contents = cursor.fetchall()
        return contents 

    # Payment Type methods        
    def addPaymentType( self, payment_type : PaymentType ) -> None:
        payment_mode = payment_type.getPaymentMode() 
        payment_mode_detail = payment_type.getPaymentModeDetail()

        with MySQLDriver( self.config ) as cursor:
            _SQL = """ INSERT INTO PAYMENT_TYPE(PAYMENT_MODE, PAYMENT_MODE_DETAIL ) VALUES( %s, %s ) """
            cursor.execute(_SQL, (payment_mode, payment_mode_detail))

    def deletePaymentType( self, id : str ) -> None:
        with MySQLDriver( self.config ) as cursor:
            _SQL = """DELETE FROM PAYMENT_TYPE WHERE ID = %s """
            cursor.execute(_SQL, (id, ))
    
    def listPaymentTypes( self ) -> list:
        contents = [] 
        with MySQLDriver( self.config ) as cursor:
            _SQL = """SELECT ID, PAYMENT_MODE, PAYMENT_MODE_DETAIL from PAYMENT_TYPE  ORDER BY PAYMENT_MODE  """
            cursor.execute( _SQL ) 
            contents = cursor.fetchall() 
        return contents 

    # Person methods    
    def addPerson( self, person : Person ) -> None:
        person_first_name = person.getFirstName()
        person_last_name = person.getLastName()
        person_short_name = person.getShortName() 

        with MySQLDriver( self.config ) as cursor:
            _SQL = """INSERT INTO PERSON(PERSON_FIRST_NAME, PERSON_LAST_NAME, PERSON_SHORT_NAME ) VALUES( %s, %s, %s )"""
            cursor.execute(_SQL, (person_first_name, person_last_name, person_short_name))

    def deletePerson( self, id : str ) -> None :
        with MySQLDriver( self.config ) as cursor:
            _SQL = """DELETE FROM PERSON WHERE ID = %s """
            cursor.execute(_SQL, (id, ))

    def listPeople( self ) -> list:
        contents = [] 
        with MySQLDriver( self.config ) as cursor:
            _SQL = """SELECT ID, PERSON_FIRST_NAME, PERSON_LAST_NAME, PERSON_SHORT_NAME  from PERSON  """
            cursor.execute( _SQL ) 
            contents = cursor.fetchall() 
        return contents 

    # Other utility methods    
    def getPersonByShortName( self, short_name : str  ) -> Person:
        contents = [] 
        with MySQLDriver( self.config ) as cursor:
            _SQL = """SELECT ID, PERSON_FIRST_NAME, PERSON_LAST_NAME, PERSON_SHORT_NAME  from PERSON  """
            _WHERE = "WHERE PERSON_SHORT_NAME = %s "
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
        with MySQLDriver( self.config ) as cursor:
            _SQL = """ SELECT ID, STORE_NAME, STORE_DETAIL, HOME_DELIVERY FROM STORE  """
            _WHERE = """ WHERE STORE_NAME = %s """
            cursor.execute(_SQL + _WHERE, (store_name, ) ) 
            contents = cursor.fetchall()
        if contents:
            content = contents[ 0 ]
            return Store( content[ 0 ], content[ 1 ], content[ 2 ], content[ 3 ])
        else:
            return None

    def getPaymentTypeByMode( self, payment_mode : str ) -> PaymentType:
        contents = [] 
        with MySQLDriver( self.config ) as cursor:
            _SQL = """SELECT ID, PAYMENT_MODE, PAYMENT_MODE_DETAIL from PAYMENT_TYPE  """
            _WHERE = """ WHERE PAYMENT_MODE = %s  """ 
            cursor.execute( _SQL + _WHERE, (payment_mode, ) ) 
            contents = cursor.fetchall() 
        if contents:
            content = contents[ 0 ]
            return PaymentType( content[ 0 ], content[ 1 ], content[ 2 ])
        else:
            return None

    def getExpenseCategoryByExpenseType( self, expense_type : str ) -> ExpenseCategory:
        contents = [] 
        with MySQLDriver( self.config ) as cursor:
            _SQL = """ SELECT ID, EXPENSE_TYPE, EXPENSE_TYPE_DETAIL FROM expense_category  """
            _WHERE = """ WHERE EXPENSE_TYPE = %s """
            cursor.execute(_SQL + _WHERE, ( expense_type, ))
            contents = cursor.fetchall()

        print( contents ) 
        if contents:
            content = contents[ 0 ]
            return ExpenseCategory( content[ 0 ], content[ 1 ], content[ 2 ]  )
        else:
            return None
    
    # All reporting functions
    def getExpenseSummaryForMonth( self, search_string : str ) -> tuple:
        contents = [] 
        with MySQLDriver( self.config ) as cursor:
            _SQL = """ SELECT SUBSTR( EXPENSE_DATE, 1, 7 ) EDATE, COUNT( ID ), SUM(EXPENSE_AMOUNT) FROM EXPENSE GROUP BY SUBSTR( EXPENSE_DATE, 1, 7 ) """ 
            _WHERE = """ HAVING EDATE = %s  """
            cursor.execute( _SQL + _WHERE, ( search_string, ) )
            contents = cursor.fetchall() 
        if contents:
            content = contents[ 0 ] 
            return ( content[ 0 ], content[ 1 ], content[ 2 ] )
        else:
            return None

    def getMonthwiseExpenseSummary( self ) -> list:
        contents = [] 
        with MySQLDriver( self.config ) as cursor:
            _SQL = """ SELECT SUBSTR( EXPENSE_DATE, 1, 7 ) AS EDATE, COUNT( ID ), SUM(EXPENSE_AMOUNT) FROM EXPENSE GROUP BY EDATE  ORDER BY EDATE DESC """ 
            cursor.execute( _SQL )
            contents = cursor.fetchall() 
        if contents:
            return contents 
        else:
            return None

    def getMonthwiseCategoryExpense( self ) -> list:
        contents = [] 
        with MySQLDriver( self.config ) as cursor:
            _SQL = """ SELECT SUBSTR( EXPENSE_DATE, 1, 7) AS EDATE,  EXPENSE_CATEGORY.EXPENSE_TYPE,  COUNT( EXPENSE.ID), SUM( EXPENSE_AMOUNT ) from EXPENSE, EXPENSE_CATEGORY WHERE EXPENSE.EXPENSE_CATEGORY_ID = EXPENSE_CATEGORY.ID GROUP BY EDATE, EXPENSE_CATEGORY.EXPENSE_TYPE ORDER BY EDATE DESC,  EXPENSE_CATEGORY.EXPENSE_TYPE  """ 
            cursor.execute( _SQL  )
            contents = cursor.fetchall() 
        if contents:
            return contents 
        else:
            return None

    def getMonthwisePaymentTypeSummary( self ) -> list:
        contents = [] 
        with MySQLDriver( self.config ) as cursor:
            _SQL = """ SELECT SUBSTR( EXPENSE_DATE, 1, 7) AS EDATE,  PAYMENT_TYPE.PAYMENT_MODE,  COUNT( EXPENSE.ID), SUM( EXPENSE_AMOUNT ) from EXPENSE, PAYMENT_TYPE WHERE EXPENSE.PAYMENT_TYPE_ID = PAYMENT_TYPE.ID GROUP BY EDATE, PAYMENT_TYPE.PAYMENT_MODE ORDER BY EDATE DESC,  PAYMENT_TYPE.PAYMENT_MODE  """ 
            cursor.execute( _SQL )
            contents = cursor.fetchall() 
        if contents:
            return contents 
        else:
            return None

    def getMonthwisePersonSummary( self ) -> list:
        contents = [] 
        with MySQLDriver( self.config ) as cursor:
            _SQL = """ SELECT SUBSTR( EXPENSE_DATE, 1, 7) AS EDATE,  PERSON.PERSON_SHORT_NAME,  COUNT( EXPENSE.ID), SUM( EXPENSE_AMOUNT ) from EXPENSE, PERSON WHERE EXPENSE.PERSON_ID = PERSON.ID GROUP BY EDATE, PERSON.PERSON_SHORT_NAME ORDER BY EDATE DESC,  PERSON.PERSON_SHORT_NAME  """ 
            cursor.execute( _SQL )
            contents = cursor.fetchall() 
        if contents:
            return contents 
        else:
            return None
