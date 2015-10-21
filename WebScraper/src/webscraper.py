# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "czepeda"
__date__ = "$Oct 20, 2015 7:58:50 PM$"

from bs4 import BeautifulSoup
import urllib2

f = open('C:\Users\czepeda\Desktop/outfile.txt', 'w')
errorFile = open('C:\Users\czepeda\Desktop/errorespn.txt', 'w')

x = 0
while (x < 500):
    soup = BeautifulSoup(urllib2.urlopen('http://games.espn.go.com/ffl/tools/projections?&startIndex=' + str(x)).read(), "html.parser")
    tableStats = soup.find("table", {"class": "playerTableTable tableBody"})
    for row in tableStats.findAll('tr')[2:]:
        col = row.findAll('td')
        try:
            name = col[0].a.string.strip()
            f.write(name + '\n')
   
        except Exception as e:
            errorFile.write (str(x) + '*******' + str(e) + '*******' + str(col) + '\n')
            pass

    x = x + 40

f.close()
errorFile.close