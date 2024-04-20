# your code goes here!

import re

class EmailAddressParser:

    
    def __init__(self, string):
        self.string = string

    def parse(self):
        pattern = r'\b[A-Za-z][A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,3}\b'
        email_regex = re.compile(pattern)            
        match_split = email_regex.findall(self.string)
        match_split.sort()

        return match_split
        
    
# addresses = "talk@talk.com john.jones@flatironschool.com alexa@amazon.com"

# parser = EmailAddressParser("talk@talk.com, what john.jones@flatironschool.com, who alexa@amazon.com, where when why")
# print(parser.parse())
# # assert(parser.parse() == ["alexa@amazon.com", "john.jones@flatironschool.com", "talk@talk.com"])
# # print(EmailAddressParser(addresses).parse())