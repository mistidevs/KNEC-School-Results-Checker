import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with the actual URL of the webpage
url = "https://results.knec.ac.ke"
code = "20406020"  # Replace with the actual index number 
options = Options()
driver = webdriver.Chrome(options=options)  # Replace with the appropriate driver for your browser
driver.get(url)

"""min = int(input("Enter lowest index: "))
max = int(input("Enter highest index: "))"""

def get_fields(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "name")))
    name_field = driver.find_element(By.ID, "name")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "indexNumber")))
    index_field = driver.find_element(By.ID, "indexNumber")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "consentCheckbox")))
    checkbox = driver.find_element(By.ID, "consentCheckbox")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-primary")))
    search_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

    return name_field, index_field, checkbox, search_button

for index in range(1, 501):
    flag = False
    index_number = code + str(index).zfill(3)
    _, index_field, _, _ = get_fields(driver)
    index_field.send_keys(index_number)

    for first_letter in range(65, 91):  # Loop through uppercase letters A-Z
        for second_letter in range(97, 123):  # Loop through lowercase letters a-z
            if flag:
                break
            name = chr(first_letter) + chr(second_letter)
            name_field, index_field, checkbox, search_button = get_fields(driver)
            name_field.clear()
            name_field.send_keys(name)
            index_field.clear()
            index_field.send_keys(index_number)
            if not checkbox.is_selected():
                checkbox.click()
            search_button.click()

            try:
                # Wait for data to appear in the target divs
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "row"))
                )

                # Extract and save the data
                data_rows = driver.find_elements(By.CLASS_NAME, "row")[1:]
                data = [row.text for row in data_rows]
                if any('KCSE Examination Provisional Results' in item for item in data):
                    with open("results.txt", "a") as file:
                        file.writelines(data[2:])
                    print(data[2:])
                    flag = True
                    break
                
            except Exception as e:
                pass


driver.quit()
