def main():
    hello('world')
    goodbye('world')

def hello(name):
    print(f"Hello, {name}!")

def goodbye(name):
    print(f"Goodbye, {name}!")

if __name__ == "__main__": # only running this if the script is executed directly 
    main()