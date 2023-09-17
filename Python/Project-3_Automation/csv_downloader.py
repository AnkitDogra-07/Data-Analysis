import os
from bs4 import BeautifulSoup
import requests
from datetime import datetime  # Import datetime for timestamp

url = "https://www.football-data.co.uk/englandm.php"

download_folder = r"C:\\Users\\ankit\\OneDrive\\Desktop\\Dev\\Data-Analysis\\Python\\Project-3_Automation\\Football-CSV"

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all('a')
    seasons = soup.find_all('i')
    new_seasons = []
    
    for i in seasons:
        new_seasons.append(str(i))
        
    final_seasons = []     
    for i in new_seasons:
        final_seasons.append(i[10:-4]) 
        
    csv_links = [link.get('href') for link in links if link.get('href').endswith('.csv')]
    
    for season_name , csv_link in zip(final_seasons, csv_links):
        full_csv_url = url + csv_link
        
        # Generate a unique file name using a timestamp
        
        file_name = f"{season_name}_{os.path.basename(csv_link).split('.')[0]}.csv"
        
        file_path = os.path.join(download_folder, file_name)
        
        csv_data = requests.get(full_csv_url).content
        
        with open(file_path, 'wb') as file:
            file.write(csv_data)

        # Print a message indicating that the CSV file has been downloaded
        print(f"Downloaded CSV file: {file_name}")
else:
    print(f"Failed to retrieve the URL. Status code: {response.status_code}")
