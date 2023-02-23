import csv

import scraper

# Run the Scraper class from scraper.py
asos_data = scraper.Scraper()
clothes_list = asos_data.asos_scraper()
print(type(clothes_list))
print(clothes_list)

# Save clothes_list to a csv file
myFile = open("asos_clothes.csv", "w")
writer = csv.DictWriter(myFile, fieldnames=["id", "description", "price", "colour"])
writer.writeheader()
writer.writerows(clothes_list)
myFile.close()
