# LinkedIn Profile Scraper

A simple Python script that uses Selenium to scrape basic information (name and title) from a list of LinkedIn profile URLs.

## Features

- Reads LinkedIn profile URLs from `profiles.txt`
- Extracts the name and job title from each profile
- Saves the scraped data into `output.csv`
- Uses Selenium and Chrome WebDriver for browser automation
- Includes basic error handling for missing elements

## Prerequisites

- Python 3.7 or higher
- Google Chrome installed
- ChromeDriver installed and added to your system PATH (matching your Chrome version)
- Selenium Python package

## Installation

1. Install Selenium via pip:

2. Download and install ChromeDriver from [here](https://sites.google.com/chromium.org/driver/) and ensure it matches your Chrome browser version.

3. Place `chromedriver` executable in your PATH or in the same folder as the script.

## Usage

1. Prepare a `profiles.txt` file in the same directory as the script. Add one LinkedIn profile URL per line. Example:

2. Run the Python script:

3. The script will open Chrome, visit each profile, scrape the name and title, and store the results in `output.csv`.

4. After completion, the console will print:


## Notes

- The script waits 3 seconds for page loading. Adjust the `time.sleep(3)` for slower/loading profiles.
- Make sure you are logged in to LinkedIn in Chrome or your scraper may be blocked or see limited info.
- This scraper extracts only basic public profile summary info (name and title).

## License

This project is licensed under the MIT License.

---

Feel free to expand the scraper to extract more profile details or improve error handling and headless browsing.


