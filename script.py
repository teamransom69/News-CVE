import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# URL of the CVE page
url = "https://www.cert.ssi.gouv.fr/"

# Function to check for new CVEs
def check_for_new_cves():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find elements containing CVEs
    cve_elements = soup.find_all('div', class_='cve')

    for cve in cve_elements:
        cve_title = cve.find('a').text
        cve_link = cve.find('a')['href']
        # Check if you have already processed this CVE
        # If it's new, send an email
        # You can store already processed CVEs in a file or a database
        if not is_cve_already_sent(cve_title):
            send_email(cve_title, cve_link)
            mark_cve_as_sent(cve_title)

# Function to mark a CVE as already sent
def mark_cve_as_sent(cve_title):
    # Implement logic to save the CVE in a file or a database
    pass

# Function to check if a CVE has already been sent
def is_cve_already_sent(cve_title):
    # Implement logic to check if the CVE has already been sent
    pass
    
# Function to send an email
def send_email(cve_title, cve_link):
    to_email = "darkcybernetik@gmail.com"
    password = "thats_a_secret"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "New CVE: " + cve_title

    body = f"A new CVE has been published: {cve_title}\n\nLink: {cve_link}"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

if __name__ == "__main__":
    check_for_new_cves()
