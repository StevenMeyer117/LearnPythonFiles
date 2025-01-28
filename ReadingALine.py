# Reading A Line
# 3/13

# Sometimes you don't want to iterate through a whole file. For that, there's a different file method, .readline(),
# which will only read a single line at a time. If the entire document is read line by line in this way subsequent calls
# to .readline() will not throw an error but will start returning an empty string (""). Suppose we had this file: