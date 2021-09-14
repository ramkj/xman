import time 

class Timer:
    def __init__( self, fname : str ):
        self.fname = fname 

    def __enter__( self ) -> int :
        self.start_time = int(time.time())
        return self.start_time
    
    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.end_time = int(time.time())
        print( f'Total time spent on {self.fname} : {self.end_time - self.start_time} seconds' )
