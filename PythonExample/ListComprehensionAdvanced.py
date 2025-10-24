# Create a list of squared even numbers and filter with a function.

def is_even(n):
    return n % 2 == 0

squared_evens = [x*x for x in range(20) if is_even(x)]
if __name__ == '__main__':
    print("Even suqares:", squared_evens)
    print("Count:", len(squared_evens))