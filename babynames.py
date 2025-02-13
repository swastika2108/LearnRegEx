#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re #reggex module

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
# <h3 align="center">Popularity in 2006</h3>


def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  with open(filename,'r') as f:
    text=f.read()
    
  
  year_match=re.search(r'Popularity\s+in\s+(\d{4})',text)
  if not year_match:
    raise ValueError("Year not found in the file")
  
  year=year_match.group(1)
  print(f"Year:{year}")
  

  tuples=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td',text)
  print(f"Tuples:{tuples}")
  return year,tuples


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  # summary = False
  # if args[0] == '--summaryfile':
  #   summary = True
  #   del args[0]

  for filename in args:
    print(f"Processing the files as requested:{filename}")

    try:
      year,tuple=extract_names(filename)
      output=[year]+[f'{name}{rank}' for rank,name,_ in tuple]

    except Exception as e:
      print(f"Error Processing file {filename}")

    # if summary:
    #   summary_filename=f"{filename}.summary"
    #   with open(summary_filename,'w') as summary_file:
    #     summary_file.write(text)
    #   print(f"Summary written to {summary_filename}")
    # else:
    #   print(text)


if __name__ == '__main__':
  main()
