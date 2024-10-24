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
PATH = r"C:\Users\user\Desktop\sele"
 
options.add_experimental_option("prefs", {
    "download.default_directory": PATH,
    "directory_upgrade": True,
    "profile.default_content_settings.popups": 0,
    "plugins.always_open_pdf_externally": True,
    "safebrowsing.enabled": True  # Abilita il safe browsing per evitare problemi con i download
})
 
# Avvio del driver di Chrome
driver = Chrome(service=service, options=options)
 
 
driver.get("https://www.arpalazio.it/")

#Impostazione di un tempo di attesa per il caricamento della pagina
driver.implicitly_wait(10)
 
def accetta_cookie(driver):
    try:
        # Attendi che l'elemento sia presente e cliccabile
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.acceptcookies"))
        ).click()
        logging.info("Cookie accettati con successo.")
    except NoSuchElementException:
        logging.error("Il bottone per accettare i cookie non è stato trovato.")
    except ElementClickInterceptedException:
        logging.error("Il click sul bottone dei cookie è stato bloccato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")
 
 
# Funzione per cliccare sul bottone "Servizi"
def clicca_bottone_servizi(driver):
    try:
        # Trova il bottone "Servizi"
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button#Servizi'))
        )
        # Forza il click con JavaScript
        driver.execute_script("arguments[0].click();", button)
        logging.info("Bottone 'Servizi' cliccato con successo.")
    except NoSuchElementException:
        logging.error("Il bottone 'Servizi' non è stato trovato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")
 
 
# Funzione per cliccare sul link "Open Data"
def clicca_link_tariffario(driver):
    try:
        # Attendi che il link "Open Data" sia visibile
        link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Tariffario"]'))
        )
        # Clicca sul link
        link.click()
        logging.info("Link 'Tariffario' cliccato con successo.")
        # Attendi che la nuova pagina si carichi e accetta i cookie
        WebDriverWait(driver, 10).until(EC.title_contains("Tariffario"))  # Attendere che il titolo della pagina indichi che siamo sulla pagina "Tariffario"
        accetta_cookie(driver)  # Chiamata per accettare nuovamente i cookie
    except NoSuchElementException:
        logging.error("Il link 'Tariffario' non è stato trovato.")
    except ElementClickInterceptedException:
        logging.error("Il click sul link 'Tariffario' è stato bloccato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")
# Funzione per cliccare sul link "Dati della rete micrometeorologica" e accettare i cookie nella nuova pagina


 
def salva_nomi (driver): 
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label]')))
    
        documenti = driver.find_elements(By.CSS_SELECTOR, 'a[aria-label]')

        if documenti:
            logging.info("Questi sono i documenti: ")
            for doc in documenti:
                if ".pdf" in doc.get_attribute("href"):
                    print(doc.text)
                
        else:
            logging.info("Nessun documento trovato")    
    except  Exception as e:
        logging.error (f"Errore imprevisto {str(e)}")

def scarica_doc(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[aria-label]'))
            )
        documenti = driver.find_elements(By.CSS_SELECTOR, 'a[aria-label]')

        if documenti: 
             for doc in documenti:
                if ".pdf" in doc.get_attribute("href"):
                    doc.click()
                    logging.info(f"Scaricato: {doc.text}")
        else:
            logging.info("nessun documento trovato")
    except Exception as e:
        logging.error(f"Errore imprevisto : {str(e)}")    
# Esegui le funzioni precedenti e scarica i documenti
accetta_cookie(driver)
clicca_bottone_servizi(driver)
clicca_link_tariffario(driver)
accetta_cookie(driver)
salva_nomi(driver)
scarica_doc(driver)
# Chiudi il browser al termine
driver.quit()
