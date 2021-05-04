import sqlite3 


DB_FILE = '../db/expenses.db'

CREATE_PAYMENT_TYPE = """   CREATE TABLE IF NOT EXISTS PAYMENT_TYPE (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                PAYMENT_MODE CHAR( 20 ) NOT NULL,
                                PAYMENT_MODE_DETAIL CHAR( 80 )
                        )"""

CREATE_EXPENSE_CATEGORY = """CREATE TABLE IF NOT EXISTS EXPENSE_CATEGORY (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                EXPENSE_TYPE CHAR( 40 ),
                                EXPENSE_TYPE_DETAIL CHAR( 80 )
                            ) """

CREATE_PERSON = """CREATE TABLE IF NOT EXISTS PERSON (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    PERSON_FIRST_NAME CHAR( 100 ) NOT NULL,
                    PERSON_LAST_NAME CHAR( 100 ) NOT NULL,
                    PERSON_SHORT_NAME CHAR( 50 ) NOT NULL
                )"""

CREATE_STORE = """CREATE TABLE IF NOT EXISTS STORE (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        STORE_NAME CHAR( 40 ) NOT NULL,
                        STORE_DETAIL CHAR( 100 ),
                        HOME_DELIVERY CHAR( 1 )
                )""" 

CREATE_EXPENSE = """CREATE TABLE IF NOT EXISTS EXPENSE (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        EXPENSE_DETAIL CHAR(60),
                        EXPENSE_CATEGORY_ID INTEGER REFERENCES EXPENSE_CATEGORY( ID ),
                        EXPENSE_DATE INTEGER ,
                        EXPENSE_AMOUNT REAL,
                        PAYMENT_TYPE_ID INTEGER NOT NULL, 
                        PERSON_ID INTEGER NOT NULL,
                        STORE_ID INTEGER REFERENCES STORE( ID ) NOT NULL, 
                        FOREIGN KEY (PAYMENT_TYPE_ID) REFERENCES PAYMENT_TYPE( ID ),
                        FOREIGN KEY (PERSON_ID) REFERENCES PERSON( ID ),
                        FOREIGN KEY (STORE_ID) REFERENCES STORE( ID )
                    )"""

CREATE_LOGIN = """CREATE TABLE IF NOT EXISTS LOGIN (
                    LOGIN_ID        CHAR( 75 ) NOT NULL,
                    PASSWORD_HASH   CHAR( 256 ) NOT NULL,
                    ACTIVE          CHAR( 1 )
                )"""


