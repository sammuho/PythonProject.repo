#syntax error missing or additional braces or brackets
#handling exception
class valueTooHighError(Exception):
    pass
#or add some more information for handlers
class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message= message
        self.value=value
def test_value(a):
    if a > 1000:
        raise valueTooHighError('Value too high') 
    if a < 5:
        #constructor takes 2 arguments
        raise ValueTooLowError('Value too low', a) 
    return a  
try:
    test_value(10)
except valueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, 'The value is:', e.value)
else:
    #test_value < 5 & > 1000:
    print('Value within Range')   