# Import libraries
import pandas as pd
import requests
import json
import time
from datetime import datetime


# Settings to run once
url = "https://apps.unive.it/sitows/index/personebiblioteche"
biblioteche = ['CFZ','BEC','BAS','BAUM']
data = [['timestamp','biblioteca','persone','capienza']]


while True:

    # Get actual timestamp and convert it
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    timestamp = pd.to_datetime(dt_string)

    # Get data from API
    response = requests.get(url).json()


    # Iterate through the list of libraries
    for biblio in biblioteche:
        # Create the temp empty list that needs to be appended to the list
        templist = []
        templist.append(timestamp)
        templist.append(biblio) # Nome della biblioteca
        templist.append(response[biblio]['persone']) # Persone presenti
        templist.append(response[biblio]['max']) # Capienza

        data.append(templist)


    # Convert list to Dataframe
    data_as_df = pd.DataFrame(data)
    # Set first row as columns
    data_as_df.columns = data_as_df.iloc[0]
    # Remove first row
    data_as_df = data_as_df.iloc[1:]

    # Create filename for exporting
    filename = 'capienza_biblioteche_'+str(timestamp)+'.csv'
    # Export
    data_as_df.to_csv(filename)

    
    if (timestamp.hour < 8):
        time.sleep(1800)
    else:
        time.sleep(300)

