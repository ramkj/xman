INSERT INTO STORE ( store_name, store_detail, home_delivery) VALUES( 'Lumiere', 'Lumiere Organic store, HSR', 'Y' ) ;
INSERT INTO STORE ( store_name, store_detail, home_delivery) VALUES( 'Eco Store', 'Eco Store - Organic, HSR', 'Y' ) ;
INSERT INTO STORE ( store_name, store_detail, home_delivery) VALUES( 'Organic World', 'Organic World, 27th Main, HSR', 'Y' ) ;
INSERT INTO STORE ( store_name, store_detail, home_delivery) VALUES( 'Lumiere', 'Lumiere Organic store, HSR', 'Y' ) ;

INSERT INTO PAYMENT_TYPE( PAYMENT_MODE, PAYMENT_MODE_DETAIL ) VALUES( 'CASH', 'Cash payment' ) ;
INSERT INTO PAYMENT_TYPE( PAYMENT_MODE, PAYMENT_MODE_DETAIL ) VALUES( 'CARD', 'Card payment' ) ;
INSERT INTO PAYMENT_TYPE( PAYMENT_MODE, PAYMENT_MODE_DETAIL ) VALUES( 'PAYTM', 'PayTM payment' ) ;
INSERT INTO PAYMENT_TYPE( PAYMENT_MODE, PAYMENT_MODE_DETAIL ) VALUES( 'SavingsAcct', 'Payment from Savings Account' ) ;

INSERT  INTO EXPENSE_CATEGORY( EXPENSE_TYPE, EXPENSE_TYPE_DETAIL ) VALUES( 'Veggies and Groceries', 'Vegetables and Groceries' ) ;
INSERT  INTO EXPENSE_CATEGORY( EXPENSE_TYPE, EXPENSE_TYPE_DETAIL ) VALUES( 'Stationaries', 'Stationaries and books' ) ;
INSERT  INTO EXPENSE_CATEGORY( EXPENSE_TYPE, EXPENSE_TYPE_DETAIL ) VALUES( 'Non Veg', 'Meat or Fish' ) ;
INSERT  INTO EXPENSE_CATEGORY( EXPENSE_TYPE, EXPENSE_TYPE_DETAIL ) VALUES( 'Hotel', 'Eat out in a Hotel' ) ;
INSERT  INTO EXPENSE_CATEGORY( EXPENSE_TYPE, EXPENSE_TYPE_DETAIL ) VALUES( 'Food Delivery', 'Home delivered food' ) ;
INSERT  INTO EXPENSE_CATEGORY( EXPENSE_TYPE, EXPENSE_TYPE_DETAIL ) VALUES( 'Others', 'Others' ) ;

INSERT INTO PERSON( PERSON_FIRST_NAME, PERSON_LAST_NAME, PERSON_SHORT_NAME ) VALUES( 'Ramakrishnan', 'Jayachandran', 'Ram' ) ;
INSERT INTO PERSON( PERSON_FIRST_NAME, PERSON_LAST_NAME, PERSON_SHORT_NAME ) VALUES( 'Nithya', 'Ramakrishnan', 'Nithya' ) ;
INSERT INTO PERSON( PERSON_FIRST_NAME, PERSON_LAST_NAME, PERSON_SHORT_NAME ) VALUES( 'Keshav', 'Ramakrishnan', 'Keshav' ) ;
INSERT INTO PERSON( PERSON_FIRST_NAME, PERSON_LAST_NAME, PERSON_SHORT_NAME ) VALUES( 'Akshara', 'Ramakrishnan', 'Akshara' ) ;

INSERT INTO LOGIN( LOGIN_ID, PASSWORD_HASH, ACTIVE ) VALUES( 'ram', 'fa44411dc4759179f96fc5fc74640242f05406c9d18814ac35bc11f97c217ac025ae17c48125fe8735fe5002ea90421587fbcf9918a14ae56423359f2cf51a21', 'A' ) ;
INSERT INTO LOGIN( LOGIN_ID, PASSWORD_HASH, ACTIVE ) VALUES( 'nithya', 'fa44411dc4759179f96fc5fc74640242f05406c9d18814ac35bc11f97c217ac025ae17c48125fe8735fe5002ea90421587fbcf9918a14ae56423359f2cf51a21', 'A' ) ;
INSERT INTO LOGIN( LOGIN_ID, PASSWORD_HASH, ACTIVE ) VALUES( 'keshav', 'fa44411dc4759179f96fc5fc74640242f05406c9d18814ac35bc11f97c217ac025ae17c48125fe8735fe5002ea90421587fbcf9918a14ae56423359f2cf51a21', 'A' ) ;

