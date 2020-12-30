Awk is a programming language for information retrieval and data manipulation.
Awk is a programming language that allows many tasks of information retrieval, processing, and report generation to be specified simply.
An awk program is a sequence of pattern-action statements that searches a set of files for lines matching any  the specified patterns and executes the action associated with each matching pattern

  Syntax-1 : awk ’pattern { action }’ <file1,file2...>          EX : $1 == "address" { print $2, $3 }
  Either the pattern or the action in a pattern-action statement may be omitted.
  Since patterns and actions are both optional, actions are enclosed in braces to distinguish them from patterns.
  If there is no action with a pattern, as in  $1 == "name" the matching line is printed.
  If there is no pattern with an action, as in { print $1, $2 } then the action is performed for every input line.
  If no files are mentioned on the command line, the awk interpreter will read the standard input
  The pattern-action statements are enclosed in single quotes. This protects characters like $ from being interpreted by the shell and also allows the program to be longer than one line.

  Syntax-2 : awk -f <program_file> <file1,file2...>                   Ex : awk -f myprogram myfile
  If the program is long, it is often more convenient to put it into a separate file, say myprogram, and use the -f option to fetch it:

FIELDS :
===========
splits each line into a sequence of fields, where, by default, a field is a string of non-blank, non-tab characters.
Fields are normally separated by sequences of blanks and/or tabs determined by the field separator .
When printed, items separated by a comma in the print statement are separated by the output field separator, which by default is a single blank.
Each line printed is terminated by the output record separator, which by default is a newline.

-> awk '{print}' countrues.txt
-> awk '{print $1,$2}' countries.txt
-> awk '{ printf "%10s %6d\n", $1, $3 }' countries.txt -> Print formatting
   With printf, no output separators or newlines are produced automatically; you must create them yourself, which is the purpose of the \n in the format specification .

BEGIN and END :
================
There are two special patterns, BEGIN and END, that ‘‘match’’ before the first input line has been read and after the last input line has been processed.
The special pattern BEGIN matches before the first input record is read, so any statements in the action part of a BEGIN are done once before awk starts to read its first input file.
The pattern END matches the end of the input, after the last file has been processed.
BEGIN and END provide a way to gain control for initialization and wrapup.

This program uses BEGIN to print a title:
    BEGIN { print "Countries of Asia:" }
    /Asia/ { print " ", $1 }
    END {print "End of print.."}

EXAMPLES :
===============
Print last field of each input line:                         { print $NF }
Print 10th input line:                                       NR == 10
Print last input line:                                       { line = $0} END { print line }
Print input lines that don’t have 4 fields:                  NF != 4 { print $0, "does not have 4 fields" }
Print input lines with more than 4 fields:                   NF > 4
Print input lines with last field more than 4:               $NF > 4
Print total number of input lines:                           END { print NR }
Print total number of fields:                                { nf = nf + NF } END { print nf }
Print total number of input characters:                      { nc = nc + length($0) } END { print nc + NR }
Print the total number of lines that contain Asia:           /Asia/ { nlines++ } END { print nlines }
                                                             ( The statement nlines++ has the same effect as nlines = nlines + 1.)

Relational  comparison, if both operands are numeric, a numeric comparison is made; otherwise the operands are compared as strings.
$3>100        selects lines where the third field exceeds 100, and
$1 >= "S"     selects lines that begin with an S, T, U, etc.,

To restrict the match to a specific field, use the matching operators ~ (for matches) and !~ (for does not match):
$4 ~ /Asia/ { print $1 }      prints the first field of all lines in which the fourth field matches Asia, while
$4 !~ /Asia/ { print $1 }     prints the first field of all lines in which the fourth field does not match Asia.

