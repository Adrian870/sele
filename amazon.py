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
 
 
driver.get("https://www.amazon.it/?tag=wwwbingcom07-21&ref=pd_sl_7qhc95m3oa_e&adgrpid=1233652364972904&hvadid=77103437818587&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=1860&hvtargid=kwd-77103517078644:loc-93&hydadcr=10841_1834695&msclkid=a67f0a2742241f180af56d3c0f701340")

def accetta_cookie(driver):
    try:
        # Attendi che l'elemento sia presente e cliccabile
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sp-cc-accept"))
        ).click()
        logging.info("Cookie accettati con successo.")
    except NoSuchElementException:
        logging.error("Il bottone per accettare i cookie non è stato trovato.")
    except ElementClickInterceptedException:
        logging.error("Il click sul bottone dei cookie è stato bloccato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")
 

 
def clicca_ricerca(driver):
    try:
        input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#twotabsearchtextbox'))
            )
        
        # Forza il click con JavaScript
        input.send_keys("Dragon ball")
        logging.info("Bottone 'Servizi' cliccato con successo.")
    except NoSuchElementException:
        logging.error("Il bottone 'Servizi' non è stato trovato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")

def ricerca(driver):
    try:
        # Trova il bottone "Servizi"
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#nav-search-submit-button'))
        )
        # Forza il click con JavaScript
        driver.execute_script("arguments[0].click();", button)
        logging.info("Bottone 'Servizi' cliccato con successo.")
    except NoSuchElementException:
        logging.error("Il bottone 'Servizi' non è stato trovato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")
        
#.s-main-slot .s-result-item
#h2 .a-link-normal
#".a-price-whole"
def stampa_prodotti(driver):
    prodotti = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")

    # Itera su ogni prodotto e stampa la descrizione e il prezzo
    for prodotto in prodotti:
        try:
            descrizione = prodotto.find_element(By.CSS_SELECTOR, "h2 .a-link-normal").text
            prezzo = prodotto.find_element(By.CSS_SELECTOR, ".a-price-whole").text
            print(f"Descrizione: {descrizione}")
            print(f"Prezzo: {prezzo}€")
            time.sleep(1)
        except:
            # Se non riesce a trovare la descrizione o il prezzo, passa al prossimo prodotto
            continue
# Itera su ogni prodotto e stampa la descrizione e il prezzo
accetta_cookie(driver)
clicca_ricerca(driver)
time.sleep(2)
ricerca(driver)
stampa_prodotti(driver)



 

