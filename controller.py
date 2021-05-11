###################################################################### 
# controller - deals with the UI concerns
# 1. navigation
# 2. preparing data elements in ui way for the screens
# 
# It will not be referring to the business domain objects 
# - it will use the bl component to deal with the business logic
######################################################################

import flask 
import sys
import datetime 

from factory import XManFactory 

# all app level variables
__version__=0.1
__author__='Ramakrishnan Jayachandran'
__appname__='XMAN (eXpense MANager) v0.2'

# Flask initialisation
app = flask.Flask( __name__ )


#######################################
## This section contains all the code
## related to just navigation to other
## pages in the system
#######################################

# This is the index page or the home page for the App
@app.route( '/', methods = [ 'GET'] )
def index_page() -> str:
    return flask.render_template( 'index.html', the_title=__appname__ )

# redirection to input screen for expense - and build neccessary objects for it
@app.route( '/expense_input', methods = [ 'GET' ] )
def expense_input() -> str :

    # constants for accessing tuple with some readability 
    _EXPENSE_TYPES_ : int = 0 
    _PEOPLE_ : int = 1 
    _STORES_ : int = 2 
    _PAYMENT_MODE_ : int = 3

    ui_objects : tuple = factory_object.getBusinessLayer().prepareExpenseInput()

    ## TODO: add code here to navigate to expense_input page
    return flask.render_template( 'expense_input.html', the_title=__appname__ , short_names=ui_objects[ _PEOPLE_ ], store_names=ui_objects[ _STORES_ ], payment_types=ui_objects[ _PAYMENT_MODE_], expense_types=ui_objects[ _EXPENSE_TYPES_ ] )

# expense category redirection to the input screen
@app.route( '/expense_category_input', methods = [ 'GET' ] )
def expense_category_input() -> str :
    return flask.render_template( 'expense_category_input.html', the_title=__appname__ ) 


@app.route( '/store_input', methods = [ 'GET' ] )
def store_input() -> str :
    return flask.render_template( 'store_input.html', the_title=__appname__ )


#######################################
## This section contains all the code
## related to just backend operations
## and then subsequent navigations
#######################################

@app.route( '/expense_category_add', methods=['POST'] )
def add_expense_category() -> str :
    print( 'add_expense_category')

    expense_type : str = flask.request.form[ 'expense_type' ]
    expense_detail : str = flask.request.form[ 'expense_type_detail' ]
    factory_object.getBusinessLayer().addExpenseCategory( expense_type, expense_detail ) 
    return flask.render_template('data_saved.html', the_title= __appname__ )  

@app.route( '/expense_categories_list', methods = [ 'GET']  )
def list_expense_categories() -> str :
    print( 'list_expense_categories' )
    expense_categories : list = factory_object.getBusinessLayer().listExpenseCategories()  

    ui_header = ( 'Expense Type', 'Expense Detail' )
    ui_data : list = [ ( ec.getExpenseType(), ec.getExpenseDetail()) for ec in expense_categories ]
    mode = flask.request.args.get( 'mode' )

    if mode == 'popup':
        return flask.render_template( 'list_data_popup.html', the_title=__appname__, the_header = ui_header, the_data = ui_data ) 
    else:
        return flask.render_template( 'list_data_page.html', the_title=__appname__, the_header = ui_header, the_data = ui_data ) 

@app.route( '/store_add', methods=['POST'] )
def add_store() -> str :
    factory_object.getBusinessLayer().addStore( flask.request.form[ 'store_name' ], flask.request.form[ 'store_detail' ], flask.request.form[ 'home_delivery' ] )
    return flask.render_template('data_saved.html', the_title= __appname__ )  

@app.route( '/stores_list', methods = [ 'GET'] )
def list_stores() -> str :
    stores : list = factory_object.getBusinessLayer().listStores()     
    ui_header = ( 'Store Name', 'Store Detail', 'Home Delivery ?' )
    ui_data : list = [ (st.getStoreName(), st.getStoreDetail(), ('Y' if st.getHomeDelivery() else 'N') ) for st in stores ] 
    mode = flask.request.args.get( 'mode' )

    if mode == 'popup':
        return flask.render_template( 'list_data_popup.html', the_title=__appname__, the_header = ui_header, the_data = ui_data ) 
    else:
        return flask.render_template( 'list_data_page.html', the_title=__appname__, the_header = ui_header, the_data = ui_data ) 

@app.route( '/expense_add', methods=['POST'] )
def add_expense() -> str :
    factory_object.getBusinessLayer().addExpense( flask.request.form[ 'exp_type' ], flask.request.form[ 'exp_detail' ], datetime.datetime.strptime( flask.request.form[ 'exp_date' ], '%Y-%m-%d' ) , float( flask.request.form[ 'exp_amount' ]), flask.request.form[ 'payment_type' ], flask.request.form[ 'store_name' ], flask.request.form[ 'short_name' ])
    return flask.render_template('data_saved.html', the_title= __appname__ )  


@app.route( '/expenses_list', methods = [ 'GET'] )
def list_expenses() -> str :
    print( 'list_expenses' )
    expenses : list = factory_object.getBusinessLayer().listExpenses() 
    ui_header = [ 'ID', 'Expense Detail', 'Expense Date', 'Amount', 'Spent by', 'Store', 'Expense Type', 'Payment mode' ] 
    ui_data : list = [ (e.getId(), e.getExpenseDetail(), datetime.datetime.fromtimestamp( e.getExpenseDate()).strftime( '%d-%b-%Y'), e.getExpenseAmount(), \
                        e.getPerson().getShortName(), e.getStore().getStoreName(), \
                        e.getExpenseCategory().getExpenseType(), e.getPaymentType().getPaymentMode()) for e in expenses ]

    return flask.render_template( 'list_data_page.html', the_title=__appname__, the_header = ui_header, the_data = ui_data ) 

# Main code 
if len( sys.argv ) == 2:
    factory_object = XManFactory() 
    factory_object.createObjects( sys.argv[ 1 ] )
    app.run(debug=True) 
else:
    print( 'Invalid usage python3 controller.py <DB-String>' )
