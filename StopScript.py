import os

dir = "C:\Program Files\Bitcoin\daemon"
os.chdir(dir)

os.system("bitcoin-cli stop")