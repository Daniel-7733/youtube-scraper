# youtube-scraper
Youtube Scraper

A minimal Python script that uses **Selenium** to search YouTube, grab the titles + view counts of the first _N_ results, and save them to a CSV file.

![demo](docs/demo.gif) <!-- feel free to delete this line or add a real GIF later -->

---

## Features
- 🔍 Searches YouTube for any keyword you choose  
- 📄 Extracts video **title** and **views** together (keeps them in sync)  
- 💾 Saves results to **`youtube.csv`** using the safe built-in `csv` module  
- 🧩 Clean, modular code with docstrings and type hints—easy to extend  
- 🪄 Ready for GUI or `.exe` packaging later

---

## Requirements
| Tool | Tested Version |
|------|----------------|
| Python | 3.10 + |
| Selenium | 4.x |
| Chrome | Latest |
| ChromeDriver | Matching your Chrome version |

> **Tip:** Put `chromedriver.exe` on your system PATH or in the same folder as the script.

Install Python packages:

```bash
pip install selenium
```

## Usage
python youtube-scraper.py

# Change the search term or number of videos
search_box.send_keys("machine learning tutorials" + Keys.ENTER)
video_info = fetch_video_data(driver, count=10)

## Output
Title;Views
Awesome ML Tutorial for Beginners;1.2M views
How To Build a Neural Network in Python;845K views
...

## Contributing
Pull requests are welcome! If you spot a bug or have an idea, open an issue first.


## License

---

**Next steps**

1. Create **README.md** in the repo and paste the content.  
2. Commit the file.  
3. If you ever add screenshots/GIFs, drop them in a `/docs` folder and update the image link at the top.

Let me know if you’d like any tweaks or a quick guide on adding a license file or `.gitignore`!

