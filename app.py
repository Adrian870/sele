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

def clicca_dati_decreto_interdirettoriale(driver):
    try:
        # Attendi che il link "Dati della rete micrometeorologica" sia visibile
        link = WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Decreto interdirettoriale del 23 novembre 2012"]'))
)
 
        # Clicca sul link
        link.click()
        logging.info("Link 'Decreto interdirettoriale del 23 novembre 2012 ' cliccato con successo.")

    except NoSuchElementException:
        logging.error("Il link 'Decreto interdirettoriale del 23 novembre 2012 ' non è stato trovato.")
    except ElementClickInterceptedException:
        logging.error("Il click sul link 'Decreto interdirettoriale del 23 novembre 2012 ' è stato bloccato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}", exc_info=True)


def clicca_dati_circolare_3marzo(driver):
    try:
        # Attendi che il link "Dati della rete micrometeorologica" sia visibile
        link = WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Circolare del Ministero del Lavoro e delle Politiche Sociali del 3 marzo 2015 "]'))
)
 
        # Clicca sul link
        link.click()
        logging.info("Link 'Circolare del Ministero del Lavoro e delle Politiche Sociali del 3 marzo 2015 ' cliccato con successo.")

    except NoSuchElementException:
        logging.error("Il link 'Circolare del Ministero del Lavoro e delle Politiche Sociali del 3 marzo 2015 ' non è stato trovato.")
    except ElementClickInterceptedException:
        logging.error("Il click sul link 'Circolare del Ministero del Lavoro e delle Politiche Sociali del 3 marzo 2015 ' è stato bloccato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}", exc_info=True)

def clicca_dati_decreto_ministero(driver):
    try:
        # Attendi che il link "Dati della rete micrometeorologica" sia visibile
        link = WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Decreto 14 ottobre 2016 del Ministero dell Ambiente e della Tutela del Territorio e del Mare"]'))
)
 
        # Clicca sul link
        link.click()
        logging.info("Link 'Decreto 14 ottobre 2016 del Ministero dell'Ambiente e della Tutela del Territorio e del Mare' cliccato con successo.")

    except NoSuchElementException:
        logging.error("Il link 'Decreto 14 ottobre 2016 del Ministero dell'Ambiente e della Tutela del Territorio e del Mare' non è stato trovato.")
    except ElementClickInterceptedException:
        logging.error("Il click sul link 'Decreto 14 ottobre 2016 del Ministero dell'Ambiente e della Tutela del Territorio e del Mare' è stato bloccato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}", exc_info=True)
  

def clicca_dati_circolare_min(driver):
    try:
        # Attendi che il link "Dati della rete micrometeorologica" sia visibile
        link = WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Circolare del Ministero del Lavoro e delle Politiche Sociali n. 10912 del 24.11.2022"]'))
)
 
        # Clicca sul link
        link.click()
        logging.info("Link 'Circolare del Ministero del Lavoro e delle Politiche Sociali n. 10912 del 24.11.2022 ' cliccato con successo.")

    except NoSuchElementException:
        logging.error("Il link 'Circolare del Ministero del Lavoro e delle Politiche Sociali n. 10912 del 24.11.2022 ' non è stato trovato.")
    except ElementClickInterceptedException:
        logging.error("Il click sul link 'Circolare del Ministero del Lavoro e delle Politiche Sociali n. 10912 del 24.11.2022 ' è stato bloccato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}", exc_info=True)

def clicca_dati_deliberazione(driver):
    try:
        # Attendi che il link "Dati della rete micrometeorologica" sia visibile
        link = WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label=" deliberazione n. 14 dell 31.01.2024."]'))
)
 
        # Clicca sul link
        link.click()
        logging.info("Link ' deliberazione n. 14 dell'31.01.2024. ' cliccato con successo.")

    except NoSuchElementException:
        logging.error("Il link ' deliberazione n. 14 dell'31.01.2024. ' non è stato trovato.")
    except ElementClickInterceptedException:
        logging.error("Il click sul link ' deliberazione n. 14 dell'31.01.2024. ' è stato bloccato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}", exc_info=True)


def clicca_dati_tariffario(driver):
    try:
        # Attendi che il link "Dati della rete micrometeorologica" sia visibile
        link = WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label=" Tariffario 2024"]'))
)
 
        # Clicca sul link
        link.click()
        logging.info("Link 'Tariffario 2024 ' cliccato con successo.")

    except NoSuchElementException:
        logging.error("Il link ' Tariffario 2024 ' non è stato trovato.")
    except ElementClickInterceptedException:
        logging.error("Il click sul link ' Tariffario 2024 ' è stato bloccato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}", exc_info=True)

 
 
def main (driver): 
    accetta_cookie(driver)
    clicca_dati_decreto_interdirettoriale(driver)
    clicca_dati_circolare_3marzo(driver)
    clicca_dati_decreto_ministero(driver)
    clicca_dati_circolare_min(driver)
    clicca_dati_deliberazione(driver)
    clicca_dati_tariffario(driver)
    
# Esegui le funzioni precedenti e scarica i documenti
accetta_cookie(driver)
clicca_bottone_servizi(driver)
clicca_link_tariffario(driver)
main(driver)
# Chiudi il browser al termine
driver.quit()
