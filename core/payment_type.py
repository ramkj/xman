
class PaymentType:

    def __init__( self, id : int, payment_mode : str, payment_mode_detail : str ):
        self.id = id 
        self.payment_mode = payment_mode
        self.payment_mode_detail = payment_mode_detail
    
    def getId( self ) -> int:
        return self.id 

    def getPaymentMode( self ) -> str:
        return self.payment_mode 
    
    def getPaymentModeDetail( self ) -> str:
        return self.payment_mode_detail
