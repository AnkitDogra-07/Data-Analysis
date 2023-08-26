import os 
import pandas as pd
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

ua = UserAgent()
user_agent = ua.random

url = "https://www.football-data.co.uk/englandm.php"
base_url = "https://www.football-data.co.uk"

download_folder = r"C:\Users\ankit\OneDrive\Desktop\Data Analysis\Football-CSV"

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

headers = {"User-Agent": user_agent}
response = requests.get(url, headers = headers,  verify=True)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    seasons = soup.find_all('h2', string=lambda string: string and string.startswith('Season'))
    
    for season in seasons:
        season_year = season.text.split(' ')[-1]
        season_data = season.find_next_sibling('ul')

        links = season_data.find_all('a')

        csv_links = [link.get('href') for link in links if link.get('href').endswith('.csv')]

        for csv_link in csv_links:
            full_csv_url = base_url + csv_link

            file_name = f"{season_year}_{os.path.basename(csv_link).split('.')[0]}.csv"

            file_path = os.path.join(download_folder, file_name)
            
            print(f"Full CSV URL: {full_csv_url}")
            print(f"File Path: {file_path}")

            csv_data = requests.get(full_csv_url).content

            with open(file_path, 'wb') as file:
                file.write(csv_data)

            # Print a message indicating that the CSV file has been downloaded
            print(f"Downloaded CSV file: {file_name}")
else:
    print(f"Failed to retrieve the URL. Status code: {response.status_code}")