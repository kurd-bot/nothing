import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
    import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support this Tools")
    print(' Join Over Facebook Group For Any Help 😍 ')
    from AKING import login
    login()
elif bit == '32bit':
    print("\x1b[1;91m Sorry ! Your Device Support Not this Tools")
    print(' Join Over Facebook Group For Any Help 😍 ')
    exit()