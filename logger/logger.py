import functools 

logfile = None 
_LOGFILE_ = "./logs/app.log"
should_log = True 
def log( func ):
    @functools.wraps( func )
    def log_wrapper(*args, **kwargs):
        if not logfile:
            logfile = open( _LOGFILE_, "a" ) 
        
        if should_log:
            logfile.write( "calling " + func.__name__ ) 
            logfile.flush() 
        
        return func( args, kwargs )
    return log_wrapper


