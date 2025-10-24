#Demonstrate pop with default.
d= {"a":1, "b":2}
x = d.pop("b", None)
if __name__ == '__main__':
    print("Popped value:", x)
    print("Remaining: ",d)