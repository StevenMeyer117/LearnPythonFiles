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