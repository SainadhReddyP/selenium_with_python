"""
Regular Expressions (RegEx)
are used to check whether the search pattern is available in the string.
- import re
"""
import re


pattern = "Sainadh"
user_input = input("Enter any text: ")
if re.search(pattern,user_input):
    print("Pattern got matched.")
else:
    print("Pattern didn't match.")

# user_input = "sainadh" - pattern didn't match

new_pattern = "[Ss]ainadh"
if re.search(new_pattern,user_input):
    print("Pattern got matched.")
else:
    print("Pattern didn't match.")












