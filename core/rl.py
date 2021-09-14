# core reporting layer 

from core.da.dal import DataAccessLayer

class ReportingLayer:

    def __init__( self ):
        self.dal=None 
    
    def setDALayer( self, dal : DataAccessLayer ) -> None:
        self.dal = dal 

    def listMonthwiseSummary( self ) -> tuple:
        report_header = [ 'Month', 'COUNT', 'Amount Spent'] 
        return ( report_header, self.dal.getMonthwiseExpenseSummary() ) 

    def listMonthwiseCategorySummary( self ) -> tuple:
        report_header = [ 'Month', 'Category', 'Count', 'Amount Spent' ]
        return ( report_header, self.dal.getMonthwiseCategoryExpense())
    
    def listMonthwisePersonSummary( self ) -> tuple:
        report_header = [ 'Month', 'Person', 'Count', 'Amount Spent' ]
        return ( report_header, self.dal.getMonthwisePersonSummary())
    
    def listMonthwisePaymentTypeSummary( self ) -> tuple:
        report_header = [ 'Month', 'Payment Type', 'Count', 'Amount Spent' ]
        return ( report_header, self.dal.getMonthwisePaymentTypeSummary())
