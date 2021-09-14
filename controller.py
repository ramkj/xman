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
import traceback
from flask import send_file 

from core.constants import _DATE_STR_DISPLAY_FORMAT_

from factory import XManFactory 
from core.timer import Timer 

# all app level variables
__version__=1.0
__author__='Ramakrishnan Jayachandran'
__appname__='XMAN (eXpense MANager) v1.0'


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
    with Timer( 'index_page') as stime:  
        summary = getExpenseSummary() 

    return flask.render_template( 'index.html', the_title=__appname__, summary=summary )

# redirection to input screen for expense - and build neccessary objects for it
@app.route( '/expense_input', methods = [ 'GET' ] )
def expense_input() -> str :

    with Timer( 'expense_input' ) as start_time:
        summary = getExpenseSummary() 

        # constants for accessing tuple with some readability 
        _EXPENSE_TYPES_ : int = 0 
        _PEOPLE_ : int = 1 
        _STORES_ : int = 2 
        _PAYMENT_MODE_ : int = 3

        ui_objects : tuple = factory_object.getBusinessLayer().prepareExpenseInput()

    ## TODO: add code here to navigate to expense_input page
    return flask.render_template( 'expense_input.html', the_title=__appname__ , summary=summary, \
        short_names=ui_objects[ _PEOPLE_ ], store_names=ui_objects[ _STORES_ ], \
        payment_types=ui_objects[ _PAYMENT_MODE_], expense_types=ui_objects[ _EXPENSE_TYPES_ ] )

# expense category redirection to the input screen
@app.route( '/expense_category_input', methods = [ 'GET' ] )
def expense_category_input() -> str :
    summary = getExpenseSummary() 
    return flask.render_template( 'expense_category_input.html', the_title=__appname__, summary=summary ) 

@app.route( '/store_input', methods = [ 'GET' ] )
def store_input() -> str :
    summary = getExpenseSummary() 
    return flask.render_template( 'store_input.html', the_title=__appname__, summary=summary )

@app.route( '/payment_type_input', methods = [ 'GET' ] )
def payment_type_input() -> str :
    summary = getExpenseSummary() 
    return flask.render_template( 'payment_type_input.html', the_title=__appname__, summary=summary )

@app.route( '/person_input', methods = [ 'GET' ] )
def person_input() -> str :
    summary = getExpenseSummary() 
    return flask.render_template( 'person_input.html', the_title=__appname__, summary=summary )

#######################################
## This section contains all the code
## related to just backend operations
## and then subsequent navigations
#######################################

# All Add flows go here ... 
@app.route( '/expense_add', methods=['POST'] )
def add_expense() -> str :
    summary = getExpenseSummary() 

    try:
        factory_object.getBusinessLayer().addExpense( flask.request.form[ 'exp_type' ], flask.request.form[ 'exp_detail' ], datetime.datetime.strptime( flask.request.form[ 'exp_date' ], '%Y-%m-%d' ) , float( flask.request.form[ 'exp_amount' ]), flask.request.form[ 'payment_type' ], flask.request.form[ 'store_name' ], flask.request.form[ 'short_name' ])
    except:
        traceback.print_exc()
        return flask.render_template( 'error_page.html', \
                error_cause='Failed adding expense information', \
                error_action = 'Please reenter the expense data and try again',\
                summary=summary )
    else:
        return flask.render_template('data_saved.html', the_title= __appname__, summary=summary )  

@app.route( '/expense_category_add', methods=['POST'] )
def add_expense_category() -> str :
    print( 'add_expense_category')
    summary = getExpenseSummary() 

    expense_type : str = flask.request.form[ 'expense_type' ]
    expense_detail : str = flask.request.form[ 'expense_type_detail' ]
    try:

        factory_object.getBusinessLayer().addExpenseCategory( expense_type, expense_detail ) 
    except:
        traceback.print_exc()
        return flask.render_template( 'error_page.html', \
                error_cause='Failed adding expense category', \
                error_action = 'Please reenter the Expense category - make sure it is not a duplicate', summary=summary )
    else:
        return flask.render_template('data_saved.html', the_title= __appname__, summary=summary )  

