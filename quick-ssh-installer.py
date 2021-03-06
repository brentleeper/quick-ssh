import os

if os.getuid() != 0:
    print("You must install as root...exiting")
    os.system("pwd")
    exit()

print("Starting installation\n")

print("Executing the following commands:")

if not os.path.exists("/usr/local/lib/quick-ssh"):
    print("mkdir /usr/local/lib/quick-ssh")
    os.mkdir("/usr/local/lib/quick-ssh")

print("rm /usr/local/lib/quick-ssh/quick-ssh")
os.system("rm /usr/local/lib/quick-ssh/quick-ssh")
print("rm /usr/local/bin/quick-ssh")
os.system("rm /usr/local/bin/quick-ssh")
print("rm /usr/local/lib/quick-ssh-config.json")
os.system("rm /usr/local/lib/quick-ssh-config.json")

print("cp ./quick-ssh /usr/local/lib/quick-ssh/")
os.system("cp ./quick-ssh /usr/local/lib/quick-ssh/")
print("ln -s /usr/local/lib/quick-ssh/quick-ssh /usr/local/bin/")
os.system("ln -s /usr/local/lib/quick-ssh/quick-ssh /usr/local/bin/")

if not os.path.isfile(f"{os.path.expanduser('~')}/quick-ssh-config.json"):
    print("cp ./quick-ssh-config.json ~/")
    os.system("cp ./quick-ssh-config.json ~/")
else:
    print("Found existing config file, will not replace.")

print("ln -s ~/quick-ssh-config.json /usr/local/lib")
os.system("ln -s ~/quick-ssh-config.json /usr/local/lib")

print("chmod 755 /usr/local/bin/quick-ssh")
os.system("chmod 755 /usr/local/bin/quick-ssh")

print("chmod 766 ~/quick-ssh-config.json")
os.system("chmod 766 ~/quick-ssh-config.json")

print("Opening config file..")
os.system("open -a TextEdit ~/quick-ssh-config.json")

print("\nInstall complete")
