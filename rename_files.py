import os

filesdir = r"C:\My files"  # Choose a directory (for local disk use \\ at the end e.g. C:\\)
old = ""  # Old characters to change/remove
new = ""  # New characters to change to

for root, dirs, filenames in os.walk(filesdir):
    for filename in filenames:
        if old in filename:
            filepath = os.path.join(root, filename)
            os.rename(filename, filename.replace(old, new))
            print("[Done]", filepath)
