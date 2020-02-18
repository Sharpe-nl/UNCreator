# User Name Creator (UNC)
This is a small script that creates possible usernames from a firstname and a secondname.
It can be used for pentesting purposes when only firstname and secondnames can be found and you want to bruteforce usernames.
**Please use this only for professional or education purposes**

## Usage
Make sure you have a file containing a list of first and secondnames separated by a space. (See [example_input.txt](example_input.txt))

Now simply run the following command:
```
python unc.py -i example_input.txt -o example_output.txt
```

## Help
```
Usage: unc.py -i inputfile [-oncs]

Options:
  -h, --help            show this help message and exit
  -i INFILE, --inputfile=INFILE
                        Specify a file containing a list of first and second
                        names (e.g. John Doe)
  -o OUTFILE, --outputfile=OUTFILE
                        Specify an outputfile, otherwise a custom name will be
                        created
  -n NUMBERADD, --numberadd=NUMBERADD
                        Additionally create usernames with appended number,
                        default is no number
  -c, --casesensitive   Use this if you want case sensitivity activated, this
                        will result in a list that is two times the size,
                        default=False
  -s, --specialchars    Use this if you want special chars in names e.g. a=@
```

## More Info
I will also work on a script creating correstponding passwords later on. This would be quite similar
