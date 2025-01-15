# Automotive-web-scraping-Data
from selenium import webdriver 
import chromedriver_autoinstaller # type: ignore
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
product_codes = [
    "VCCT77421A2C",
    "A0694214000",
    "VCCT1000899G",
    "05137713AA",
    "68050126AB",
    "BC3Z19860G",
    "85163204"
]

# Prepare the Excel workbook and sheet
workbook = Workbook()
sheet = workbook.active
sheet.title = 'Product Data'
sheet.append(['product_code', 'brand', 'part_number', 'category', 'price', 'image_filename'])  # Write headers

for part in product_codes:
    try:
        driver.get("https://www.rockauto.com/en/partsearch/")
        time.sleep(2)
        
        search_input = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/main/table/tbody/tr/td[1]/div[2]/div/div[1]/div/form/div/table/tbody[1]/tr[1]/td[2]/input")
        search_input.clear()
        search_input.send_keys(part + Keys.RETURN)
        time.sleep(2)

        # Loop through all results (if multiple results are present)
        while True:
            # Extract data for each result
            brand = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/main/table/tbody/tr/td[1]/div[2]/div/div[1]/div/div[3]/div/div/div[2]/div/form/div/div/table/tbody[3]/tr[1]/td[1]/div[2]/span[1]").text
            part_number = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/main/table/tbody/tr/td[1]/div[2]/div/div[1]/div/div[3]/div/div/div[2]/div/form/div/div/table/tbody[3]/tr[1]/td[1]/div[2]/span[2]").text
            category = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/main/table/tbody/tr/td[1]/div[2]/div/div[1]/div/div[3]/div/div/div[2]/div/form/div/div/table/tbody[3]/tr[1]/td[1]/div[3]/span/span").text.split("Category: ")[1]
            price = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/main/table/tbody/tr/td[1]/div[2]/div/div[1]/div/div[3]/div/div/div[2]/div/form/div/div/table/tbody[3]/tr[1]/td[3]/span/span/span").text

            # Write data to Excel
            sheet.append([part, brand, part_number, category, price, image_filename])

            # Check if there is a "next" button for more results
            try:
                next_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")
                next_button.click()
                time.sleep(2)
            except:
                # If there is no "next" button, break the loop
                break

    except Exception as e:
        print(f"Error processing {part}: {e}")
        continue

# Save the Excel file and close the browser
workbook.save("product_data.xlsx")
driver.quit()
