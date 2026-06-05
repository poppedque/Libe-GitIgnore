import os

files_to_ignore = set()

print("----Libe---")
print("Type a file or folder name to ignore. Type 'done' when you are finished.")

while True:
    user_input = input("Enter a file or folder name: ")

    if user_input.lower() == 'done':
        break

    files_to_ignore.add(user_input)

    with open('.gitignore', 'w') as f:
        for item in files_to_ignore:
            f.write(item + "\n")

print("Thanks. Your .gitignore file has been created.")
print("Thank you for using Libe!")

# Thank you for viewing our source code!
