#Perform common set operations: Union, Intersection, diffrence.

a= {1,2,3,4}
b= {3,4,5,6}

if __name__ == '__main__':
    print("Union:", a|b)
    print("Intersection:", a &b)
    print("Diffrence (a-b):", a-b)
    print("Symmetric diffrence:", a^b)