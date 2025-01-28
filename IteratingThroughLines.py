# Iterating Through Lines
# 2/13

# When we read a file, we might want to grab the whole document in a single string, like .read() would return. But what
# if we wanted to store each line in a variable? We can use the .readlines() function to read a text file line by line
# instead of having the whole thing. Suppose we have a file:
# keats_sonnet.txt
# To one who has been long in city pent,
# 'Tis very sweet to look into the fair
# And open face of heave,-to breathe a prayer
# Full in the smile of the blue firmament

# script.py
# ***Uncomment to see code***
# with open('keats_sonnet.txt') as keats_sonnet:
#   for line in keats_sonnet.readlines():
#       print(line)

# The above script creates a temporary file object called keats_sonnet that points to the file keats_sonnet.txt. It then
# iterates over each line in the document and prints the entire file out.

# ***INSTRUCTIONS***
# 1. Using a with statement, create a file object pointing to the file how_many_lines.txt. Store that file object in the
# variable lines_doc
with open('how_many_lines.txt') as lines_doc:
    # 2. Iterate through each of the lines in lines_doc.readlines() using a for loop. Inside the for loop print out each
    # line of how_many_lines.txt
    for line in lines_doc.readlines():
        print(line)