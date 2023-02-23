import scraper
import csv

asos_data = scraper.Scraper()
clothes_list = asos_data.asos_scraper()
print(type(clothes_list))
print(clothes_list)

myFile = open('asos_clothes.csv', 'w')
writer = csv.DictWriter(myFile, fieldnames=['id', 'description', 'price', 'colour'])
writer.writeheader()
writer.writerows(clothes_list)
myFile.close()
# myFile = open('demo_file.csv', 'r')
# print("The content of the csv file is:")
# print(myFile.read())
# myFile.close()