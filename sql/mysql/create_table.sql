

use xman ;

SELECT 'Cleaning up - dropping all the tables (if any) - please ignore errors' AS ' ' ;

DROP TABLE EXPENSE ;
DROP TABLE PAYMENT_TYPE ;
DROP TABLE EXPENSE_CATEGORY ;
DROP TABLE PERSON ;
DROP TABLE STORE ;
DROP TABLE LOGIN ;

SELECT 'creating tables for xman - please ensure there are no errors' AS ' '  ;
CREATE TABLE PAYMENT_TYPE (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    PAYMENT_MODE VARCHAR( 20 ) NOT NULL,
    PAYMENT_MODE_DETAIL VARCHAR( 80 )
);


CREATE TABLE EXPENSE_CATEGORY (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    EXPENSE_TYPE VARCHAR( 40 ),
    EXPENSE_TYPE_DETAIL VARCHAR( 80 )
);


CREATE TABLE PERSON (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    PERSON_FIRST_NAME VARCHAR( 100 ) NOT NULL,
    PERSON_LAST_NAME VARCHAR( 100 ) NOT NULL,
    PERSON_SHORT_NAME VARCHAR( 50 ) NOT NULL
);


CREATE TABLE STORE (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    STORE_NAME VARCHAR( 40 ) NOT NULL,
    STORE_DETAIL VARCHAR( 100 ),
    HOME_DELIVERY VARCHAR( 1 )
);



CREATE TABLE EXPENSE (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    EXPENSE_DETAIL VARCHAR(60),
    EXPENSE_CATEGORY_ID INT,
    EXPENSE_DATE DATE ,
    EXPENSE_AMOUNT NUMERIC(10,3),
    PAYMENT_TYPE_ID INT,
    PERSON_ID INT,
    STORE_ID INT,
    FOREIGN KEY( EXPENSE_CATEGORY_ID ) REFERENCES EXPENSE_CATEGORY( ID ),
    FOREIGN KEY( PAYMENT_TYPE_ID ) REFERENCES PAYMENT_TYPE( ID ),
    FOREIGN KEY( PERSON_ID ) REFERENCES PERSON( ID ),
    FOREIGN KEY( STORE_ID ) REFERENCES STORE( ID )
);

CREATE TABLE LOGIN (
    LOGIN_ID        VARCHAR( 75 ) NOT NULL,
    PASSWORD_HASH   VARCHAR( 256 ) NOT NULL,
    ACTIVE          VARCHAR( 1 )
);




