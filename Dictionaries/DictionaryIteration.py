#Show different ways to iterarte though a dictionary.
student = {"name": "Bob", "age": 22, "grade": "A"}
if __name__ == '__main__':
    print("Keys")
    for key in student:
        print(key)
    print("\nValues:")
    for value in student.values():
        print(value)
    print("\nItems:")
    for key, value in student.items():
        print(f"{key} => {value}")
