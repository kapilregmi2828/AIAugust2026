#external modules
import pandas
import numpy

# Internal modules

import os
import datetime
import sys

# enabling environment files and variables 

openai_api_key = os.environ.get("OPENAI_API_KEY")
username = os.environ.get("oracle_user")
password = os.environ.get("orcle_password")

a = 10

s = ""

for i in range(1, a +1):
    s += str(i) + " " # += defines concatenation of strings and here we convert i into string first and add a space after it to separate the numbers

print(s)


