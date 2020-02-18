infile = "testfile.txt"
outfile = "out.txt"
# https://www.owasp.org/index.php?title=Testing_for_Default_or_Guessable_User_Account_(OWASP-AT-003)&setlang=es
defaultList = ["admin", "administrator", "root", "system", "guest", "operator", "super"]

class UNC:

    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile

    def createOptions(self, user, mrange=-1, caseSensitive=False):
        firstname, secondname = user.strip().split(" ")
        if caseSensitive:
            """If case sensitive is set, repeat the process for also only non capitalized input"""
            self.createOptions(user.lower(), mrange)
        options = self.applyOptionRules(firstname, secondname)
        if mrange >= 0:
            options = options + self.addNumbersToOptions(options, mrange)
        with open(self.outfile, 'a') as f:
            for username in options:
                f.write(username + "\n")

    def applyOptionRules(self, firstname, secondname):
        options = []
        options.append(firstname)
        options.append(secondname)
        options.append(firstname + secondname)
        options.append(firstname + '.' + secondname)
        options.append(firstname[0] + secondname)
        options.append(firstname[0] + '.' + secondname)
        return options

    def addNumbersToOptions(self, options, mrange):
        optionsWithNumbers = []
        for option in options:
            optionsWithNumbers = optionsWithNumbers + self.addNumbersToUsername(mrange, option)
        return optionsWithNumbers

    def addNumbersToUsername(self, mrange, username):
        numberedUsernames = []
        if mrange > 0:
            for i in range(0, mrange+1):
                print(username + str(i))
                numberedUsernames.append(username + str(i))
        return numberedUsernames

    def run(self):
        with open(self.infile, 'r') as userfile:
            for user in userfile:
                if user == "\n":
                    pass
                else:
                    self.createOptions(user, 2)


if __name__ == "__main__":
    unc = UNC(infile, outfile)
    unc.run()
