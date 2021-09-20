


SELECT EXPENSE.expense_detail AS expense_detail, EXPENSE.expense_date as expense_date, EXPENSE.expense_amount as expense_amount, 
    EXPENSE_CATEGORY.EXPENSE_TYPE as expense_type, PAYMENT_TYPE.PAYMENT_MODE as payment_type,
    PERSON.PERSON_SHORT_NAME person_name, STORE.store_name store_name FROM EXPENSE
    LEFT JOIN EXPENSE_CATEGORY ON EXPENSE.EXPENSE_CATEGORY_ID = EXPENSE_CATEGORY.ID 
    LEFT JOIN PAYMENT_TYPE ON EXPENSE.payment_type_id = PAYMENT_TYPE.ID 
    LEFT JOIN PERSON ON EXPENSE.person_id = PERSON.ID 
    LEFT JOIN STORE ON EXPENSE.store_id =  STORE.ID 



    , EXPENSE_CATEGORY, PAYMENT_TYPE, PERSON, STORE
    WHERE EXPENSE.expense_category_id = EXPENSE_CATEGORY.ID AND
        EXPENSE.payment_type_id = PAYMENT_TYPE.ID AND
        EXPENSE.person_id = PERSON.ID AND
        EXPENSE.store_id =  STORE.ID 

