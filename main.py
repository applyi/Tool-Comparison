from loguru import logger
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from Timer.timer import timer
from Scripts.SE import SeleniumScraper
from Scripts.PW import PlaywrightScraper

def main() -> None:
    try:
        # Selenium setup
        logger.info("Starting Selenium scraper...")
        selenium_scraper = SeleniumScraper()
        selenium_time = timer(selenium_scraper)
        logger.info(f"Selenium scraping time: {selenium_time} ns")
    except Exception as e:
        logger.error(f"Selenium scraper failed: {e}")

    try:
        # Playwright setup
        logger.info("Starting Playwright scraper...")
        playwright_scraper = PlaywrightScraper()
        playwright_time = timer(playwright_scraper)
        logger.info(f"Playwright scraping time: {playwright_time} ns")
    except Exception as e:
        logger.error(f"Playwright scraper failed: {e}")

if __name__ == "__main__":
    main()
