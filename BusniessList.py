# url https://www.businesslist.pk
# importing libraries



import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# set the chrome driver below
driver =webdriver.Chrome("chromedriver.exe")
driver.minimize_window()
import pandas as pd

# the url of the website

weburl = "https://www.businesslist.pk/location/lahore/"
driver.get(weburl)
r = requests.get(weburl)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent, "html.parser")


global_page_url="https://www.businesslist.pk/location/lahore/"
company_list = []
address_list = []
phone_list =[]
website_list = []
page_number  =2
for i in range(1,10,1):

    # urlglob = driver.get("https://www.businesslist.pk/location/lahore/")
    driver.get(weburl)
    r2 = requests.get(weburl)
    htmlcontent2 = r2.content
    soup2 = BeautifulSoup(htmlcontent2, "html.parser")
    driver.find_element(By.LINK_TEXT, f"{i}").click()

    print("the url is ",driver.current_url)
    divs = soup2.find_all("div", {"class": "company with_img g_0"})
    headers = soup2.find_all("h4")
    main_cmpnes = [i.text for i in headers]


    for i,k in enumerate(main_cmpnes):
        try:

            print(i,k)
            driver.get(driver.current_url)
            print("the internal current url is",driver.current_url)
            # print("now globale url :",driver.current_url)
            driver.find_element(By.LINK_TEXT,f"{k}").click()

            print("after clicking the button",driver.current_url)

            # print(internal_details_url,"internal details url")

            driver.get(driver.current_url)
            r1 = requests.get(weburl)
            htmlcontent = r1.content
            soup1 = BeautifulSoup(htmlcontent, "html.parser")
            print("after soup 1",driver.current_url)
            # data finding
            company_name =k

            address = soup1.find_all("div", {"class": "text location"})
            address_data = [i.text for i in address]

            phone_number = soup1.find_all("div",{"class","text phone"})
            phone_data = [i.text for i in phone_number]
            print(phone_data)

            website = soup1.find_all("div", {"class", "weblinks"})
            website_data = [i.text for i in website]


            company_list.append(company_name),
            address_list.append(address_data),
            phone_list.append(phone_data),
            website_list.append(website_data)
            
            print("internal url chaned")
            print(company_name,address_data,phone_data,website_data)
            
            # store the data in CSV file at run time 
            df = pd.DataFrame({
                "Company": company_name,
                "address": address_data,
                "phone": phone_data,
                "website": website_data
            })
            df.to_csv("finalcompanies1.csv",  mode='a')

            print('DATA HAS BEEN INSERTED')

        except:
            pass



    print("URL CHANGED GLOBALLY")
    # global_page_url.clear()
    page_number+=1
    # global_page_url.append(f"http://www.businesslist.pk/location/lahore/{page_number}")
