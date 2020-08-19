import pandas as pd

weather = "Resources/cities.csv"

weather_data = pd.read_csv(weather)

table  = weather_data.to_html(classes=["table", "table-bordered", "table-striped", "table-hover"])

text_file = open("table.txt", "w")
text_file.write(table)
text_file.close()