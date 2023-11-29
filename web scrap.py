import requests
from bs4 import BeautifulSoup
import csv



symbols = [ 'amzn', 'an', 'anab', 'ande', 'aneb', 'anet', 'anf', 'angh', 'angi', 'apei', 'apg', 
'apge', 'aph', 'api', 'apld', 'aple', 'aplm', 'apls', 'aplt', 'apm', 'apo', 'apog', 'app', 'appf', 'appn', 'apps', 'apre', 'apt', 'aptm', 'apto', 'aptv', 'apvo', 'apwc', 'apxi', 'apyx', 'aqb', 'aqms', 'aqn', 'aqst',  'ar', 'arav', 'aray', 'arbb', 'arbe', 'arbk', 'arc', 'arcb', 'arcc', 'arce', 'arch', 'arco', 'arct', 'ardx', 'are', 'areb', 'arec', 'aren', 'ares', 'argx', 'arhs', 'ari', 'aris', 'ariz', 'arko', 'arkr', 'arl', 'arlo', 'arlp', 'arm', 'armk', 'armp', 'aroc', 'arow', 'arqq', 'arqt', 'arr', 'arrw', 'arry', 'artl', 'artw', 'arvl', 'arvn', 'arw', 'arwr',  'asa', 'asai', 'asan', 'asb', 'asc', 'ascb', 'asgn', 'ash', 'asix', 'asle', 'asln', 'asm', 'asmb', 'asml', 'asnd', 'asns', 'aso', 'aspi', 'aspn', 'asps', 'asr', 'asrt', 'asrv', 'asst', 'astc', 'aste', 'asti', 'astl', 'astr', 'asts', 'asur', 'asx', 'asxc', 'asys', 'atai', 'atak', 'atat', 'atec', 'atek', 'aten', 'ater', 'atex', 'atge', 'atgl', 'atha', 'athe', 'athm', 'ati', 'atif', 'atip', 'atkr', 'atlc', 'atlo', 'atlx', 'atmc', 'atmu', 'atmv', 'atnf', 'atni', 'atnm', 'ato', 'atom', 'atos', 'atpc', 'atr']

url = "https://stockanalysis.com/stocks/{}/company/"
url1 = "https://stockanalysis.com/stocks/{}/"

csv_filename = "data.csv"

with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    csv_writer.writerow(['Symbol', 'Name', 'Industry', 'Sector', 'CEO', 'Price', 'Market Cap', 'Revenue', 'Volume', '52-Week Min', '52-Week Max'])

    for symbol in symbols:
        modified_url = url.format(symbol)
        response = requests.get(modified_url)
        html_content = response.content

        soup = BeautifulSoup(html_content, 'html.parser')

        # Pronalaženje podataka
        name = soup.find('div', {'class': 'text-center text-2xl font-semibold', 'data-test': 'profile-name'}).text
        industry = soup.find('td', string='Industry').find_next_sibling('td').text
        sector = soup.find('td', string='Sector').find_next_sibling('td').text
        ceo = soup.find('td', string='CEO').find_next_sibling('td').text

        modified_url1 = url1.format(symbol)
        response1 = requests.get(modified_url1)
        html_content1 = response1.content

        soup = BeautifulSoup(html_content1, 'html.parser')
        price = soup.find('div', {'class': 'text-4xl font-bold inline-block'}).text
        market_cap = soup.find('td', string='Market Cap').find_next_sibling('td').text
        revenue = soup.find('td', string='Revenue (ttm)').find_next_sibling('td').text
        volume = soup.find('td', string='Volume').find_next_sibling('td').text
        week_range = soup.find('td', string='52-Week Range').find_next_sibling('td').text
        
        min_week, max_week = map(float, week_range.split(" - "))

        

        # Pisanje podataka u CSV fajl
        csv_writer.writerow([symbol, name, industry, sector, ceo, price, market_cap, revenue, volume, min_week, max_week])

print(f"Podaci su sačuvani u {csv_filename}.")
