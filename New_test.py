import requests
from bs4 import BeautifulSoup


def start():
    for i in range(0,9):
        url = f"https://isd110.org/our-schools/laketown-elementary/staff-directory?s=&page={i}"
        print(url)
        re = requests.get(url)
        print(re.status_code)
        soup = BeautifulSoup(re.text, "html.parser")

        school = soup.title.string.split("|")[-1].strip()
        print(school)

        full_address = [a.text.strip() for a in soup.select("p[class='address']")]
        full_address_new = full_address[-1].split("\n")

        address = full_address_new[0].strip()
        print(address)
        state = full_address_new[1].split(",")[0].strip()
        print(state)
        zip = full_address_new[1].split(",")[-1].strip()
        print(zip)
        information = soup.find_all("div",class_='first group')
        name = [i.find("h2",class_='title').text for i in information]
        print(name)

        job_title = [i.find("div",class_='field job-title').text.strip() for i in information]
        print(job_title)

        information_contact = soup.find_all("div",class_='last group')
        phone = [i.find("div",class_='field phone').text.strip() for i in information_contact]
        print(phone)

        email = [i.find("div",class_='field email').text.strip() for i in information_contact]
        print(email)

        print("******************************************************************")


if __name__ == '__main__':

    start()
