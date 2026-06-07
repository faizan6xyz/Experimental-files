x = open("eg.csv", "r") # r = read mode 
lines = x.read()
print(lines)
x.close()
file = open("eg.csv", "w")  # w = write mode
file.write("Hello, this is my first file!\n")
file.write("Learning Python file handling.")
file.close()
file = open("eg.csv", "a")  # a = append mode
file.write("\nThis line is added later.")
file.close()


'''
"r+"	Read + Write (no overwrite initially)
"w+"	Write + Read (overwrites file first)
"a+"	Append + Read (adds + can read)
"rt"	Read text
"wt"	Write text
"rb"	Read binary
"wb"	Write binary
"ab"	Append binary
"rb+"	Read + Write binary
"wb+"	Write + Read binary (overwrite)
"ab+"	Append + Read binary
'''