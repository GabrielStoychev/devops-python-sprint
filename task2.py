import os

folder_path=input("Enter the folder path to scan: ")

if os.path.exists(folder_path):
  print(f"Scanning: {folder_path}")
  items=os.listdir(folder_path)

  for item in items:
    if item.startswith("2026"):
      print(f"Found: {item}")
else:
  print("Invalid path! Try again")