@app.route( '/store_add', methods=['POST'] )
def add_store() -> str :
    summary = getExpenseSummary() 

    try:
        factory_object.getBusinessLayer().addStore( flask.request.form[ 'store_name' ], flask.request.form[ 'store_detail' ], flask.request.form[ 'home_delivery' ] )
    except:
        traceback.print_exc()
        return flask.render_template( 'error_page.html', \
                error_cause='Failed adding store data', \
                error_action = 'Please reenter the Store data and make sure it is not a duplicate',\
                summary=summary )
    else:
        return flask.render_template('data_saved.html', the_title= __appname__, summary=summary )  

@app.route( '/payment_type_add', methods=['POST'] )
def add_payment_type() -> str :
    summary = getExpenseSummary() 

    try:
        factory_object.getBusinessLayer().addPaymentType( flask.request.form[ 'payment_mode' ], flask.request.form[ 'payment_mode_detail' ] )
    except:
        traceback.print_exc()
        return flask.render_template( 'error_page.html', \
                error_cause='Failed adding payment type data', \
                error_action = 'Please reenter the payment type data and make sure it is not a duplicate',\
                summary=summary )
    else:
        return flask.render_template('data_saved.html', the_title= __appname__, summary=summary )  

@app.route( '/person_add', methods=['POST'] )
def add_person() -> str :
    summary = getExpenseSummary() 

    try:
        factory_object.getBusinessLayer().addPerson( flask.request.form[ 'person_first_name' ], flask.request.form[ 'person_last_name' ], flask.request.form[ 'person_short_name' ] )
    except:
        traceback.print_exc()
        return flask.render_template( 'error_page.html', \
                error_cause='Failed adding person data', \
                error_action = 'Please reenter the person data and make sure short name it is not a duplicate',\
                summary=summary )
    else:
        return flask.render_template('data_saved.html', the_title= __appname__, summary=summary )  

# All list flows go here ... 
@app.route( '/expenses_list', methods = [ 'GET'] )
def list_expenses() -> str :
    print( 'list_expenses' )
    summary = getExpenseSummary() 

    expenses : list = factory_object.getBusinessLayer().listExpenses() 
    ui_header = [ 'ID', 'Expense Detail', 'Expense Date', 'Amount', 'Spent by', 'Store', 'Expense Type', 'Payment mode' ] 
    ui_data : list = [ (e.getId(), e.getExpenseDetail(), e.getExpenseDate().strftime( _DATE_STR_DISPLAY_FORMAT_ ) , e.getExpenseAmount(), \
                        e.getPerson().getShortName(), e.getStore().getStoreName(), \
                        e.getExpenseCategory().getExpenseType(), e.getPaymentType().getPaymentMode()) for e in expenses ]

    # Generate the csv file for future use
    csv_rows = [] 
    csv_rows.append( ui_header )
    for row in ui_data:
        csv_rows.append( [ c for c in row ])

    factory_object.getCSVGenerator().generateFile( 'all_expenses.csv', csv_rows )

    return flask.render_template( 'list_data_page.html', the_title=__appname__, \
                summary=summary, the_header = ui_header, the_data = ui_data, module='expense', download=True ) 

@app.route( '/expense_categories_list', methods = [ 'GET']  )
def list_expense_categories() -> str :
    print( 'list_expense_categories' )
    summary = getExpenseSummary() 

    expense_categories : list = factory_object.getBusinessLayer().listExpenseCategories()  

    ui_header = ( 'Id', 'Expense Type', 'Expense Detail' )
    ui_data : list = [ ( ec.getId(), ec.getExpenseType(), ec.getExpenseDetail()) for ec in expense_categories ]
    mode = flask.request.args.get( 'mode' )

    if mode == 'popup':
        return flask.render_template( 'list_data_popup.html', the_title=__appname__, \
                the_header = ui_header, summary=summary, the_data = ui_data, module = None ) 
    else:
        return flask.render_template( 'list_data_page.html', the_title=__appname__, summary=summary, \
                the_header = ui_header, the_data = ui_data, module = 'expense_category' ) 

