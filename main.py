import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time
from prettytable import PrettyTable

while True:
    # Input marka
    print()
    print('Kādas markas auto meklējat?')
    marka = input()
    if marka == 'bmw' or marka == 'BMW':
        formated_marka = 'BMW'
    else:
        formated_marka = " ".join(word.capitalize() for word in marka.split())

    # Input cena
    print()
    print('Kādā cenu intervālā?')
    cena_no = input('MIN cena: ')
    cena_lidz = input('MAX cena: ')

    # Input gads
    print()
    print('Kura gada?')
    gads1 = input('No: ')
    gads2 = input('Līzd: ')

    # Input dzineja tips
    while True:
        print()
        print('Kāds dzinējs? (Benzīns; Gāze ; Dīzelis ; Hibrīds ; Elektriskais)')
        tips = input()
        format_tips = " ".join(word.capitalize() for word in tips.split())
        if format_tips == 'Benzīns':
            dzineja_tips = '493'
            break
        elif format_tips == 'Gāze':
            dzineja_tips = '495'
            break
        elif format_tips == 'Dīzelis':
            dzineja_tips = '494'
            break
        elif format_tips == 'Hibrīds':
            dzineja_tips = '7434'
            break
        elif format_tips == 'Elektriskais':
            dzineja_tips = '114330'
            break
        else:
            print('Nepareizi ievadīts!')
            print('Ievadiet atkārtoti!')


    # Input dzineja tilpums
    print()
    print('Kāds dzinēja tlpums?')
    dzineja_tilpums1 = input('No: ')
    dzineja_tilpums2 = input('Līdz: ')

    # Input kārba
    print()
    while True:
        print('Kāda ātrumu kārba(Automāts; Manuāla)?')
        karba_input = input()
        karba = " ".join(word.capitalize() for word in karba_input.split())
        if karba == 'Automāts':
            atruma_karba = '497'
            break
        elif karba == 'Manuāla':
            atruma_karba = '496'
            break
        else:
            print('Nepareizi ievadīts!')
            print('Ievadiet atkārtoti!')


    # Atvert SS.lv
    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=option)
    url = "https://www.ss.lv/lv/transport/cars/"
    driver.get(url)
    time. sleep(2)
    

    # Atrast marku
    xpath_marka = f"//a[text()='{formated_marka}']"

    try:
        link = driver.find_element(By.XPATH, xpath_marka)
        link.click()
    except NoSuchElementException:
        print('Šādam auto nav sludinājumu!')
        break

    # Ievadit cena
    cena_no_box = driver.find_element(By.ID, 'f_o_8_min')
    cena_no_box.send_keys(cena_no)
    cena_lidz_box = driver.find_element(By.ID, 'f_o_8_max')
    cena_lidz_box.send_keys(cena_lidz)

    # Ievadit gads
    try:
        gads_box = driver.find_element(By.ID, 'f_o_18_min')
        select_gads = Select(gads_box)
        select_gads.select_by_value(gads1)
        gads_box = driver.find_element(By.ID, 'f_o_18_max')
        select_gads = Select(gads_box)
        select_gads.select_by_value(gads2)
    except NoSuchElementException:
        print('Šādam auto nav sludinājumu!')
        break


    # Ievadit tilpums
    try:
        tilpums_box = driver.find_element(By.ID, 'f_o_15_min')
        select_tilpums = Select(tilpums_box)
        select_tilpums.select_by_value(dzineja_tilpums1)
        tilpums_box = driver.find_element(By.ID, 'f_o_15_max')
        select_tilpums = Select(tilpums_box)
        select_tilpums.select_by_value(dzineja_tilpums2)
    except NoSuchElementException:
        print('Šādam auto nav sludinājumu!')
        break

    # Ievadit dzinejs
    try:
        dzinejs_box = driver.find_element(By.ID, 'f_o_34')
        select_dzinejs = Select(dzinejs_box)
        select_dzinejs.select_by_value(dzineja_tips)
    except NoSuchElementException:
        print('Šādam auto nav sludinājumu!')
        break

    # Ievadit karba
    try:
        karba_box = driver.find_element(By.ID, 'f_o_35')
        select_karba = Select(karba_box)
        select_karba.select_by_value(atruma_karba)
    except NoSuchElementException:
        print('Šādam auto nav sludinājumu!')
        break


    # Atrast tabula majaslapa
    form = driver.find_element(By.XPATH, "//form[@id='filter_frm']")

    table_index = 3
    table_xpath = f"(//form[@id='filter_frm']//table)[{table_index}]"
    table = form.find_element(By.XPATH, table_xpath)

    tbody = table.find_element(By.TAG_NAME, "tbody")

    tbody = table.find_element(By.TAG_NAME, "tbody")


    # Iegut datus no majaslapas
    data = []
    def get_link_from_row(row):
        try:
            link_element = row.find_element(By.XPATH, ".//td[@class='msg2']/div[@class='d1']/a")
            link = link_element.get_attribute('href')
            return link
        except NoSuchElementException:
            return ''
        
    rows = tbody.find_elements(By.TAG_NAME, "tr")[1:]
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text for cell in cells] + [get_link_from_row(row)]

        data.append(row_data)


    # Iznemt lieko info no datiem
    def clean_row(row):
        if len(row) >= 8:
            return [row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
        else:
            return row

    cleaned_data = [clean_row(row) for row in data]


    # Sakartot datus
    cleaned_data = [row for row in cleaned_data if row]

    table_headers = ['Sludinajums', 'Modelis', 'Gads', 'Tilp.', 'Nobraukums', 'Cena', 'Link']
    pretty_table = PrettyTable(table_headers)

    for row in cleaned_data:
        if len(row) == len(table_headers):
            pretty_table.add_row(row)
    driver.quit()


    # Izvadit tabulu + parbaudit vai ir dati
    if cleaned_data:
        pretty_table.align = "l"
        print('\n' * 3)
        print(pretty_table)
    else:
        print('Šādam auto nav sludinājumu!')


    # Koda atkartosana
    print('\n' * 2)
    repeat = input("Vai meklējat vēl kādu mašīnu? (jā/nē): ").lower()

    if repeat != 'jā' and repeat != 'j':
        break


    # Iztuksot mainigos
    data.clear()
    cleaned_data.clear()
    pretty_table.clear_rows()
