import os

folder_path = input("Enter folder path: ")
prefix = input("Enter new file prefix: ")

files = os.listdir(folder_path)

count = 1

for file in files:
    old_path = os.path.join(folder_path, file)

    if os.path.isfile(old_path):
        extension = os.path.splitext(file)[1]
        new_name = f"{prefix}_{count}{extension}"
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {file} -> {new_name}")

        count += 1

print("Done!")

