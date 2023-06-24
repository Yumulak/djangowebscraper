#!C:\Python39\python.exe

import smtplib
import ssl
from email.message import EmailMessage
import cgi
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

form_inputs = cgi.FieldStorage()
# site_url = form_inputs.getvalue('site-url')
email_receiver = form_inputs.getvalue('email')
interval = form_inputs.getvalue('interval')

# scrape job ad page from url provided by user

# my job scrape code
def my_scrape_job_ads(site_url):
    r = requests.get(site_url)

    soup = BeautifulSoup(r.content, "html.parser")

    s = soup.find("div", class_="postings-wrapper")

    content = s.find_all("h5")

    titles = []
    links = []

    for c in content:
        titles.append(c.text)
        # print(c.text)

    for link in s.find_all("a"):
        links.append(link.get("href"))
        # print(link.get("href"))

    for listings in zip(titles, links):
        print(listings)

    d = {"Title": titles, "Link": links}
    df = pd.DataFrame.from_dict(d, orient = "index")
    df = df.transpose()
    df.to_csv("Vannevar_Labs_Job_Listings.csv", index = False, encoding = "utf-8")

# generated job scrape code
def scrape_job_ads(site_url):
    # Send a GET request to the website
    response = requests.get(site_url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all div elements on the page
    div_elements = soup.find_all('div')
    
    # Iterate over each div element and check for job ad information
    for div_element in div_elements:
        # Check if the div element contains job ad information based on specific criteria
        if contains_job_ad_info(div_element):
            title = extract_title(div_element)
            company = extract_company(div_element)
            location = extract_location(div_element)
            description = extract_description(div_element)
            
            # Print the extracted information
            # print('Title:', title)
            # print('Company:', company)
            # print('Location:', location)
            # print('Description:', description)
            # print('---')

            # Return the extracted information
            return title, company, location, description

def contains_job_ad_info(element):
    # Implement your logic to determine if the element contains job ad information
    # Return True if it does, False otherwise
    # You can check for specific patterns, class names, or other identifiers
    # For example:
    return element.get('class') == ['jobs-grid']

def extract_title(element):
    # Implement your logic to extract the job title from the element
    # Return the extracted title as a string
    # You may need to navigate the element's structure or use other methods
    # For example:
    return element.find('h3').text.strip()

def extract_company(element):
    # Implement your logic to extract the company name from the element
    # Return the extracted company name as a string
    # For example:
    return element.find('p', class_='company').text.strip()

def extract_location(element):
    # Implement your logic to extract the location from the element
    # Return the extracted location as a string
    # For example:
    return element.find('div', class_='p-16px-black none-bottom').text.strip()

def extract_description(element):
    # Implement your logic to extract the job description from the element
    # Return the extracted description as a string
    # For example:
    return element.find('div', class_='description').text.strip()

# email sender function
def send_email(email, url, interval):

    load_dotenv()

    # form inputs
    site_url = url
    email_receiver = email
    interval = interval

    # email sender credentials
    email_sender = os.environ["email_sender"]
    email_password = os.environ["email_password"]

    # email message
    subject = 'Your Job Ad Scraping Results are Ready!'
    body = f'Here are your job ad scraping results: \n{scrape_job_ads(site_url)}'

    # , scrape_job_ads(site_url)

    # email message instance
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # security
    context = ssl.create_default_context()

    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

# run sendemail script on each user every appropriate (interval) 

# for each user in Users

# scrape job ad page from url they provided

# send email with results

# user = Users.objects.create()

# for user in Users: