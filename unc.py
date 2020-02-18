import optparse
import time

class UNC:

    def __init__(self, infile, outfile, numberadd, casesense):
        self.infile = infile
        self.outfile = outfile
        self.numberadd = numberadd
        self.casesense = casesense
        # https://www.owasp.org/index.php?title=Testing_for_Default_or_Guessable_User_Account_(OWASP-AT-003)&setlang=es
        self.defaultList = ["admin", "administrator", "root", "system", "guest", "operator", "super"]

    def createOptions(self, user):
        firstname, secondname = user.strip().split(" ")
        if self.casesense:
            """If case sensitive is set, repeat the process for also only non capitalized input"""
            self.casesense = False
            self.createOptions(user.lower())
        options = self.applyOptionRules(firstname, secondname)
        if self.numberadd >= 0:
            options = options + self.addNumbersToOptions(options, self.numberadd)
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
        options.append(secondname + firstname)
        options.append(secondname + firstname[0])
        options.append(secondname[0] + firstname)

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
                    self.createOptions(user)


def main():
    infile = "testfile.txt"
    outfile = "out.txt"

    parser = optparse.OptionParser(usage='usage: '+__file__+ ' -i inputfile ')
    parser.add_option('-i', '--inputfile', dest='infile', type='string', help='Specify a file containing a list of first and second names (e.g. John Doe')
    parser.add_option('-o', '--outputfile', dest='outfile', type='string', help='Specify an outputfile, otherwise a custom name will be created')
    parser.add_option('-n', '--numberadd', dest='numberadd', type='string', help='Additionally create usernames with appended number, default is no number')
    parser.add_option('-c', '--casesensitive', dest='casesense', action="store_true", default=False, help='State \"True\" if you want case sensitivity activated, this will result in a list that is two times the size, default=False')

    (options, args) = parser.parse_args()
    if options.infile == None:
        print('[-] No inputfile specified')
        print(parser.usage())
        exit(0)
    if options.outfile == None:
        outfile = "usernames_" + time.strftime("%Y%m%d-%H%M%S")
        print('[-] No outputfile specified, creating default file {}'.format(outfile))
    else:
        outfile = options.outfile
    if options.numberadd == None:
        numberadd = -1
    else:
        numberadd = int(options.numberadd)

    print('[+] Starting creating username file')
    unc = UNC(options.infile, outfile, numberadd, options.casesense)
    unc.run()
    print('[+] List creation finished: {}'.format(outfile))

if __name__ == "__main__":
    main()