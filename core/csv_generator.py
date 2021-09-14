

import csv 

__tmpfolder__ = './tmp/'

class CSVGenerator:
    def __init__( self ):
        pass
    
    def generateFile( self, file_name : str, all_rows : list ) -> None:
        with open( __tmpfolder__ + file_name, 'w', newline='') as file:
            writer = csv.writer( file )
            writer.writerows( all_rows )

    def getFilenameWithPath( self, file_name : str ) -> str:
        return __tmpfolder__ + file_name ; 

