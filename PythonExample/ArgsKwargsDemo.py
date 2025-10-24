# Demostrate *args and **kwargs usage.

def printer(*arg, **kwargs):
    print("ARGS:", arg)
    print("KW:", kwargs)

if __name__ == '__main__':
    printer(1,2,3, a=10, b=20)