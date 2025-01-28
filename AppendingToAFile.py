# LEARN PYTHON: FILES
# Appending to a File
# 5/13

# So maybe completely deleting and overwriting existing files is something that bothers you. Isn't there a way to just
# add a line to a file without completely deleting it? Of course there is! Instead of opening the file argument 'w' for
# write-mode, we open it with 'a' for append-mode. If we ahve a generated file with the following contents:

# generated_file.txt
# This was a popular file...

# Then we can add another line to that file with the following code:

# script.py
# with open('generated_file.txt', 'a') as gen_file:
#   gen_file.write("\n... and it still is")

# In the code above we open a file object in the temporary variable gen_file. Ths variable points to the file
# generated_file.txt and, since it's open in append-mode, adds the string \n... and it still is to the file. The newline
# character \n moves to the next line before adding the rest of the string. If you were to open the file after running
# the script it would look like this:

# generated_file.txt
# This was a popular file...
# ... and it still is

# Notice that opening the file in append-mode, with 'a' as an argument to open(), means that using the file object's
# .write() method appends whatever is passed to the end of the file. If we were to run script.py again, this would be
# what generated_file.txt looks like:

# generated_file.txt
# This was a popular file...
# ... and it still is
# ... and it still is

# ***INSTRUCTIONS***
# 1. We've got a file, cool_dogs.txt, filled with all the cool dogs we know. Somehow while compiling this list we forgot
# about one very cool dog. Let's fix that problem by adding him to our cool_dogs.txt

# Open up our file cool_dogs.txt in append-mod and assign it to the file object cool_dogs_file
with open('cool_dogs.txt', 'a') as cool_dogs_file:
    # 2. Inside your with block, add "Air Buddy\n" to cool_dogs.txt. Air Buddy is a Golden Retriever that plays
    # basketball, which more than qualifies him for this list. The \n character moves to the next line after appending
    # the string.
    cool_dogs_file.write("Air Buddy\n")