-- Query for getting expense detail
SELECT EXPENSE.expense_detail AS expense_detail, EXPENSE.expense_date as expense_date, EXPENSE.expense_amount as expense_amount,
    EXPENSE_CATEGORY.EXPENSE_TYPE expense_type, PAYMENT_TYPE.PAYMENT_MODE payment_type,
    PERSON.PERSON_SHORT_NAME person_name, STORE.store_name store_name FROM EXPENSE, EXPENSE_CATEGORY, PAYMENT_TYPE, PERSON, STORE
    WHERE EXPENSE.expense_category_id = EXPENSE_CATEGORY.ID AND
        EXPENSE.payment_type_id = PAYMENT_TYPE.ID AND
        EXPENSE.person_id = PERSON.ID AND
        EXPENSE.store_id =  STORE.ID ;

-- Month by month expense
SELECT SUBSTR( EXPENSE_DATE, 1, 7 ), COUNT( ID ), SUM(EXPENSE_AMOUNT) FROM EXPENSE GROUP BY SUBSTR( EXPENSE_DATE, 1, 7 );

-- Month wise categories - number of expenditure count and sum
SELECT SUBSTR( EXPENSE_DATE, 1, 7 ), EXPENSE_CATEGORY_ID, COUNT( ID ), SUM(EXPENSE_AMOUNT) FROM EXPENSE GROUP BY SUBSTR( EXPENSE_DATE, 1, 7 ), EXPENSE_CATEGORY_ID ;

-- Month wise people - number of expenditure count and sum
SELECT SUBSTR( EXPENSE_DATE, 1, 7 ), PERSON_ID, COUNT( ID ), SUM(EXPENSE_AMOUNT) FROM EXPENSE GROUP BY SUBSTR( EXPENSE_DATE, 1, 7 ), PERSON_ID ;



SELECT SUBSTR( EXPENSE_DATE, 1, 7 ), EXPENSE_CATEGORY_ID, COUNT( ID ), SUM(EXPENSE_AMOUNT) FROM EXPENSE GROUP BY SUBSTR( EXPENSE_DATE, 1, 7 ), EXPENSE_CATEGORY_ID ORDER BY EXPENSE_DATE DESC, EXPENSE_CATEGORY_ID

-- Expenses by month and category
SELECT SUBSTR( EXPENSE_DATE, 1, 7),  EXPENSE_CATEGORY.EXPENSE_TYPE,  COUNT( EXPENSE.ID), SUM( EXPENSE_AMOUNT ) from EXPENSE, EXPENSE_CATEGORY WHERE EXPENSE.EXPENSE_CATEGORY_ID = EXPENSE_CATEGORY.ID GROUP BY SUBSTR( EXPENSE_DATE, 1, 7), EXPENSE_CATEGORY.EXPENSE_TYPE ORDER BY EXPENSE_DATE,  EXPENSE_CATEGORY.EXPENSE_TYPE 

-- Expenses by month and people
SELECT SUBSTR( EXPENSE_DATE, 1, 7),  PERSON.PERSON_SHORT_NAME,  COUNT( EXPENSE.ID), SUM( EXPENSE_AMOUNT ) from EXPENSE, PERSON WHERE EXPENSE.PERSON_ID = PERSON.ID GROUP BY SUBSTR( EXPENSE_DATE, 1, 7), PERSON.PERSON_SHORT_NAME ORDER BY EXPENSE_DATE,  PERSON.PERSON_SHORT_NAME

-- Expense by month and Payment Type
SELECT SUBSTR( EXPENSE_DATE, 1, 7),  PAYMENT_TYPE.PAYMENT_MODE,  COUNT( EXPENSE.ID), SUM( EXPENSE_AMOUNT ) from EXPENSE, PAYMENT_TYPE WHERE EXPENSE.PAYMENT_TYPE_ID = PAYMENT_TYPE.ID GROUP BY SUBSTR( EXPENSE_DATE, 1, 7), PAYMENT_TYPE.PAYMENT_MODE ORDER BY EXPENSE_DATE,  PAYMENT_TYPE.PAYMENT_MODE