@app.route( '/stores_list', methods = [ 'GET'] )
def list_stores() -> str :
    summary = getExpenseSummary() 

    stores : list = factory_object.getBusinessLayer().listStores()     
    ui_header = ('ID', 'Store Name', 'Store Detail', 'Home Delivery ?' )
    ui_data : list = [ (st.getId(), st.getStoreName(), st.getStoreDetail(), ('Y' if st.getHomeDelivery() else 'N') ) for st in stores ] 
    mode = flask.request.args.get( 'mode' )

    if mode == 'popup':
        return flask.render_template( 'list_data_popup.html', the_title=__appname__, \
        summary=summary, the_header = ui_header, the_data = ui_data, module=None) 
    else:
        return flask.render_template( 'list_data_page.html', the_title=__appname__, \
        summary=summary, the_header = ui_header, the_data = ui_data, module='store'  ) 

@app.route( '/payment_type_list', methods = [ 'GET'] )
def list_payment_types() -> str :
    summary = getExpenseSummary() 

    payment_modes : list = factory_object.getBusinessLayer().listPaymentTypes()
    ui_header = ('ID', 'Payment Mode', 'Payment Mode Detail' )
    ui_data : list = [ (p.getId(), p.getPaymentMode(), p.getPaymentModeDetail() ) for p in payment_modes ] 
    mode = flask.request.args.get( 'mode' )

    if mode == 'popup':
        return flask.render_template( 'list_data_popup.html', the_title=__appname__, \
        summary=summary, the_header = ui_header, the_data = ui_data, module=None) 
    else:
        return flask.render_template( 'list_data_page.html', the_title=__appname__, \
        summary=summary, the_header = ui_header, the_data = ui_data, module='payment_type'  ) 

@app.route( '/person_list', methods = [ 'GET'] )
def list_person() -> str :
    summary = getExpenseSummary() 

    people : list = factory_object.getBusinessLayer().listPeople()
    ui_header = ('ID', 'First Name', 'Last Name', 'Short Name' )
    ui_data : list = [ (p.getId(), p.getFirstName(), p.getLastName(), p.getShortName() ) for p in people ] 
    mode = flask.request.args.get( 'mode' )

    if mode == 'popup':
        return flask.render_template( 'list_data_popup.html', the_title=__appname__, \
        summary=summary, the_header = ui_header, the_data = ui_data, module=None) 
    else:
        return flask.render_template( 'list_data_page.html', the_title=__appname__, \
        summary=summary, the_header = ui_header, the_data = ui_data, module='person'  ) 

# All delete flows go here ...
@app.route( '/expense_delete', methods = [ 'GET' ] )
def delete_expense() -> str :
    print( 'delete_expense')
    summary = getExpenseSummary() 

    Id = flask.request.args.get( 'Id' )
    try:
        factory_object.getBusinessLayer().deleteExpense( Id )
    except:
        traceback.print_exc()
        return flask.render_template( 'error_page.html', \
                error_cause='Failed deleting expense', \
                error_action = 'Please retry or check the log for details',\
                summary=summary )
    else:
        return flask.render_template('data_saved.html', the_title= __appname__, summary=summary )  

@app.route( '/expense_category_delete', methods = [ 'GET' ] )
def delete_expense_category() -> str :
    print( 'delete_expense_category')
    summary = getExpenseSummary() 

    Id = flask.request.args.get( 'Id' )
    try:
        factory_object.getBusinessLayer().deleteExpenseCategory( Id )
    except:
        traceback.print_exc()
        return flask.render_template( 'error_page.html', \
                error_cause='Failed deleting expense category', \
                error_action = 'Please retry or check the log for details',\
                summary=summary )
    else:
        return flask.render_template('data_saved.html', the_title= __appname__, summary=summary )  

