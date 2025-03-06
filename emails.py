#!/usr/bin/env python3

import csv
import sys

def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict

def find_email(argv):
  """ Return an email address based on the username given."""
  # Create the username based on the command line input.
  try:
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    email_dict = populate_dictionary('/home/student/data/user_emails.csv')
     # If email exists, print it
    if email_dict.get(fullname.lower()):
      return email_dict.get(fullname.lower())
    else:
      return "No email address found"
  except IndexError:
    return "Missing parameters"

def main():
  print(find_email(sys.argv))

if __name__ == "__main__":
  main()

#This script consists of two functions: populate_dictionary(filename) and find_email(argv). The function populate_dictionary(filename) reads the user_emails.csv file and populates a dictionary with name/value pairs. The other function, find_emails(argv), searches the dictionary created in the previous function for the user name passed to the function as a parameter.
# python3 emails.py Blossom Gill
# output: blossom@abc.edu
