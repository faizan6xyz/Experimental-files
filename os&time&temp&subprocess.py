# Shows where Python is currently working
import os , subprocess , time , tempfile 
from pathlib import Path
print(os.getcwd())
# Change Directory
os.chdir("C:\\Users\\faiza\\Desktop")
# List Files & Folders
print(os.listdir())
# List Files & Folders in Specific folder:
print(os.listdir("C:\\Users\\faiza\\Desktop"))
# Create Folder
os.mkdir("new_folder")
# Create nested folders:
os.makedirs("parent/child")
# Remove Folder
os.rmdir("new_folder")
#  Remove nested:
os.removedirs("parent/child")
# Rename File / Folder
os.rename("old.txt", "new.txt")
# replace the file 
os.replace("old.txt", "new.txt")
# Delete File
os.remove("file.txt")
# Check if File Exists
os.path.exists("file.txt")
# Join Paths (VERY IMPORTANT 🔥)
Path("folder") / "file.txt" 
# Get File Info
print(os.path.getsize("file.txt"))   # size
print(os.path.isfile("file.txt"))    # is file?
print(os.path.isdir("folder"))       # is folder?
# Environment Variables
print(os.environ)
print(os.environ.get("PATH"))
# Get File Path of Script
print(os.path.dirname(__file__))
# Walk through directories ( Recursively goes through all folders ) 
for root, dirs, files in os.walk("C:\\Users\\faiza\\Desktop"):
    print("Folder:", root)
    print("Subfolders:", dirs)
    print("Files:", files)
# Get absolute path ( Converts relative → full path )
print(os.path.abspath("student.csv"))
# Get file name & extension
file = "student.csv"
print(os.path.basename(file))   # student.csv
print(os.path.splitext(file))   # ('student', '.csv')
# Get parent directory
path = "C:\\Users\\faiza\\Desktop\\python\\file.txt"
print(os.path.dirname(path))
# Check permissions
print(os.access("file.txt", os.R_OK))  # Read permission
print(os.access("file.txt", os.W_OK))  # Write permission
# Get OS name
print(os.name)
# Get environment variable
print(os.getenv("USERNAME"))
# Create empty file
open("newfile.txt", "w").close()
# Change file permissions in window Make file read-only
os.chmod("file.txt", 0o444)
# Change file permissions in window Make file writable again
os.chmod("file.txt", 0o666)
# Get file stats
info = os.stat("file.txt")
print(info.st_size)   # size
print(info.st_mtime)  # last modified time
# Safe file handling (try/except)
try:
    os.remove("file.txt")
except FileNotFoundError:
    print("File not found")
# Check current script path
print(os.path.realpath(__file__))
# Create temp directory
os.mkdir("temp")
os.chdir("temp")
# Copy environment variables
env_copy = dict(os.environ)
print(env_copy)
# os.scandir() (faster and gives more info than listdir) Returns DirEntry objects(special object that represents one item inside a directory) not just names
with os.scandir(".") as entries:
    for entry in entries:
        print(entry.name, entry.is_file(), entry.is_dir())
# Safe path handling (os.path deep dive)
# Normalize path ( This function cleans and simplifies a file path)
os.path.normpath("folder//subfolder/../file.txt")
#  Check same file (Checks if both paths point to same file )
os.path.samefile("file1.txt", "file2.txt")
#  Split path
path = "C:\\Users\\faiza\\file.txt"
print(os.path.split(path))   # split() → (folder, file)
print(os.path.dirname(path))  # dirname() → folder
print(os.path.basename(path)) # basename() → file
#  Process-related functions
#  Get process ID of current running ppython program
print(os.getpid()) 
# Kill process kills the program by id (pid)
pid = 1223 
os.kill(pid, 9)
#  File descriptor operations (low-level) : its just a number that represents an open file
fd = os.open("file.txt", os.O_CREAT | os.O_WRONLY) # os.O_CREAT : Create the file if it doesn’t exist , os.O_WRONLY : Open file in write-only mode
os.write(fd, b"Hello")
os.close(fd)
#  Change file timestamps : it changes Access time , Modification time . its  Useful for: file syncing , cache systems
import time
os.utime("file.txt", (time.time(), time.time()))
#  Working with bytes paths : Useful for special encoding cases
os.listdir(b".")
#  Environment manipulation (temporary)
# Set variable 
os.environ["MY_VAR"] = "Hello"
# Platform-specific behavior
if os.name == "nt":
    print("Windows")
else:
    print("Linux/Mac") 
# Gives the logged-in username 
print(os.getlogin())
# Number of CPU cores
print(os.cpu_count())
# Gives home director
print(os.path.expanduser("~"))
# shows the path separator
print(os.sep)  
# shows the line seprator 
print(os.linesep)
# converts the timestamp to human readable text 
print(time.ctime(os.path.getmtime("file.txt")))
# delay execution 
time.sleep(2)
print("Hello after 2 seconds")
# human readable time 
print(time.ctime())
#  current time
print(time.time())
# Run System Command
subprocess.run(["dir"], shell=True) # dir is windows command to Display the list of files and folders in a directory . shell true means un through the shell command 
# Execute Python file
subprocess.run(["python", "student1.py"])
# run command and Capture output
result = subprocess.run(
    ["echo", "Hello"],
    capture_output=True,
    text=True
)
print(result.stdout)
#  Temporary files & directories ( provides safe temperory storage used for caching and intermediate files )
temp_dir = tempfile.gettempdir()
print(temp_dir)
# read write and close a temp file 
temp = tempfile.TemporaryFile()
temp.write(b"Hello World")
temp.seek(0)
print(temp.read())
temp.close()
# Named Temporary File
with tempfile.NamedTemporaryFile(delete=True) as f:
    print(f.name)
    f.write(b"Data")
# Temporary Directory
with tempfile.TemporaryDirectory() as temp_dir:
    print("Temp folder:", temp_dir)
# handle error 
try:
    subprocess.run(["wrong_command"], check=True)
except subprocess.CalledProcessError:
    print("Command failed!")
# multiple command 
subprocess.run("echo Hello","dir", shell=True)
# get system info 
result = subprocess.run(["ipconfig"], capture_output=True, text=True)
print(result.stdout)
# use popen : Process Open - start a new process and interact with it while it is running
process = subprocess.Popen(
    ["ping", "google.com"],
    stdout=subprocess.PIPE,
    text=True
)
for line in process.stdout:
    print(line.strip())
# keep the file after closing 
f = tempfile.NamedTemporaryFile(delete=False)
print(f.name)
f.write(b"Keep this file shit")
f.close()
# create multiple file in temp directory 
with tempfile.TemporaryDirectory() as d:
    for i in range(3):
        path = os.path.join(d, f"file{i}.txt")
        with open(path, "w") as f:
            f.write( "data")
    print("Files created in:", d)
# SpooledTemporaryFile : Stores in memory → moves to disk if large
f = tempfile.SpooledTemporaryFile(max_size=100)

f.write(b"Small data")
f.seek(0)
print(f.read())
# kill a process 
p = subprocess.Popen(["notepad.exe"])
p.terminate()   
# directly get output 
output = subprocess.check_output(["echo", "Hello"], text=True)
print(output)
# pipes : connect processes
p1 = subprocess.Popen(["echo", "Hello"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["findstr", "H"], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
output = p2.communicate()[0]
print(output)
# get local time and GMT
print("Local:", time.localtime())
print("GMT:", time.gmtime())
# format time 
t = time.localtime()
formatted = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted)