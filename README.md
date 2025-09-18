# Automotive Parts Web Scraper

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.15+-green.svg)](https://selenium-python.readthedocs.io/)

A robust web scraping tool designed to extract automotive parts data from RockAuto.com. This scraper efficiently collects product information including brand names, part numbers, categories, and pricing data for specified automotive components.

## 🚀 Features

- **Automated Data Extraction**: Scrapes product details from RockAuto.com using Selenium WebDriver
- **Robust Error Handling**: Comprehensive exception handling and logging for reliable operation
- **Excel Output**: Saves collected data in a structured Excel format for easy analysis
- **Configurable Product Codes**: Easy modification of target product codes for scraping
- **Respectful Scraping**: Implements delays between requests to avoid overwhelming the target server
- **Detailed Logging**: Comprehensive logging system for monitoring scraping progress and debugging

## 📋 Prerequisites

Before running the scraper, ensure you have the following installed:

- Python 3.7 or higher
- Google Chrome browser (latest version recommended)
- pip (Python package installer)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mazenibrahem1/Automotive-web-scraping-Data.git
   cd Automotive-web-scraping-Data
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

### Basic Usage

Run the scraper with default settings:

```bash
python scraper.py
```

### Configuration

The scraper comes pre-configured with a set of automotive part codes. To modify the target products, edit the `product_codes` list in the `AutomotivePartsScraper` class:

```python
self.product_codes = [
    "VCCT77421A2C",
    "A0694214000", 
    "VCCT1000899G",
    "05137713AA",
    "68050126AB",
    "BC3Z19860G",
    "85163204"
]
```

### Headless Mode

To run the scraper in headless mode (without opening a browser window):

```python
scraper = AutomotivePartsScraper(headless=True)
```

## 📊 Output

The scraper generates an Excel file (`data/product_data.xlsx`) containing the following information:

| Column | Description |
|--------|-------------|
| product_code | The original search term/product code |
| brand | Manufacturer or brand name |
| part_number | Specific part number |
| category | Product category |
| price | Current price |
| image_filename | Placeholder for associated image filename |

## 📁 Project Structure

```
Automotive-web-scraping-Data/
├── scraper.py              # Main scraping script
├── requirements.txt        # Python dependencies
├── data/                  # Output directory for Excel files
│   └── product_data.xlsx  # Generated data file
├── scraper.log           # Logging output (generated during execution)
├── README.md             # Project documentation
└── LICENSE               # MIT License file
```

## 🔍 How It Works

1. **Initialization**: Sets up Chrome WebDriver with optimized options
2. **Product Search**: Navigates to RockAuto.com and searches for each product code
3. **Data Extraction**: Uses CSS selectors to extract product information from search results
4. **Data Processing**: Structures the extracted data into a standardized format
5. **Excel Export**: Saves all collected data to an Excel file with proper formatting
6. **Logging**: Records all operations, successes, and errors for monitoring and debugging

## ⚠️ Important Disclaimers

### Web Scraping Ethics
- This tool is designed for educational and research purposes
- Always respect the target website's robots.txt file and terms of service
- Implement appropriate delays between requests to avoid overwhelming servers
- Consider reaching out to website owners for permission when scraping large amounts of data

### Legal Considerations
- Web scraping may be subject to legal restrictions depending on your jurisdiction
- Always review and comply with the target website's terms of service
- Use scraped data responsibly and in accordance with applicable laws

## 🛠️ Troubleshooting

### Common Issues

**Chrome Driver Issues**
- The script automatically installs the appropriate ChromeDriver version
- Ensure Google Chrome is installed and up to date

**Element Not Found Errors**
- Website structure may have changed; selectors might need updating
- Check the scraper.log file for detailed error information

**Timeout Errors**
- Increase the `wait_timeout` value in the scraper configuration
- Check your internet connection stability

### Logging

The scraper creates detailed logs in `scraper.log`. Check this file for:
- Scraping progress updates
- Error messages and stack traces
- Performance metrics

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes with appropriate tests
4. Update documentation as needed
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mazen Ibrahim**
- GitHub: [@Mazenibrahem1](https://github.com/Mazenibrahem1)

## 🙏 Acknowledgments

- [Selenium WebDriver](https://selenium-python.readthedocs.io/) for web automation capabilities
- [OpenPyXL](https://openpyxl.readthedocs.io/) for Excel file manipulation
- [ChromeDriver Autoinstaller](https://pypi.org/project/chromedriver-autoinstaller/) for automated driver management

---

**Note**: This scraper is designed to work with RockAuto.com's current structure. Website changes may require updates to the scraping selectors and logic.

