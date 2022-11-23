class Employee:
    company = "facebook"
    ecode = 120

class FreeLancer:
    company = "youtube"
    level = 0
    def upgradeLevel(self):
        self.level = self.level + 1

class programmer(FreeLancer,Employee):
    name = "Prabhat"

p = programmer()
p.upgradeLevel()
print(p.company)
print(p.level)