def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce    
def hello():
    print("Run hello() function with printing out Hello, World!")

hello()