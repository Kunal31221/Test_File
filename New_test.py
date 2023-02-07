import requests
from bs4 import BeautifulSoup
import csv

with open('Output' + '.csv', 'a', newline='', encoding='UTF-8-SIG') as fp:
    header = ["School", "Address", "State", "Zip_Code", "First_name","Last_name", "Job_title", "Phone", "Email"]
    writer = csv.writer(fp)
    writer.writerow(header)

def start():
    for i in range(0,9):
        url = f"https://isd110.org/our-schools/laketown-elementary/staff-directory?s=&page={i}"
        re = requests.get(url)
        soup = BeautifulSoup(re.text, "html.parser")

        school = soup.title.string.split("|")[-1].strip()

        full_address = [a.text.strip() for a in soup.select("p[class='address']")]
        full_address_new = full_address[-1].split("\n")

        address = full_address_new[0].strip()
        state = full_address_new[1].split(",")[0].strip()
        zip_Code = full_address_new[1].split(",")[-1].strip()

        information = soup.find_all("div", class_='first group')
        information_contact = soup.find_all("div", class_='last group')

        for x,y in zip(information,information_contact):
            name = x.find("h2", class_='title').text
            first_name = name.split(',')[0]
            last_name = name.split(',')[1]
            job_title = x.find("div", class_='field job-title').text.strip()
            phone = y.find("div", class_='field phone').text.strip()
            email = y.find("div", class_='field email').text.strip()
            output_lst = [school,address,state,zip_Code,first_name,last_name,job_title,phone,email]
            write_data(output_lst)


def write_data(output_lst):
    with open('Output' + '.csv', 'a', newline='', encoding='UTF-8-SIG') as fp:
        writer = csv.writer(fp)
        writer.writerow(output_lst)


if __name__ == '__main__':
    start()
