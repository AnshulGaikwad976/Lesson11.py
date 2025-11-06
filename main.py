class empyee:

     def __init__(self):
        print("constructor created")

     def __del__(self):    
        print("destructor called, employed deleted")


obj = empyee()
del obj