@app.route( '/store_delete', methods=['GET'] )
def delete_store() -> str:
    summary = getExpenseSummary() 
    Id = flask.request.args.get( 'Id' )
    try:
        factory_object.getBusinessLayer().deleteStore( Id )
    except:
        traceback.print_exc()
        return flask.render_template( 'error_page.html', \
                error_cause='Failed deleting store data', \
                error_action = 'Please retry or check the log for details',\
                summary=summary )
    else:
        return flask.render_template('data_saved.html', the_title= __appname__, summary=summary )  

@app.route( '/payment_type_delete', methods=['GET'] )
def delete_payment_type() -> str:
    summary = getExpenseSummary() 
    Id = flask.request.args.get( 'Id' )
    try:
        factory_object.getBusinessLayer().deletePaymentType( Id )
    except:
        traceback.print_exc()
        return flask.render_template( 'error_page.html', \
                error_cause='Failed deleting payment type data', \
                error_action = 'Please retry or check the log for details',\
                summary=summary )
    else:
        return flask.render_template('data_saved.html', the_title= __appname__, summary=summary )  

@app.route( '/person_delete', methods=['GET'] )
def delete_person() -> str:
    summary = getExpenseSummary() 
    Id = flask.request.args.get( 'Id' )
    try:
        factory_object.getBusinessLayer().deletePerson( Id )
    except:
        traceback.print_exc()
        return flask.render_template( 'error_page.html', \
                error_cause='Failed deleting person data', \
                error_action = 'Please retry or check the log for details',\
                summary=summary )
    else:
        return flask.render_template('data_saved.html', the_title= __appname__, summary=summary )  

# All report flows go here ...
@app.route( '/expense_month_summary_list', methods = [ 'GET' ] )
def list_expenses_monthly_summary() -> str:
    summary = getExpenseSummary() 
    report = factory_object.getReportingLayer().listMonthwiseSummary() 
    return flask.render_template( 'list_data_page.html', the_title=__appname__, \
                summary=summary, the_header = report[ 0 ], the_data = report[ 1 ], module=None ) 

@app.route( '/expense_month_category_summary_list', methods = [ 'GET' ] )
def list_expenses_monthly_category_summary() -> str:
    summary = getExpenseSummary() 
    report = factory_object.getReportingLayer().listMonthwiseCategorySummary() 
    return flask.render_template( 'list_data_page.html', the_title=__appname__, \
                summary=summary, the_header = report[ 0 ], the_data = report[ 1 ], module=None ) 

@app.route( '/expense_month_person_summary_list', methods = [ 'GET' ] )
def list_expenses_monthly_person_summary() -> str:
    summary = getExpenseSummary() 
    report = factory_object.getReportingLayer().listMonthwisePersonSummary() 
    return flask.render_template( 'list_data_page.html', the_title=__appname__, \
                summary=summary, the_header = report[ 0 ], the_data = report[ 1 ], module=None ) 

@app.route( '/expense_month_paytype_summary_list', methods = [ 'GET' ] )
def list_expenses_monthly_paytype_summary() -> str:
    summary = getExpenseSummary() 
    report = factory_object.getReportingLayer().listMonthwisePaymentTypeSummary() 
    return flask.render_template( 'list_data_page.html', the_title=__appname__, \
                summary=summary, the_header = report[ 0 ], the_data = report[ 1 ], module=None ) 

# download links
@app.route( '/download_expenses', methods = [ 'GET' ] )
def download_expense_list() -> str:
    return send_file( factory_object.getCSVGenerator().getFilenameWithPath( 'all_expenses.csv'), mimetype='text/csv' )

# other utility methods go here ...
def getExpenseSummary():
    current_month_string = datetime.datetime.now().strftime( '%Y/%m' )
    result = factory_object.getBusinessLayer().getExpenseSummary(current_month_string ) 
    return result

# Main code ...
if len( sys.argv ) == 2:
    factory_object = XManFactory() 
    factory_object.createObjects( sys.argv[ 1 ] )
    app.run(debug=True) 
else:
    print( 'Invalid usage python3 controller.py <DB-String>' )