REGEX :
===========
In regular expressions the symbols : \ ^ $ . [] * + ? () |  have special meanings and are called METACHARACTERS .
To turn off the special meaning of a metacharacter, precede it by a \ (backslash).
Thus, the program   /a\$/   will print all lines containing an a followed by a dollar sign.

            ^ -> Match the beginning
            $ -> Match the end
            . -> Matches any single character  --> /^.$/ will match all lines that contain exactly one character.
            * -> Matches 0 or more             --> r* zero or more r’s
            + -> Matches 1 or more             --> r+ one or more r’s
            ? -> Matches 0 or 1                --> r? zero or one r
        (a|b) -> Matches a or b                --> Parentheses () are used for grouping and | is used for alternatives
          {3} -> Matches Exactly 3
         {3,} -> Matches 3 or more
        {3,5} -> Matches 3, 4 or 5
        [ABC] -> Matches lines containing any one of A, B or C anywhere
     [a-zA-Z] -> Matches any single letter
    [^a-zA-Z] -> Matches any non-letter (a ^ in [] denotes not matching)
        [0-7] -> Matches Digit from 0 to 7

           \b -> Matches backspace
           \f -> Matches formfeed
           \n -> Matches newline
           \r -> Matches -> Matches -> Matches carriage return
           \t -> Matches -> Matches tab
         \ddd -> Matches octal value ddd
           \" -> Matches quotation mark

    [:upper:] -> Matches Upper case letters
    [:lower:] -> Matches Lower case letters
    [:alpha:] -> Matches All letters
    [:alnum:] -> Matches Digits and letters
    [:digit:] -> Matches Digits
   [:xdigit:] -> Matches Hexadecimal digits
    [:punct:] -> Matches -> Matches Punctuation
    [:blank:] -> Matches Space and tab
    [:space:] -> Matches Blank characters
    [:cntrl:] -> Matches Control characters
    [:graph:] -> Matches -> Matches Printed characters
    [:print:] -> Matches Printed characters and spaces
     [:word:] -> Matches Digits, letters and underscore

BUILT-IN VARIABLES :
=======================
______________________________________________________
VARIABLE        MEANING
______________________________________________________
    ARGC        number of command-line arguments
    ARGV        array of command-line arguments
FILENAME        name of current input file
     FNR        record number in current file
      FS        input field separator
      NF        number of fields in current record
      NR        number of records read so far
    OFMT        output format for numbers
     OFS        output field separator
     ORS        output record separator
      RS        input record separator
______________________________________________________

STRING FUNCTIONS :
===================
{ print NR ":" $0 }  -> To concatnate variables and strings.
In this table :
r represents a regular expression (either as a string or as /r/), s and t string expressions, and n and p integers.
________________________________________________________________________________
              FUNCTION DESCRIPTION
________________________________________________________________________________
             gsub(r,s) substitute s for r globally in current record, return number of substitutions
           gsub(r,s,t) substitute s for r globally in string t, return number of substitutions -> gsub("Dileep","dil",$0) == replace dil with Dileep in $0
            index(s,t) return position of string t in s, 0 if not present
                length return length of $0
             length(s) return length of s
            split(s,a) split s into array a on FS, return number of fields
          split(s,a,r) split s into array a on regular expression r, return number of fields
sprintf(fmt,expr-list) return expr-list formatted according to format string fmt
              sub(r,s) substitute s for first r in current record, return number of substitutions
            sub(r,s,t) substitute s for first r in t, return number of substitutions
           substr(s,p) return suffix of s starting at position p
         substr(s,p,n) return substring of s of length n starting at position p
________________________________________________________________

FUNCTIONS :
==============
func name(argument-list) {
statements
}

FILE REDIRECTION :
====================
It is possible to print output into files instead of to the standard output. The following program
invoked on the file countries will print all lines where the population (third field) is bigger than 100
into a file called bigpop, and all other lines into smallpop:

$3 > 100 { print $1, $3 >"bigpop" }
$3 <= 100 { print $1, $3 >"smallpop" }

Notice that the filenames have to be quoted; without quotes, bigpop and smallpop are merely uninitialized variables. It is important to note that the files are opened once; each successive print or printf
statement adds more data to the corresponding file. If >> is used instead of >, output is appended to the file
rather than overwriting its original contents


GETLINE :
============
The function getline can be used to read input either from the current input or from a file or pipe, by redirection analogous to printf.
By itself, getline fetches the next input record and performs the
normal field-splitting operations on it. It sets NF, NR, and FNR.
getline returns 1 if there was a record present, 0 if the end-of-file was encountered, and -1 if some error occurred (such as failure to open a file).

It is also possible to pipe the output of another command directly into getline.
while ("who" | getline) ; n++
executes who and pipes its output into getline.
Each iteration of the while loop reads one more line and increments the variable n, so after the while loop terminates, n contains a count of the number of users.

COMMAND LINE ARGUMENTS :
==========================
The command-line arguments are available to an awk program: the array ARGV contains the elements
ARGV[0], ..., ARGV[ARGC-1]; as in C, ARGC is the count. ARGV[0] is the name of the program (generally awk); the remaining arguments are whatever was provided (excluding the program and any optional
arguments)
