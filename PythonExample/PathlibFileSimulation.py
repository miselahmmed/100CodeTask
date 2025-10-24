#Simulate path joining and name extraction using pathlib.path

from pathlib import Path

p= Path("/home/user/docs/report.txt")
print_parant = p.parent
print_name = p.name
print_suffix = p.suffix

if __name__ == '__main__':
    print("parent:", print_parant)
    print("Name:", print_name)
    print("Suffix:", print_suffix)
    