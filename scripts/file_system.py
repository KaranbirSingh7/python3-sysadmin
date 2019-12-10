
# a: open in read/write mode without worrying about truncating
with open('/tmp/xmen_base.txt', 'a') as f:
    f.write("Professor Xavier\n")
