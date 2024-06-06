#-------------IMMUTABLE PROPERTY DECARATOR-------------------------
def immutable_property(func):
   
    #Decorator to make a property immutable.
    
    attribute = "_immutable_" + func.__name__

    @property
    def wrapper(self):
        if not hasattr(self, attribute):
            setattr(self, attribute, func(self))
        return getattr(self, attribute)

    return wrapper
