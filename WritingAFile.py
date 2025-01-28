# LEARN PYTHON: FILES
# Writing a File
# 4/13

# Reading a file is all well and good, but what if we want to create a file of our own? With Python we can do just that.
# It turn out that our open() function that we're using to open a file to read needs another argument to open a file to
# write to.

# script.py
# ***Uncomment to see code***
# with open('generated_file.txt', 'w') as gen_file:
#   gen_file.write("What an incredible file!")

# Here we pass the argument 'w' to open() in order to indicate to open the file in write-mode. The default argument is
# 'r' and passing 'r' to open() opens the file in read-mode as we've been doing.

# This code creates a new file in the same folder as script.py and gives it the text Wht an incredible file! It's
# important to note that if there is already a file called generated_file.txt it will completely overwrite that file,
# erasing whatever its contents were before.

# ***INSTRUCTIONS***
# 1. Create a file object for the file bad_bands.txt using the open() function with the w argument. Assign this object
# to the temporary variable bad_bands_doc
with open('bad_bands.txt', 'w') as bad_bands_doc:
    # 2. Use the bad_bands_doc.write() method to add the name of a musical group you dislike to the document bad_bands.
    bad_bands_doc.write("Lizzo")
