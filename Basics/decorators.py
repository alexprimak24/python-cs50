# decorators - a function that takes a function, modifies it by adding additional 
# capabilities and give us back some output

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function")
    return wrapper

# adds announce decorator to the function
@announce
def hello():
    print("Hello, world!")

hello()