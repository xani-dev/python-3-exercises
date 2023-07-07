class ValidationException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Custom class that extends the 'Exception' base class
# Takes only 1 parameter - message
# line 4 INVOKES the __init__ of the 'Exception' class