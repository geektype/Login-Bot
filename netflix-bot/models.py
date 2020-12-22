import csv
class Credential(object):
    def __init__(self, uname, passwd):
        self._uname = uname
        self._passwd = passwd
    @property
    def uname(self):
        return self._uname 
    @property
    def passwd(self):
        return self._passwd
    @classmethod
    def from_csv(self, file_name = "netflix.csv"):
        creds = []
        cred_objects = []
        with open(file_name, "r") as login_csv:
            rows = csv.DictReader(login_csv)
            creds = list(rows)
        for cred in creds:
            cred_objects.append(Credential(cred['uname'], cred['passwd']))
        return cred_objects