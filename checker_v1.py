import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with the actual URL of the webpage
url = "https://results.knec.ac.ke"
code = "10208311103"  # Replace with the actual index number

# Use Chrome WebDriver
driver = webdriver.Chrome()
driver.get(url)

index_field = driver.find_element(By.ID, "indexNumber")
name_field = driver.find_element(By.ID, "name")
search_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

for index in range(1, 501):
    flag = False
    index_number = code + str(index).zfill(3)
    index_field.send_keys(index_number)
    
    for first_letter in range(65, 91):  # Loop through uppercase letters A-Z
        for second_letter in range(97, 123):  # Loop through lowercase letters a-z
            if flag:
                break
            name = chr(first_letter) + chr(second_letter)
            name_field.send_keys(name)
            index_field.send_keys(index_number)
            search_button.click()

            try:
                # Wait for data to appear in the target divs
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "row"))
                )

                # Extract and save the data
                data_rows = driver.find_elements(By.CLASS_NAME, "row")[1:]
                data = [row.text for row in data_rows]
                if data != ['View Results\nPlease enter a valid index number and your registered name', 'View Results', '', '']:
                    with open("results.txt", "a") as file:
                        file.writelines(data[2:])
                    print(data[2:])
                    flag = True

                # Clear fields
                name_field.clear()
                index_field.clear()
            
            except Exception as e:
                pass

driver.quit()