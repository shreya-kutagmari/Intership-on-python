def outer_function(x):
    def inner_function(y):
        return x+y
    return inner_function

closure=outer_function(13)
print(closure(5))