import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations 64bit")
    from AKING import login
    login()
elif bit == '32bit':
    print("\n\x1b[1;92m Congratulations 32bit")
    from AKING32 import login
    login()
else:
    print('[×] Connection Error')
    exit()
