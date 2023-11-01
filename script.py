import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# URL de la page CVE
url = "https://www.cert.ssi.gouv.fr/"

# Fonction pour envoyer un e-mail
def send_email(cve_title, cve_link):
    from_email = "votre_adresse_email@gmail.com"
    to_email = "darkcybernetik@gmail.com"
    password = "votre_mot_de_passe"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Nouvelle CVE : " + cve_title

    body = f"Une nouvelle CVE a été publiée : {cve_title}\n\nLien : {cve_link}"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# Fonction pour vérifier les nouvelles CVE
def check_for_new_cves():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Trouver les éléments contenant les CVE
    cve_elements = soup.find_all('div', class_='cve')

    for cve in cve_elements:
        cve_title = cve.find('a').text
        cve_link = cve.find('a')['href']
        # Vérifier si vous avez déjà traité cette CVE
        # Si elle est nouvelle, envoyez un e-mail
        # Vous pouvez stocker les CVE déjà traitées dans un fichier ou une base de données
        if not is_cve_already_sent(cve_title):
            send_email(cve_title, cve_link)
            mark_cve_as_sent(cve_title)

# Fonction pour marquer une CVE comme déjà envoyée
def mark_cve_as_sent(cve_title):
    # Implémentez la logique pour enregistrer la CVE dans un fichier ou une base de données
    pass

# Fonction pour vérifier si une CVE a déjà été envoyée
def is_cve_already_sent(cve_title):
    # Implémentez la logique pour vérifier si la CVE a déjà été envoyée
    pass

if __name__ == "__main__":
    check_for_new_cves()
