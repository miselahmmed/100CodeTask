#Simple CSV parsing without CSV module.

line = "name,age,city"
data = [s.strip() for s in line.split(",")]
if __name__ == '__main__':
    print("Columns:", data)