import time
import uuid

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class Scraper:
    # Initialise the Scraper class and opens the webpage
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        URL = "https://www.asos.com/men/new-in/new-in-clothing/cat/?cid=6993&nlid=mw|clothing|shop+by+product|new+in"
        self.driver.get(URL)
        time.sleep(3)

    def cookies(self) -> webdriver.Chrome:
        """Accept cookies from Chrome webpage
        """
        try:
            accept_cookies_button = self.driver.find_element(
                by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]'
            )
            accept_cookies_button.click()
            time.sleep(1)
        except (
            AttributeError
        ):
            self.driver.switch_to.frame(
                "onetrust-consent-sdk"
            )  # This is the id of the frame
            accept_cookies_button = self.driver.find_element(
                by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]'
            )
            accept_cookies_button.click()
            time.sleep(1)

        except:
            pass

    def get_links(self) -> list:
        """Collects the links of the clothes on the page
        
        clothes_list: container of all the links

        returns:
            list: list of links
        """

        clothes_container = self.driver.find_element(
            by=By.XPATH, value='//*[@class="listingPage_HfNlp"]'
        )
        clothes_list = clothes_container.find_elements(by=By.XPATH, value="./article")
        link_list = []
        print(len(clothes_list))

        # Adds the links to the list
        for clothes in clothes_list:
            a_tag = clothes.find_element(by=By.TAG_NAME, value="a")
            link = a_tag.get_attribute("href")
            link_list.append(link)
            if len(link_list) == 5:
                print(f"There are {len(link_list)} items of clothing in this page")
                return link_list

    def create_id(self):
        """Creates a unique id for each item of clothing

        returns: id
        """
        id = str(uuid.uuid4())

        return id

    def create_dict(self, id, description, price, colour):
        """Creates a dictionary of the data
        args:
            id: unique id
            description: description of the item of clothing
            price: price of the item of clothing
            colour: colour of the item of clothing
        returns:
            dict: empty dictionary of the data
        """
        id_dict = {}

        id_dict["id"] = id
        id_dict["description"] = description
        id_dict["price"] = price
        id_dict["colour"] = colour

        return id_dict

    def get_data(self):
        """Iterates through the links and collects the data
        clothes: list of links
        returns:
            clothes_list: list of dictionaries of the data
        """
        clothes = []
        clothes.extend(self.get_links())
        clothes_list = []

        try:
            # Adds the data to a dictionary and appends the dictionary to a list
            for links in clothes:
                self.driver.get(links)
                time.sleep(5)
                description = self.driver.find_element(by=By.TAG_NAME, value="h1").text
                price = self.driver.find_element(
                    by=By.XPATH, value='//*[@class="ky6t2"]'
                ).text
                colour = self.driver.find_element(
                    by=By.XPATH, value='//*[@class="L3V0U"]'
                ).text
                id = self.create_id()
                product_dict = self.create_dict(id, description, price, colour)
                clothes_list.append(product_dict)

        except NoSuchElementException:
            pass

        return clothes_list

    def asos_scraper(self):
        """Runs the functions and returns the list of clothes
        returns:
            list: list of dictionaries of the data
        """
        print("running scraper.....")
        self.cookies()
        self.create_id()
        available_clothes_list = self.get_data()

        return available_clothes_list
