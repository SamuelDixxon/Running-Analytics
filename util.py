import os
import datetime

# Prompt the user to input the directory name
directory_name = input("Enter the name of the new directory: ")

# Set the directory path
directory_path = os.path.join(os.getcwd(), directory_name)

# Create the directory
try:
    os.mkdir(directory_path)
    print("Directory created successfully!")
except FileExistsError:
    print("Error: Directory already exists!")

# Create the README file
with open(os.path.join(directory_path, "README.md"), "w") as f:
    f.write("# " + directory_name + "\n\n")
    f.write("This is a new directory created on " + str(datetime.datetime.now()) + "\n")

print("Directory populated with README file!")
