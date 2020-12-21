import json
import csv
creds = []
with open("spotify.txt", 'r') as login_file:
    lines = login_file.readlines()
    for line in lines:
        colon_pos = 0
        for character in line:
            if character == ":":
                break
            else:
                colon_pos+=1
        usern = line[:colon_pos].rstrip()
        passwd = line[colon_pos+1:].rstrip()
        stripped_pass = passwd.split(" ", 1)[0]
        creds.append({'uname':usern,'passwd':stripped_pass})

with open("spotify.csv", "w", newline='') as login_csv:
    head = ['uname', 'passwd']
    writer = csv.DictWriter(login_csv, fieldnames=head)
    writer.writeheader()
    for cred in creds:
        writer.writerow(cred)