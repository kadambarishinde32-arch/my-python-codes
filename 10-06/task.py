# Student Dictionary
stud = {
    101: {
          "name":"ram",
          "age":18,
          "sub":("python","java","mern"),
          "marks":[50,89,78]
          },
    102: {
          "name":"sita",
          "age":19,
          "sub":("python","java","mern"),
          "marks":[70,80,90]
          },
    103: {
          "name":"rahul",
          "age":20,
          "sub":("python","java","mern"),
          "marks":[58,79,100]
          },
    104: {
          "name":"gita",
          "age":21,
          "sub":("python","java","mern"),
          "marks":[88,97,100]
          }
}

# 1. Total marks of each student
print("Total Marks")

for roll, details in stud.items():
    total = sum(details["marks"])
    print(roll, ":", total)


# 2. Find topper
highest = 0
topper = ""

for roll, details in stud.items():
    total = sum(details["marks"])

    if total > highest:
        highest = total
        topper = details["name"]

print("\nTopper")
print("Name:", topper)
print("Marks:", highest)


# 3. Highest marks in Python
highest_python = 0
python_topper = ""

for roll, details in stud.items():

    if details["marks"][0] > highest_python:
        highest_python = details["marks"][0]
        python_topper = details["name"]

print("\nHighest in Python")
print("Name:", python_topper)
print("Marks:", highest_python)


# 4. Students with age greater than 19
print("\nAge > 19")

for roll, details in stud.items():

    if details["age"] > 19:
        print(details["name"])


# 5. Students with MERN marks between 70 and 90
print("\nMERN Marks > 70 and < 90")

for roll, details in stud.items():

    if details["marks"][2] > 70 and details["marks"][2] < 90:
        print(details["name"], details["marks"][2])