import urllib2, csv
#https://docs.python.org/2/library/urllib2.html
from bs4 import BeautifulSoup
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/

output_file = open('Firstattempt.csv', 'w')
writer = csv.writer(output_file)

url = 'https://www.mshp.dps.missouri.gov/HP68/search.jsp'

html = urllib2.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

crash_table = soup.find('table', {'class': 'accidentOutput'})

row_list = crash_table.find_all('tr')

for row in row_list:
	cell_list = row.find_all('td')
	data = [cell.text.encode('utf-8').strip() for cell in cell_list]

	writer.writerow(data)
	
	
	# AHHHHH FINALLY 
