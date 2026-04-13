import sys
import json

if len(sys.argv)>1:
  print(f"Ok, lets see if {sys.argv[1]}  is in the correct location you look for")
  with open(sys.argv[1], "r" ) as f:
    for line in f:
      row=json.loads(line)
      print(f"At{row['timestamp']}, an event happened: {row['event']}")
else:
  print("Sorry, you haven't given the name of the json as argument")
