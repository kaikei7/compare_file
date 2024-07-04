import filecmp

# notice the two backslashes
File1 = str(input("file1:"))
File2 = str(input("file2:"))

def compare_files(File1,File2):
   compare = filecmp.cmp(File1,File2)
   
   if compare == True:
      print("The two files are the same.")
   else:
      print("The two files are different.")
      
compare_files(File1,File2)