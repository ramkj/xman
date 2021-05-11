

class Person:

    def __init__( self, id : int, first_name : str, last_name : str, short_name ):
        self.id = id 
        self.first_name = first_name 
        self.last_name = last_name 
        self.short_name = short_name

    def getId( self ) -> int:
        return self.id 

    def getFirstName( self ) -> str:
        return self.first_name 

    def getLastName( self ) -> str:
        return self.last_name 
    
    def getShortName( self ) -> str:
        return self.short_name 
