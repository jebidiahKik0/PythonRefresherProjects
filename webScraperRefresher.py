import pandas as pd
from io import StringIO

url = "https://en.wikipedia.org/wiki/List_of_best-selling_video_games"
tables = pd.read_html(url)
csvString = tables[0].to_csv(index = True)

with open('videoGameData.csv', 'w') as file:
    file.write(csvString)
print(csvString)