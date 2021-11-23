#!/usr/local/bin/python3

cracked_hashes = open("/Users/bortiz/Documents/Projects/cerner/external/northamerica/part_cracked_hashes.txt", "r")
ntds_hashes = open("/Users/bortiz/Documents/Projects/cerner/external/northamerica/ntds", "r")

sorted_creds = open("/Users/bortiz/Documents/Projects/cerner/external/northamerica/sorted_creds.txt", "w")

creds = []

class User:
    def __init__(self, hash, username):
        self.hash = hash
        self.username = username
        self.password = ""

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password
    def get_username(self):
        return self.username
    def get_hash(self):
        return self.hash


for line in ntds_hashes.readlines():
    try:
        if "status=Enabled" in line:
            hash = line.split(":")[3]
            username = line.split(":")[0].split("\\")[1]
            new_user = User(hash, username)
            creds.append(new_user)
    except Exception as e:
        if e == "list index out of range":
            continue

for line in cracked_hashes.readlines():
    for user in creds:
        if user.get_hash() == line.split(":")[0]:
            user.set_password(line.split(":")[1])

for user in creds:
    if user.get_password():
        sorted_creds.write(user.get_username() + ":" + user.get_password())

