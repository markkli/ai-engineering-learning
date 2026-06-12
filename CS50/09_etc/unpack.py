def total(galleons, sickles, knuts):
    return galleons * 493 + sickles * 17 + knuts

coins = [100, 200, 300]

print(total (*coins), "Knuts") # * unpacks the list into separate arguments

coins_dict = {"galleons": 100, "sickles": 200, "knuts": 300}
print(total(**coins_dict), "Knuts") # ** unpacks the dictionary into separate keyword arguments

def f(*args, **kwargs): 
    """
    Explanation: This function takes a variable number of positional arguments (*args)
    and a variable number of keyword arguments (**kwargs). It prints the positional
    arguments as a tuple and the keyword arguments as a dictionary.
    """
    print('positional', args)
    print('keyword', kwargs)