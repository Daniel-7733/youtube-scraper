import time
import csv
from typing import List, Tuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fetch_video_data(driver: webdriver.Chrome, count: int = 5) -> List[Tuple[str, str]]:
    """
    Fetch video titles and view counts from YouTube search results.

    :param driver: A Selenium WebDriver instance
    :param count: Number of videos to extract
    :return: A list of tuples: [(title, views), ...]
    """
    video_data: List[Tuple[str, str]] = []

    videos: List[WebElement] = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "ytd-video-renderer"))
    )

    for video in videos[:count]:
        try:
            title: str = video.find_element(By.ID, "video-title").text
            view_elements: List[WebElement] = video.find_elements(
                By.CSS_SELECTOR, ".inline-metadata-item.style-scope.ytd-video-meta-block"
            )
            views: str = view_elements[0].text if view_elements else "N/A"
            video_data.append((title, views))
        except Exception as e:
            print("Skipping a video due to error:", e)

    return video_data


def save_to_csv(data: List[Tuple[str, str]], filename: str = "youtube.csv") -> None:
    """
    Save a list of (title, views) pairs to a CSV file.

    :param data: List of tuples containing title and view count
    :param filename: CSV filename
    :return: None
    """
    with open(filename, "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Title", "Views"])
        for title, views in data:
            writer.writerow([title, views])


def main() -> None:
    """
    Orchestrates the scraping process.
    :return: None
    """
    driver: webdriver.Chrome = webdriver.Chrome()

    try:
        driver.get('https://www.youtube.com/')

        # Wait and search
        search_box: WebElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        search_box.send_keys("AI project ideas" + Keys.ENTER)

        # Wait for search results and scrape video data
        video_info: List[Tuple[str,str]] = fetch_video_data(driver, count=5)

        # Save results
        save_to_csv(video_info)

        time.sleep(5)

    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()


if __name__ == '__main__':
    main()
