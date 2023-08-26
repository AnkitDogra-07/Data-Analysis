import os
from bs4 import BeautifulSoup
import requests
from datetime import datetime  # Import datetime for timestamp

url = "https://www.football-data.co.uk/englandm.php"

download_folder = r"C:\Users\ankit\OneDrive\Desktop\Data Analysis\Football-CSV"

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all('a')
    
    csv_links = [link.get('href') for link in links if link.get('href').endswith('.csv')]
    
    for csv_link in csv_links:
        full_csv_url = url + csv_link
        
        # Generate a unique file name using a timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"{os.path.basename(csv_link).split('.')[0]}_{timestamp}.csv"
        
        file_path = os.path.join(download_folder, file_name)
        
        csv_data = requests.get(full_csv_url).content
        
        with open(file_path, 'wb') as file:
            file.write(csv_data)

        # Print a message indicating that the CSV file has been downloaded
        print(f"Downloaded CSV file: {file_name}")
else:
    print(f"Failed to retrieve the URL. Status code: {response.status_code}")
