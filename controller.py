import flask 
import sys

from factory import XManFactory
from core.expense_category import ExpenseCategory 

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

@app.route( '/', methods = [ 'GET'] )
def index_page() -> str:
    return flask.render_template( 'index.html', the_title=__appname__ )


@app.route( '/expense_input', methods = [ 'GET' ] )
def expense_input() -> str :
    ## TODO: add code here to get all required attributes

    ## TODO: add code here to navigate to expense_input page
    return index_page() 


@app.route( '/expense_category_input', methods = [ 'GET' ] )
def expense_category_input() -> str :
    return flask.render_template( 'expense_category_input.html', the_title=__appname__ ) 


@app.route( '/store_input', methods = [ 'GET' ] )
def store_input() -> str :
    ## TODO: add code here to get all required attributes

    ## TODO: add code here to navigate to store_input page
    return index_page() 



#######################################
## This section contains all the code
## related to just backend operations
## and then subsequent navigations
#######################################

@app.route( '/expense_category_add', methods=['POST'] )
def add_expense_category() -> str :
    print( 'add_expense_category')

    # Converting form values into business object (ExpenseCategory)
    expense_type : str = flask.request.form[ 'expense_type' ]
    expense_detail : str = flask.request.form[ 'expense_type_detail' ]
    expense_category : ExpenseCategory = ExpenseCategory( expense_type, expense_detail )  

    factory_object.getBusinessLayer().addExpenseCategory( expense_category ) 
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
    print( 'add_store') 
    # TODO: Store add-to-DB code to be added here and then navigate to saved page
    return index_page()  

@app.route( '/stores_list', methods = [ 'GET'] )
def list_stores() -> str :
    print( 'list_stores')
    # TODO: get the stores from DB and navigate to data list view
    return index_page() 

@app.route( '/expense_add', methods=['POST'] )
def add_expense() -> str :
    print( 'add_expense') 
    # TODO: Expense add-to-DB code to be added here and then navigate to saved page
    return index_page() 

@app.route( '/expenses_list', methods = [ 'GET'] )
def list_expenses() -> str :
    print( 'list_expenses' )
    # TODO: get the expenses from DB and navigate to data list view
    return index_page() 

# Main code 
if len( sys.argv ) == 2:
    factory_object = XManFactory() 
    factory_object.createObjects( sys.argv[ 1 ] )
    app.run(debug=True) 
else:
    print( 'Invalid usage python3 controller.py <DB-String>' )
