import requests
import re
import pyfiglet
import termcolor
#import modules...
p = pyfiglet.figlet_format("BLACK\nROBOT")
print(termcolor.colored(p, color = "green"))
c = "BY MOSTAFA ELGERDAWI"
print(termcolor.colored(c, color = "red"))

d = termcolor.colored("Enter Domain ===>> ", color = "yellow")
domain = input(d)
#vairable to get web domain

full_domain = domain+"/robots.txt"
#vairable to get web domain + robots file

page = requests.get(full_domain, 'html.parser').text
#vairable to store web contain by html in text

hidness = re.findall("Disallow\: \S{1,}", page)
#vairable to find all disallowed files in site

if len(hidness) > 0:     #if hidness(list) contain bigger than 0 so its found disallowed files  
    for i in hidness:    #loop in list to get files beatiful 
        link = "[+] "+domain+i[10:]  #vairable to store domain and disallow file in one path
        k = ("#"*20)
        print(termcolor.colored(k, color = "red"))
        print(termcolor.colored(link, color = "green"))                  #print(vairable)

else:
    print(termcolor.colored("[-]nothing found", color = "yellow"))       #if hidness(list) contain smaller than 0 so its not found disallowed files