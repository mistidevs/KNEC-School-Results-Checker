import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import pyinputplus as pyip

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_driver():
    # Specify the path to the chromedriver executable
    chrome_driver_binary = "/usr/bin/chromedriver"  # Adjust the path accordingly

    # Create a Service object with the specified executable path
    service = Service(chrome_driver_binary)

    # Create ChromeOptions
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    # Instantiate the Chrome webdriver with the specified service and options
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def get_user_input():
    # Use pyinputplus to ensure input is an int with a maximum of 3 digits
    min_index = pyip.inputInt(prompt="Enter lowest index: " , min=1)
    max_index = pyip.inputInt(prompt="Enter highest index: ", min=1)
    if max_index > min_index:
        return min_index, max_index
    else:
        logger.error("Max index must be greater than min index")
        raise ValueError("Max index must be greater than min index")

def clear_input_fields(driver, *elements):
    for element in elements:
        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(element)).clear()
        except:
            pass

def main():
    # Replace with the actual URL of the webpage
    url = "https://results.knec.ac.ke"
    code = input("Enter School code: ")  # Replace with the actual index number

    driver = initialize_driver()
    driver.get(url)

    index_field = (By.ID, "indexNumber")
    name_field = (By.ID, "name")
    search_button = (By.CSS_SELECTOR, "button.btn-primary")

    min_index, max_index = get_user_input()

    try:
        for index in range(min_index, max_index + 1):
            flag = False
            index_number = code + str(index).zfill(3)

            clear_input_fields(driver, index_field, name_field)

            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(index_field)).send_keys(index_number)

            for first_letter in range(65, 91):  # Loop through uppercase letters A-Z
                for second_letter in range(97, 123):  # Loop through lowercase letters a-z
                    if flag:
                        break
                    name = chr(first_letter) + chr(second_letter)
                    
                    clear_input_fields(driver, name_field)
                    
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(name_field)).send_keys(name)
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(index_field)).send_keys(index_number)
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(search_button)).click()

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
                            logger.info(f"Data for index {index}: {data[2:]}")
                            flag = True
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located(name_field))
                            clear_input_fields(driver, name_field, index_field, search_button)
                            break

                        WebDriverWait(driver, 10).until(EC.presence_of_element_located(name_field))
                        clear_input_fields(driver, name_field, index_field, search_button)

                    except Exception as e:
                        logger.error(f"An error occurred: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
