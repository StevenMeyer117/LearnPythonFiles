import os
print(os.getcwd())

# Computers use file systems to store and retrieve data. Each file is an individual container of related information. If
# you've ever saved a document, downloaded a song, or even sent an email you've created a file on some computer
# somewhere.

# So, how do we interact with files using Python? We're going to learn how to read and write different kinds of files
# using code. Let's say we had a file called real_coo_document.txt with these contents:
# Wowsers!

# We could read that file like this:
# ***Uncomment the next lines to see how code looks***
# with open('real_cool_document.txt') as cool_doc:
#   cool_contents = cool_doc.read()
# print(cool_contents)

# This opens a file object called cool_doc and creates a new indented block where you can read the contents of the
# opened file. We then read the contents of the file coo_doc using cool_doc.read() and save the resulting string into
# the variable cool_contents. Then we print coo_contents, which outputs the statement Wowsers!

# ***INSTRUCTIONS***
# 1. Use with to open the file welcom.txt. Save the file object as text_file
with open('welcome.txt') as text_file:
# 2. Read the contents of text_file and save teh results in text_data
     text_data = text_file.read()
# Print out text_data
print(text_data)