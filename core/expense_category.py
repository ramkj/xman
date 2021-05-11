
#########################################################################
## class: ExpenseCategory
## why: This is a business domain class 
## who uses this: used by bl (BusinessLayer)
#########################################################################

class ExpenseCategory:
    def __init__( self, id: int, expense_type : str, expense_detail : str  ) :
        self.id = id 
        self.expenseType = expense_type 
        self.expenseDetail = expense_detail 

    def setId( self, id : int ) -> None:
        self.id = id 
        
    def setExpenseType( self, expense_type : str ) -> None:
        self.expenseType = expense_type 
    
    def setExpenseDetail( self, expense_detail : str ) -> None:
        self.expenseDetail = expense_detail 
    
    def getId( self ) -> int:
        return self.id 

    def getExpenseType( self ) -> str :
        return self.expenseType
    
    def getExpenseDetail( self ) -> str :
        return self.expenseDetail
