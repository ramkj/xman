# core business logic is initiated from this class


from core.da.dal import DataAccessLayer
from core.expense_category import ExpenseCategory
from core.store import Store 
from core.person import Person
from core.payment_type import PaymentType
from core.expense import Expense 

import datetime

class BusinessLayer:

    def __init__( self ):
        pass 

    def setDALayer( self, dal : DataAccessLayer ) -> None:
        self.dal = dal 
    
        
    def addExpenseCategory( self, expense_type : str, expense_detail : str ) -> None:
        expense_category : ExpenseCategory = ExpenseCategory( -1, expense_type, expense_detail )  
        self.dal.addExpenseCategory( expense_category ) 

    def listExpenseCategories( self ) -> list:
        return [ ExpenseCategory( row[ 0 ], row[ 1 ], row[ 2 ] ) for row in self.dal.listExpenseCategories() ] 

    def addStore( self, store_name : str, store_detail : str, home_delivery : str ) -> None:
        home_delivery_bool = home_delivery == 'true' 
        self.dal.addStore( Store( -1, store_name, store_detail, home_delivery_bool ) )

    def listStores( self ) -> list:
        return [ Store( row[ 0 ], row[ 1 ], row[ 2 ], row[ 3 ]) for row in self.dal.listStores() ] 

    def addExpense( self, exp_type : str , exp_detail: str , exp_date : datetime.datetime, exp_amount : float, payment_mode : str, store_name : str, short_name : str) -> None:
        person : Person = self.getPersonByShortName( short_name ) 
        store : Store = self.getStoreByStoreName( store_name ) 
        payment_type : PaymentType = self.getPaymentTypeByMode( payment_mode)
        expense_category : ExpenseCategory = self.getExpenseCategoryByExpenseType( exp_type ) 
        expense : Expense = Expense( -1, exp_detail, exp_date, exp_amount, person, store, expense_category, payment_type )     
        self.dal.addExpense( expense ) 
    
    def listExpenses( self ) -> list:
        data_list : list = self.dal.listExpenses()

        paymentTypeMap : dict = self.getPaymentTypeMapById() 
        storeMap : dict = self.getStoreMapById()
        personMap : dict = self.getPersonMapById() 
        expenseCategoryMap : dict = self.getExpenseCategoryMapById() 

        expense_data = [] 
        for data in data_list:
            expense_id = data[ 0 ]
            expense_detail = data[ 1 ] 
            expense_date = data[ 2 ]
            expense_amount = data[ 3 ] 
            expense_type = expenseCategoryMap[ data[ 4 ] ]
            payment_mode = paymentTypeMap[ data[ 5 ] ]
            person = personMap[ data[ 6 ] ]
            store  = storeMap[ data[ 7 ] ]

            e : Expense = Expense( expense_id, expense_detail, expense_date, \
                        expense_amount, person, store, expense_type, payment_mode ) 
            expense_data.append( e )
        
        return expense_data 

    def listPeople( self ) -> list:
        return [ Person( row[ 0 ], row[ 1 ], row[ 2 ], row[ 3 ] ) for row in self.dal.listPeople() ]  

    def listPaymentTypes( self ) -> list:
        return [ PaymentType( row[ 0 ], row[ 1 ], row[ 1 ] ) for row in self.dal.listPaymentTypes()]
    
    def getPersonByShortName( self, short_name : str ) -> Person:
        return self.dal.getPersonByShortName( short_name )

    def getStoreByStoreName( self, store_name : str ) -> Store:
        return self.dal.getStoreByStoreName( store_name ) 

    def getPaymentTypeByMode( self, payment_mode : str ) -> PaymentType:
        return self.dal.getPaymentTypeByMode( payment_mode ) 
    
    def getExpenseCategoryByExpenseType( self, expense_type : str ) -> ExpenseCategory:
        return self.dal.getExpenseCategoryByExpenseType( expense_type )

    #preparation for expense input screen - returns a tuple with all values for UI
    def prepareExpenseInput( self ) -> tuple:

        # prepare expense types
        expense_categories : list = self.listExpenseCategories()  
        ui_expense_types : list = [ ec.getExpenseType() for ec in expense_categories ]

        # prepare list of people
        people : list = self.listPeople()
        ui_people = [ person.getShortName() for person in people ]

        # prepare list of stores 
        stores : list = self.listStores() 
        ui_stores = [ store.getStoreName() for store in stores ] 

        # prepare list of payment types
        payment_types : list = self.listPaymentTypes() 
        ui_payment_types = [ pt.getPaymentMode() for pt in payment_types ]

        return ( ui_expense_types, ui_people, ui_stores, ui_payment_types ) 

    def getStoreMapById( self ) -> dict:
        stores : list = self.listStores() 
        store_map : dict = {} 
        for s in stores:
            store_map[ s.getId() ] = s 
        return store_map 
    
    def getPaymentTypeMapById( self ) -> dict:
        payment_modes : list = self.listPaymentTypes() 
        payment_mode_map : dict = {} 
        for p in payment_modes:
            payment_mode_map[ p.getId() ] = p 
        return payment_mode_map 

    def getPersonMapById( self ) -> dict:
        people : list = self.listPeople() 
        people_map : dict = {} 
        for p in people:
            people_map[ p.getId() ] = p
        return people_map 
    
    def getExpenseCategoryMapById( self ) -> dict:
        expense_categories : list = self.listExpenseCategories() 
        ec_map : dict = {} 
        for ec in expense_categories:
            ec_map[ ec.getId() ] = ec
        return ec_map 
