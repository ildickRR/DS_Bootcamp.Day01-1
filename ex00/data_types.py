def data_types():
    a = 5
    b = "Hello, World!"
    c = 3.14
    d = True
    e = [1, 2, 3, 4, 5]
    f = {"a" : 5}
    g = (1, 2, 3)
    h = {1,2,3,4,5}

    types_list = [type(a).__name__, type(b).__name__, type(c).__name__,
     type(d).__name__, type(e).__name__, type(f).__name__, 
     type(g).__name__, type(h).__name__] 

    print("["+','.join(types_list)+"]")

if __name__ == "__main__":
    data_types()