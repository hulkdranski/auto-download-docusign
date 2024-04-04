#Imports
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import customtkinter
import threading
from tkinter import filedialog
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def download():
    global running
    baixados = []
    n = 0
    x = 10
    conterro = 0
    laco = len(driver.find_elements(By.CLASS_NAME, 'css-1obf64m'))
    footer = driver.find_element(By.TAG_NAME, "footer")
    scroll_origin = ScrollOrigin.from_element(footer, 0, -50)
    name = driver.title

    if 'Concluído' in name:
        while n <= laco and running:
            try:
                nome = driver.find_element('xpath',
                                           f'/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[3]/div/table/tbody/div[{n + 2}]/tr/td[3]/span[1]/div').text
                data = driver.find_element('xpath',
                                           f'/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[3]/div/table/tbody/div[{n + 2}]/tr/td[5]/span[1]').text
                hora = driver.find_element('xpath',
                                           f'/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[3]/div/table/tbody/div[{n + 2}]/tr/td[5]/span[2]').text
                identificacao = nome + data + hora

                laco1 = len(driver.find_elements(By.CLASS_NAME, 'css-1obf64m'))
                if laco != laco1:
                    laco = len(driver.find_elements(By.CLASS_NAME, 'css-1obf64m'))
                    n = 0
                else:
                    if not identificacao in baixados:
                        btn_download = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                            f'/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[3]/div/'
                                            f'table/tbody/div[{n + 2}]/tr/td[7]/span/span/button[1]')))
                        btn_download.click()

                        btn_combinar = WebDriverWait(driver, 9999999).until(EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div[3]/div[2]/div[2]/div/div/div[3]/div/div/fieldset/div[4]/div/div[2]/label/span/span')))
                        btn_combinar.click()

                        btn_baixar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                        '/html/body/div[3]/div[2]/div[2]/div/div/div[4]/div/div/div[2]/button')))
                        btn_baixar.click()

                        driver.switch_to.window(original_window)
                        ActionChains(driver) \
                            .scroll_from_origin(scroll_origin, 0, 93) \
                            .perform()
                        baixados.append(identificacao)
                        conterro = 0
                        time.sleep(2)

                print(n, laco)
                n += 1

                if len(baixados) >= x:
                    n = 0
                    x += 10

            except NoSuchElementException:
                if identificacao in baixados:
                    n = 0
                    conterro += 1
                    ActionChains(driver) \
                        .scroll_from_origin(scroll_origin, 0, 93) \
                        .perform()
                    if conterro >= 2:
                        break
                else:
                    ActionChains(driver) \
                        .scroll_from_origin(scroll_origin, 0, 93) \
                        .perform()
                    conterro += 1
                    n = 0
                    if conterro >= 2:
                        break

            except StaleElementReferenceException:
                if identificacao in baixados:
                    n = 0
                    conterro += 1
                    if conterro >= 2:
                        break
                else:
                    conterro += 1
                    n = 0
                    if conterro >= 2:
                        break
    else:
        print('else concluido')
        while n <= laco and running:
            try:
                nome = driver.find_element('xpath',
                                           f'/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[3]/div/table/tbody/div[{n + 2}]/tr/td[3]/span[1]/div').text
                data = driver.find_element('xpath',
                                           f'/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[3]/div/table/tbody/div[{n + 2}]/tr/td[5]/span[1]').text
                hora = driver.find_element('xpath',
                                           f'/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[3]/div/table/tbody/div[{n + 2}]/tr/td[5]/span[2]').text
                identificacao = nome + data + hora

                laco1 = len(driver.find_elements(By.CLASS_NAME, 'css-1obf64m'))
                if laco != laco1:
                    laco = len(driver.find_elements(By.CLASS_NAME, 'css-1obf64m'))
                    n = 0
                else:
                    if not identificacao in baixados:
                        btn_download = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                            f'/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[3]/div/'
                                            f'table/tbody/div[{n + 2}]/tr/td[6]/span/span/button[1]')))
                        btn_download.click()

                        btn_combinar = WebDriverWait(driver, 99999999).until(EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div[3]/div[2]/div[2]/div/div/div[3]/div/div/fieldset/div[4]/div/div[2]/label/span/span')))
                        btn_combinar.click()

                        btn_baixar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div[3]/div[2]/div[2]/div/div/div[4]/div/div/div[2]/button')))
                        btn_baixar.click()

                        driver.switch_to.window(original_window)
                        ActionChains(driver) \
                            .scroll_from_origin(scroll_origin, 0, 95) \
                            .perform()
                        baixados.append(identificacao)
                        conterro = 0

                time.sleep(2)
                n += 1

            except NoSuchElementException:
                if identificacao in baixados:
                    n = 0
                    conterro += 1
                    if conterro >= 2:
                        break
                else:
                    conterro += 1
                    n = 0
                    if conterro >= 2:
                        break

            except StaleElementReferenceException:
                if identificacao in baixados:
                    n = 0
                    conterro += 1
                    if conterro >= 2:
                        break
                else:
                    conterro += 1
                    n = 0
                    if conterro >= 2:
                        break

def stop():
    global running
    running = False


def start():
    global running
    running = True
    t = threading.Thread(target=download)
    t.start()


if __name__ == '__main__':
    global running
    options = webdriver.ChromeOptions()
    file = filedialog.askdirectory()
    file_path = file.replace('/', '\\')
    prefs = {"profile.default_content_settings.popups": 0,
             "download.default_directory":
                 rf"{file_path}\\",
             "directory_upgrade": True}
    options.add_experimental_option('prefs', prefs)
    driver_service = Service(executable_path=r"T:\Robo Docusign\1\chromedriver.exe")

    driver = webdriver.Chrome(service=driver_service, options=options)
    driver.get('https://app.docusign.com/documents')
    original_window = driver.current_window_handle
    driver.implicitly_wait(15)

    login = customtkinter.CTk()
    login.title('DOCUSIGN MSP')
    login.geometry('300x180')
    login.config(bg='#ffffff')
    login.iconbitmap(r'T:\Robo Docusign\1\imgs\logo.ico')
    login.resizable(False, False)
    biduzin = customtkinter.CTkImage(Image.open(r"T:\Robo Docusign\1\imgs\logomsp.png"), size=(200, 80))

    logo1 = customtkinter.CTkLabel(master=login, image=biduzin, bg_color='#ffffff', text='')
    button_shadow = customtkinter.CTkButton(master=login, fg_color='#A3A3A3', text='',
                                            corner_radius=5, border_color='#000000', border_width=0,
                                            hover_color='#A3A3A3', width=210)

    button1 = customtkinter.CTkButton(master=login, fg_color='#44C8FE', hover_color='#D8DBE6', text_color='#000000',
                                      text='Baixar todos documentos', font=("Calibri", 14), corner_radius=5,
                                      border_color='#000000', border_width=2, width=215, command=start)

    button2 = customtkinter.CTkButton(master=login, fg_color='#ffffff', hover_color='#D8DBE6', text_color='#000000',
                                      text='Parar', font=("Calibri", 14), corner_radius=5,
                                      border_color='#000000', border_width=1, width=115, command=stop)

    button_shadow.place(x=40, y=99)
    button1.place(x=37, y=97)
    button2.place(x=87, y=140)
    logo1.grid(row=0, column=0, padx=(40, 0), pady=(10, 0))
    login.mainloop()
