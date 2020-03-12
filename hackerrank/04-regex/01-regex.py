import re
import sys

def matchStr(test_string, pattern):
    match = re.match(regex_pattern, test_string) is not None    
    if match:        
        comp = re.compile(pattern)
        return match, comp.search(test_string).groups()
    else:
        return match, ""

# The dot (.) matches anything (except for a newline).
# test_string = "123.def.Ecf.dld"
# regex_pattern = r"...\....\....\....$"	# Do not delete 'r'.
# print("dot:")
# matchStr(test_string, regex_pattern)

# # The expression \d matches any digit [0-9].
# # The expression \D matches any character that is not a digit.
# test_string = "10a10.2015452254"
# regex_pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.
# print("\d\D:")
# matchStr(test_string, regex_pattern)

# \s matches any whitespace character [ \r\n\t\f ].
# \S matches any non-white space character.
# test_string = "12 11 15"
# regex_pattern = r"\S\S\s\S\S\s\S\S"	# Do not delete 'r'.
# print("\s:") 
# matchStr(test_string, regex_pattern)

# The expression \w will match any word character. alphanumeric and underscore
# \W matches any non-word character.
# test_string = "12 11 15"
# regex_pattern = r"\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"	# Do not delete 'r'.
# print("\w:") 
# matchStr(test_string, regex_pattern)

# The ^ symbol matches the position at the start of a string.
# The $ symbol matches the position at the end of a string.
# test_string = "1abcs."
# regex_pattern = r"^\d\w\w\w\w\.$"	# Do not delete 'r'.
# print("\w:") 
# matchStr(test_string, regex_pattern)

# \b assert position at a word boundary.
# test_string = "aaAcat"
# regex_pattern = r"\b[aeiouAEIOU][a-zA-Z]*\b"	# Do not delete 'r'.
# print("\\b:")
# matchStr(test_string, regex_pattern)

# Parenthesis ( ) around a regular expression can group that part of regex together. This allows us to apply different quantifiers to that group.
# (?: ) can be used to create a non-capturing group. It is useful if we do not need the group to capture its match.
# test_string = "okokok! cya"
# regex_pattern = r"(okokok)(.*)?"	# Do not delete 'r'.
# print("()?:")
# matchStr(test_string, regex_pattern)

# Alternations, denoted by the | character, match a single item out of several possible items separated by the vertical bar. 
# test_string = "Mrs.Mourisca"
# regex_pattern = r"^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)([a-z|A-Z]+)$"	# Do not delete 'r'.
# matchStr(test_string, regex_pattern)

# Valid coordinates
# coordsDic = dict()

# coordsDic = {
#     "(-127, -48)": False, 
#     "(+90.0, -147.45)": True, 
#     "(+91.0, -147.45)": False,
#     "(75, 180)": True
# }

# for coord, val in coordsDic.items():
#     # regex_pattern = r"^\(-?[0-180](\.\d+)?,-?[0-180](\.\d+)?\)$"
#     regex_pattern = r"^\((-|\+)?(([0-9]|[1-8][0-9])(\.\d+)?|90(\.0+)?)?(,)(\s)?(-|\+)?(([0-9]{1,2}|1[0-7][0-9])(\.\d+)?|180(\.0+)?)\)$"
#     res, matchG = matchStr(coord, regex_pattern)
#     if val == res:
#         print("Passed")
#     else: 
#         print("Failed. Coord: ", coord)

# input = ["I love #hackerrank", "I just scored 27 points in the Picking Cards challenge on #HackerRank", 
# "I just signed up for summer cup @hackerrank", "interesting talk by hari, co-founder of hackerrank"]

# regex_pattern = r"(?i)(.*)hackerrank(.*)" # (?i) makes the search case insensitive
# for i in input:
#     print(matchStr(i, regex_pattern))

# regex_pattern = r"(?i)<h3><a\s+href=\"/questions/(\d+)/.+?\" class=\"question-hyperlink\">(.+?)</a></h3>.+?<span\s+title=\".+?\"\s+class=\"relativetime\">(.+?)</span>"
# # regex_pattern = r"<div\s+class=\"question-summary\"\s+id=\"question-summary-(\d+)\">.+?</div>"

# with open("/home/juliana/Starticket/Playground/Python101/hackerrank/04-regex/htmlinput.html", 'r') as file:
#     test_string = " ".join([x.strip() for x in file]) 


# # print(test_string)
# allMatched = re.findall(regex_pattern, test_string)
# for str in allMatched:
#     print(';'.join(str))


# inputs = ["u4474671BMSZSACKXPLYEUZSURELG", 
#             "juBa1527ZNXUBYXXEYOQCXEPDQZMZODZA",
#             "17258902ZDNOVGDQWWXEYLANVDI",
#             "832",
#             "911FXYBFHJWUUAHSFTLQEUCJFLAEOSPO",
#             "Tks549572163",
#             "Hfvx47MUPXRMTIIQMUVG",
#             "54481486LFPXKYCNDLWBLQAP",
#             "E327UYBLRKWHUSBKXBUHPBP",
#             "lr08762PUXOPAZMFZSVGLLQUDAHLSMNEO",
#             "SND71QZXC",
#             "305BJAZWADPIDVDEHHZJIMKKBJC",
#             "odfw6980BRKAWPHKMZWNHZDZLMYRZVXSKHPW"]
# regex_pattern = r"[a-z]{0,3}\d{2,8}[A-Z]{3}"

# for i in inputs:
#     if re.match(regex_pattern, i):
#         print("VALID")
#     else:
#         print("INVALID")

inputs = ['<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>',
        '<a href="http://www.hackerrank.com"><h1><b>HackerRank</b></h1></a>',
        '<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>',
        '<li class="interwiki-simple"><a href="//simple.wikipedia.org/wiki/" title="" lang="simple" hreflang="simple">Simple English</a></li>',
        '<li class="interwiki-eo"><a href="//eo.wikipedia.org/wiki/" title="" lang="eo" hreflang="eo">Esperanto</a></li>',
        '<div class="portal" role="navigation" id="p-lang"><li class="interwiki-bg"><a href="//bg.wikipedia.org/wiki/" title="" lang="bg" hreflang="bg"></a></li></div>']

total = len(inputs)

regex_pattern = r"<a href=\"(.*?)\".*?>([\w ,./]*)(?=</)"

while total > 0:
    i = inputs[total - 1]
    allMatched = re.findall(regex_pattern, i)
    for a in allMatched:
        print(','.join(a))
    total -= 1