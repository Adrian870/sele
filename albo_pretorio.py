from selenium.common.exceptions import StaleElementReferenceException
from datetime import datetime
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver import Chrome
import logging
import time
# Configurazione delogger
logging.basicConfig(level=logging.INFO)

 
# Percorso del driver di Chrome specifico
chrome_driver_path = r"C:\Users\user\Desktop\chromedriver-win64\chromedriver-win64\\chromedriver.exe"
 
# Inizializzo il servizio con il percorso specifico del driver di Chrome
service = Service(chrome_driver_path)
 
# Inizializzo le opzioni del browser Chrome
options = Options()
 
# DIRECTORY DI DESTINAZIONE DEI FILE
PATH = r"C:\Users\user\Desktop\sele\file"
 
options.add_experimental_option("prefs", {
    "download.default_directory": PATH,
    "directory_upgrade": True,
    "profile.default_content_settings.popups": 0,
    "plugins.always_open_pdf_externally": True,
    "safebrowsing.enabled": True  # Abilita il safe browsing per evitare problemi con i download
})
 
# Avvio del driver di Chrome
driver = Chrome(service=service, options=options)

driver.get("https://www.albopretorionline.it/campania/")

def clicca_ricerca(driver):
    try:
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#btCerca'))
        )
        # Forza il click con JavaScript
        driver.execute_script("arguments[0].click();", button)
        logging.info("Bottone 'Cerca' cliccato con successo.")
    except NoSuchElementException:
        logging.error("Il bottone 'Cerca' non è stato trovato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")


clicca_ricerca(driver)


def refresh_li_elements():
    return driver.find_elements(By.XPATH, "//li[.//a[contains(@href, 'download.aspx')]]")

def date(text):
    pattern = re.compile(r"dal (\d{2}-\d{2}-\d{4}) al (\d{2}-\d{2}-\d{4})")
    match = pattern.search(text)
    if match:
        return match.group(1), match.group(2)
    return None, None

def numero_atti(text):
    pattern = re.compile(
        r"Proc\.n\. (\d+)/\d+|"
        r"\(Proc\. (\d+)/\d+\)|"
        r"Proc\. (\d+)/\d+|"
        r": Proc\.(\d+)/\d+-|"
        r"PROC\.\s(\d+)/\d+\s-|"
        r"(\d+)/\d+-|"
        r"proc\.\s(\d+)/\d+|"
        r"Proc\.(\d+)/\d+|"
        r"proc\.\s(\d+)/\d+|"
        r"proc\.(\d+)/\d+|"
        r"PROC\.\s(\d+)/\d+|"
        r"D\. D\. n\. (\d+)"  
    )
    
    match = pattern.search(text)
    if match:
        for group in match.groups():
            if group:
                return int(group)
    return None

li_elements = refresh_li_elements()

file_scaricati = []

data = datetime.now().strftime('%Y-%m-%d')

for li in li_elements:
    try:
        documents_links = li.find_elements(By.XPATH, "//a[contains(@href, 'download.aspx')]")

        text_content = li.text
        dataInizio, dataFine = date(text_content)
        act_number = numero_atti(text_content)

        for link in documents_links:
            file_url = link.get_attribute("href")
            file_name = link.text
            
            minio = f"REGIONE_CAMPANIA"
            file_scaricati.append({
                "nome_file": file_name,
                "file_url": file_url,
                "dataInizio": dataInizio,
                "dataFine": dataFine,
                "numero_atti": act_number, 
                "data_scraping": data,
            })        
            link.click()
            logging.info(f"scaricamento del file: {file_name} dall'URL: {file_url}")
            logging.info(file_scaricati)

            time.sleep(3)                
       
        li_elements = refresh_li_elements()
       
       
    
    except StaleElementReferenceException:
        continue
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")

    document_links = driver.find_elements(By.CSS_SELECTOR, '#centercol > ul > li > a')

    
for link in document_links:
    document_url = link.get_attribute('href')
    driver.get(document_url)
    time.sleep(1)  

    


driver.quit()