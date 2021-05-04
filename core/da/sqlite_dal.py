
from core.expense_category import ExpenseCategory
from core.da.dal import DataAccessLayer
from core.da.sqlitedriver import SQLiteDriver

class SQLiteDataAccessLayer( DataAccessLayer ):

    def __init__( self ) :
        # TODO: The following line should not be hard coded and should come from param
        self.data_file = './db/expenses.db'
    
    def addExpenseCategory( self, expense_category : ExpenseCategory ) -> None :
        print( 'addExpenseCategories')
        expense_type : str = expense_category.getExpenseType() 
        expense_type_detail : str = expense_category.getExpenseDetail() 

        with SQLiteDriver( self.data_file ) as cursor:
            _SQL = """INSERT INTO EXPENSE_CATEGORY(expense_type, expense_type_detail ) VALUES( ?, ? )"""
            cursor.execute(_SQL, (expense_type, expense_type_detail))
    
    def listExpenseCategories( self ) -> list :
        print( 'list expense categories' ) 
        contents = [] 
        with SQLiteDriver( self.data_file ) as cursor:
            _SQL = """ SELECT ID, expense_type, expense_type_detail FROM expense_category  """
            _ORDERBY = """ ORDER BY expense_type """
            cursor.execute( _SQL + _ORDERBY ) 
            contents = cursor.fetchall()
        print( contents ) 
        return contents 
