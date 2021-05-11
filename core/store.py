
#########################################################################
## class: Store
## why: This is a business domain class 
## who uses this: used by bl (BusinessLayer)
#########################################################################

class Store:
    def __init__( self, id : int, store_name : str, store_detail : str, home_delivery : bool  ) :
        self.id = id 
        self.storeName = store_name
        self.storeDetail = store_detail
        self.homeDelivery = home_delivery

    def setId( self, id : int ) -> None:
        self.id = id 
    
    def setStoreName( self, store_name : str ) -> None:
        self.storeName = store_name 
    
    def setStoreDetail( self, store_detail : str ) -> None:
        self.storeDetail = store_detail 
    
    def setHomeDelivery( self, home_delivery : bool ) -> None: 
        self.homeDelivery = home_delivery

    def getId( self ) -> int:
        return self.id 

    def getStoreName( self ) -> str :
        return self.storeName
    
    def getStoreDetail( self ) -> str :
        return self.storeDetail

    def getHomeDelivery( self ) -> bool:
        return self.homeDelivery  

    def getHomeDeliveryString( self ) -> str:
        if self.homeDelivery == True:
            return 'Y'
        else: 
            return 'N'
