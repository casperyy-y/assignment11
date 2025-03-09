last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson"]

def display_names(names):
    print("\nList of Last Names:")
    for name in names:
        print(name)

def display_names_reverse(names):
    print("\nList of Last Names in Reverse Order:")
    for name in reversed(names):
        print(name)

display_names(last_names)
display_names_reverse(last_names)
