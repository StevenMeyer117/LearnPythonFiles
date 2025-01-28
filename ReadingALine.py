# Reading A Line
# 3/13

# Sometimes you don't want to iterate through a whole file. For that, there's a different file method, .readline(),
# which will only read a single line at a time. If the entire document is read line by line in this way subsequent calls
# to .readline() will not throw an error but will start returning an empty string (""). Suppose we had this file:
# millay_sonnet.txt
# I shall forget you presently, my dear,
# So make the most of this, your little day,
# Your little month, your little half a year,
# Ere I forget, or die, or move away,

# script.py
# ***Uncomment to see code***
# with open('millay_sonnet.txt') as sonnet_doc:
#   first_line = sonnet_doc.readline()
#   second_line = sonnet_doc.readline()
#   print(second_line

# This script also create a file object called sonnet_doc that points to the file millay_sonnet.txt. It then reads in
# the first line using sonnet_doc.readline() and saves that to the variable first_line. It then saves the second line
# (So make the most of this, your little day,) into a variable second_line and then prints it out

# ***INSTRUCTIONS***
# 1. Using a with statement, create a file object pointing to the file just_the_first.txt
with open('just_the_first.txt') as first_line_doc:
    # 2. Save the first line of just_the_first.txt into the variable first_line
    first_line = first_line_doc.readline()
# 3. Print out the variable first_line
print(first_line)