# All insert statements 
def insert_seed_data( connection ): 

    print( 'started seed data insertion ...')
    cursor = connection.cursor() 
    cursor.execute(  """INSERT INTO STORE ( store_name, store_detail, home_delivery) VALUES( 'Lumiere', 'Lumiere Organic store, HSR', 'Y' ) """ ) 
    cursor.execute( """INSERT INTO STORE ( store_name, store_detail, home_delivery) VALUES( 'Eco Store', 'Eco Store - Organic, HSR', 'Y' ) """ ) 
    cursor.execute( """INSERT INTO STORE ( store_name, store_detail, home_delivery) VALUES( 'Organic World', 'Organic World, 27th Main, HSR', 'Y' ) """ ) 
    cursor.execute( """INSERT INTO STORE ( store_name, store_detail, home_delivery) VALUES( 'Lumiere', 'Lumiere Organic store, HSR', 'Y' ) """ ) 

    cursor.execute( """INSERT INTO PAYMENT_TYPE( PAYMENT_MODE, PAYMENT_MODE_DETAIL ) VALUES( 'CASH', 'Cash payment' )  """ ) 
    cursor.execute( """INSERT INTO PAYMENT_TYPE( PAYMENT_MODE, PAYMENT_MODE_DETAIL ) VALUES( 'CARD', 'Card payment' )  """ ) 
    cursor.execute( """INSERT INTO PAYMENT_TYPE( PAYMENT_MODE, PAYMENT_MODE_DETAIL ) VALUES( 'PAYTM', 'PayTM payment' )  """ ) 
    cursor.execute( """INSERT INTO PAYMENT_TYPE( PAYMENT_MODE, PAYMENT_MODE_DETAIL ) VALUES( 'SavingsAcct', 'Payment from Savings Account' )  """ ) 

    cursor.execute( """INSERT  INTO EXPENSE_CATEGORY( EXPENSE_TYPE, EXPENSE_TYPE_DETAIL ) VALUES( 'Veggies and Groceries', 'Vegetables and Groceries' )  """ ) 
    cursor.execute( """INSERT  INTO EXPENSE_CATEGORY( EXPENSE_TYPE, EXPENSE_TYPE_DETAIL ) VALUES( 'Stationaries', 'Stationaries and books' )  """ ) 
    cursor.execute( """INSERT  INTO EXPENSE_CATEGORY( EXPENSE_TYPE, EXPENSE_TYPE_DETAIL ) VALUES( 'Non Veg', 'Meat or Fish' )  """ ) 
    cursor.execute( """INSERT  INTO EXPENSE_CATEGORY( EXPENSE_TYPE, EXPENSE_TYPE_DETAIL ) VALUES( 'Hotel', 'Eat out in a Hotel' )  """ ) 
    cursor.execute( """INSERT  INTO EXPENSE_CATEGORY( EXPENSE_TYPE, EXPENSE_TYPE_DETAIL ) VALUES( 'Food Delivery', 'Home delivered food' )  """ ) 
    cursor.execute( """INSERT  INTO EXPENSE_CATEGORY( EXPENSE_TYPE, EXPENSE_TYPE_DETAIL ) VALUES( 'Others', 'Others' )  """ ) 

    cursor.execute( """INSERT INTO PERSON( PERSON_FIRST_NAME, PERSON_LAST_NAME, PERSON_SHORT_NAME ) VALUES( 'Ramakrishnan', 'Jayachandran', 'Ram' )  """ ) 
    cursor.execute( """INSERT INTO PERSON( PERSON_FIRST_NAME, PERSON_LAST_NAME, PERSON_SHORT_NAME ) VALUES( 'Nithya', 'Ramakrishnan', 'Nithya' )  """ ) 
    cursor.execute( """INSERT INTO PERSON( PERSON_FIRST_NAME, PERSON_LAST_NAME, PERSON_SHORT_NAME ) VALUES( 'Keshav', 'Ramakrishnan', 'Keshav' )  """ ) 
    cursor.execute( """INSERT INTO PERSON( PERSON_FIRST_NAME, PERSON_LAST_NAME, PERSON_SHORT_NAME ) VALUES( 'Akshara', 'Ramakrishnan', 'Akshara' )  """ ) 

    cursor.execute( """INSERT INTO LOGIN( LOGIN_ID, PASSWORD_HASH, ACTIVE ) VALUES( 'ram', 'fa44411dc4759179f96fc5fc74640242f05406c9d18814ac35bc11f97c217ac025ae17c48125fe8735fe5002ea90421587fbcf9918a14ae56423359f2cf51a21', 'A' )  """ ) 
    cursor.execute( """INSERT INTO LOGIN( LOGIN_ID, PASSWORD_HASH, ACTIVE ) VALUES( 'nithya', 'fa44411dc4759179f96fc5fc74640242f05406c9d18814ac35bc11f97c217ac025ae17c48125fe8735fe5002ea90421587fbcf9918a14ae56423359f2cf51a21', 'A' )  """ ) 
    cursor.execute( """INSERT INTO LOGIN( LOGIN_ID, PASSWORD_HASH, ACTIVE ) VALUES( 'keshav', 'fa44411dc4759179f96fc5fc74640242f05406c9d18814ac35bc11f97c217ac025ae17c48125fe8735fe5002ea90421587fbcf9918a14ae56423359f2cf51a21', 'A' )  """ ) 
    connection.commit() 
    cursor.close() 
    print( 'completed inserting seed data.')
    return True 



statements = [ 
        CREATE_PAYMENT_TYPE, 
        CREATE_EXPENSE_CATEGORY, 
        CREATE_PERSON, 
        CREATE_STORE, 
        CREATE_EXPENSE,
        CREATE_LOGIN
] 

tables = [
    'PAYMENT_TYPE',
    'EXPENSE_CATEGORY',
    'PERSON',
    'STORE',
    'EXPENSE',
    'LOGIN'
]

def create_connection( db_file ) -> sqlite3.Connection :
    
    connection = None 

    try:
        connection = sqlite3.connect( db_file )
        print( sqlite3.version ) 
    except Exception as e:
        print( e ) 
    
    return connection 

def create_tables( db_file ) -> 'boolean' :
    connection = create_connection( db_file ) 

    if connection == None :
        return False 
    
    print( 'starting table creation ... ') 
    cursor = connection.cursor() 

    try:

        cursor = connection.cursor() 

        i = 0 
        while i < len( statements) :
            print( 'Creating table %s ' % ( tables[ i ])) 
            cursor.execute( statements[ i ] ) 
            print( 'completed %s ' % (tables[ i ]))
            i = i + 1

        print( "completed creation scripts.") 
        cursor.close() 

        insert_seed_data( connection ) 

    
    except Exception as e:
        print( e ) 
    finally:
        if connection:
            connection.close() 
    
    return True

if __name__ == '__main__':
    create_tables( DB_FILE )

