class Student:
    # Class variable (static variable) to keep track of total students
    counter = 0

    def __init__(self, name, major):
        # Instance variables unique to each student
        self.name = name
        self.major = major
        
        # Increment the static counter using the class name
        Student.counter += 1
        
        # Assign the current counter value as a unique ID
        self.id = Student.counter

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Major: {self.major}"

# --- Demonstration ---

# 1. Check counter before creating students
print(f"Initial count: {Student.counter}")

# 2. Create student instances
s1 = Student("Alice", "Computer Science")
print(f"Initial count: {Student.counter}") # check how its value in process

s2 = Student("Bob", "Mechanical Engineering")
s3 = Student("Charlie", "Data Science")

# 3. Print student details
print(s1)
print(s2)
print(s3)

# 4. Check the final count
print(f"\nFinal Total Students: {Student.counter}")