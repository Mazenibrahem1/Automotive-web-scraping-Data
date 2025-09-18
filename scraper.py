"""
Automotive Parts Web Scraper

This script scrapes automotive parts data from RockAuto.com using Selenium WebDriver.
It extracts product information including brand, part number, category, and price
for a predefined list of product codes and saves the data to an Excel file.

Author: Mazen Ibrahim
Date: 2024
"""

import logging
import time
from typing import List, Dict, Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import chromedriver_autoinstaller
from openpyxl import Workbook

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class AutomotivePartsScraper:
    """Web scraper for automotive parts data from RockAuto.com"""
    
    def __init__(self, headless: bool = False):
        """
        Initialize the scraper
        
        Args:
            headless (bool): Whether to run browser in headless mode
        """
        self.base_url = "https://www.rockauto.com/en/partsearch/"
        self.driver = None
        self.headless = headless
        self.wait_timeout = 10
        
        # Product codes to scrape
        self.product_codes = [
            "VCCT77421A2C",
            "A0694214000", 
            "VCCT1000899G",
            "05137713AA",
            "68050126AB",
            "BC3Z19860G",
            "85163204"
        ]
    
    def setup_driver(self) -> None:
        """Setup Chrome WebDriver with appropriate options"""
        try:
            chromedriver_autoinstaller.install()
            
            chrome_options = Options()
            if self.headless:
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            
            self.driver = webdriver.Chrome(options=chrome_options)
            logger.info("Chrome WebDriver initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to setup WebDriver: {e}")
            raise
    
    def scrape_product_data(self, product_code: str) -> List[Dict[str, Any]]:
        """
        Scrape data for a specific product code
        
        Args:
            product_code (str): The product code to search for
            
        Returns:
            List[Dict[str, Any]]: List of product data dictionaries
        """
        products_data = []
        
        try:
            logger.info(f"Scraping data for product code: {product_code}")
            
            # Navigate to search page
            self.driver.get(self.base_url)
            
            # Wait for search input to be available
            search_input = WebDriverWait(self.driver, self.wait_timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='partnum']"))
            )
            
            # Clear and enter search term
            search_input.clear()
            search_input.send_keys(product_code)
            search_input.send_keys(Keys.RETURN)
            
            # Wait for results to load
            WebDriverWait(self.driver, self.wait_timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".listing-inner"))
            )
            
            # Extract product information
            try:
                # Use more robust selectors
                brand_element = self.driver.find_element(By.CSS_SELECTOR, ".listing-text-row .brand")
                part_number_element = self.driver.find_element(By.CSS_SELECTOR, ".listing-text-row .part")
                category_element = self.driver.find_element(By.CSS_SELECTOR, ".listing-text-row .category")
                price_element = self.driver.find_element(By.CSS_SELECTOR, ".price")
                
                brand = brand_element.text.strip() if brand_element else "N/A"
                part_number = part_number_element.text.strip() if part_number_element else "N/A"
                category = category_element.text.replace("Category: ", "").strip() if category_element else "N/A"
                price = price_element.text.strip() if price_element else "N/A"
                
                product_data = {
                    'product_code': product_code,
                    'brand': brand,
                    'part_number': part_number,
                    'category': category,
                    'price': price,
                    'image_filename': f"{product_code}_image.jpg"  # Placeholder for image filename
                }
                
                products_data.append(product_data)
                logger.info(f"Successfully scraped data for {product_code}")
                
            except NoSuchElementException as e:
                logger.warning(f"Could not find product elements for {product_code}: {e}")
                # Add placeholder data for failed scrapes
                products_data.append({
                    'product_code': product_code,
                    'brand': 'N/A',
                    'part_number': 'N/A', 
                    'category': 'N/A',
                    'price': 'N/A',
                    'image_filename': 'N/A'
                })
                
        except TimeoutException:
            logger.error(f"Timeout while scraping {product_code}")
        except Exception as e:
            logger.error(f"Error scraping {product_code}: {e}")
            
        return products_data
    
    def save_to_excel(self, all_data: List[Dict[str, Any]], filename: str = "data/product_data.xlsx") -> None:
        """
        Save scraped data to Excel file
        
        Args:
            all_data (List[Dict[str, Any]]): List of all product data
            filename (str): Output Excel filename
        """
        try:
            # Create data directory if it doesn't exist
            import os
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = 'Product Data'
            
            # Write headers
            headers = ['product_code', 'brand', 'part_number', 'category', 'price', 'image_filename']
            sheet.append(headers)
            
            # Write data rows
            for product in all_data:
                row_data = [product.get(header, 'N/A') for header in headers]
                sheet.append(row_data)
            
            workbook.save(filename)
            logger.info(f"Data saved successfully to {filename}")
            
        except Exception as e:
            logger.error(f"Error saving to Excel: {e}")
            raise
    
    def run_scraper(self) -> None:
        """Main method to run the complete scraping process"""
        all_products_data = []
        
        try:
            self.setup_driver()
            logger.info("Starting automotive parts scraping process")
            
            for product_code in self.product_codes:
                try:
                    product_data = self.scrape_product_data(product_code)
                    all_products_data.extend(product_data)
                    
                    # Add delay between requests to be respectful
                    time.sleep(2)
                    
                except Exception as e:
                    logger.error(f"Failed to scrape {product_code}: {e}")
                    continue
            
            # Save all collected data
            if all_products_data:
                self.save_to_excel(all_products_data)
                logger.info(f"Scraping completed. Total products processed: {len(all_products_data)}")
            else:
                logger.warning("No data was collected during scraping")
                
        except Exception as e:
            logger.error(f"Critical error during scraping process: {e}")
            raise
        finally:
            if self.driver:
                self.driver.quit()
                logger.info("WebDriver closed")


def main():
    """Main function to run the scraper"""
    scraper = AutomotivePartsScraper(headless=False)  # Set to True for headless mode
    scraper.run_scraper()


if __name__ == "__main__":
    main()

