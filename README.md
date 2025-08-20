🎬 IMDb Movie Rating Scraper

A lightweight Python automation tool that scrapes IMDb’s Top 250 Movies list and exports the data into a structured CSV file.
Built with Selenium WebDriver and pandas, this project demonstrates browser automation, dynamic web scraping, and data handling.

✨ Features

🔎 Automatically extracts Rank, Title, Year, and IMDb Rating

⚡ Handles JavaScript-rendered content using Selenium

🗂️ Saves results in a CSV file for easy analysis

🖥️ Runs in both headless (background) and normal browser modes

📈 Data ready for analysis, dashboards, or recommendation engines

🛠️ Tech Stack

Python 3.10+ – core programming language

Selenium – browser automation & scraping dynamic content

pandas – data structuring and CSV export

webdriver-manager – automatically manages ChromeDriver

🚀 Installation

Clone the repository

git clone https://github.com/your-username/imdb-movie-rating-scraper.git
cd imdb-movie-rating-scraper


Install dependencies

pip install selenium pandas webdriver-manager


Make sure you have Google Chrome installed (latest version recommended).

▶️ Usage

Run the script:

python imdb_scraper.py


Output:

A file named imdb_top_250_updated.csv will be created in the project folder.

Columns: Rank | Title | Year | IMDb Rating

Example:

Rank	Title	Year	IMDb Rating
1	The Shawshank Redemption	1994	9.2
2	The Godfather	1972	9.2

🧩 How It Works

Launches Chrome via Selenium.

Navigates to IMDb’s Top 250 movies page.

Waits for the page to finish loading (JavaScript content).

Extracts details for each movie card.

Builds a pandas DataFrame.

Saves the data to CSV for reuse or analysis.

📜 License

This project is open-source and intended for educational use only. IMDb content belongs to IMDb.
