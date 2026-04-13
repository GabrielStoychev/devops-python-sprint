import json
my_data={
  "name":"Gabriel",
  "role":"Junior Devops",
  "company": "ICT Strypes",
  "list_key": ["Python", "Linux", "Git"]
  }

with open("profile.json", "w") as f:
  json.dump(my_data, f, indent=4)
print("Done! profile.json should be working now!")