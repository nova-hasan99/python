import math, os, sys, datetime, random, subprocess, hashlib

print(math.sqrt(16))              # see square root
print(os.getcwd())                # see own device many directory informatoin
print(sys.version)                # see python current version
print(datetime.datetime.now())    # see current time
print(random.randint(1, 10))      # generate random number

version = subprocess.run(         # version check
    [
        'python', '--version',
        # 'php', '--version',
        # 'node', '--version',
    ],
    capture_output = True,
    text = True
)
print(version.stdout)

print('.......................has password...................')

password = b'Hasan553565'
hass_pass = hashlib.md5(password)
print(hass_pass.hexdigest())