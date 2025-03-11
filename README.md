# Motivational Quote Generator
The Motivational Quote Generator is a simple web application that fetches and displays a random motivational quote every time the user clicks the "Fetch Quote" button. The app runs locally on your machine and retrieves quotes from a pre-built SQLite database created using a scraper.


## Key Technologies
+ **Backend**: Python, Flask, SQLite3
+ **Frontend**: HTML, CSS, JavaScript
+ **Scraping**: BeautifulSoup, Requests
+ **Database**: SQLite3
+ **CORS Handling**: Flask-CORS


## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)


### Installation
To get this project up and running locally, follow these steps:

**1. Clone the repository:**

```bash
git clone https://github.com/username/motivational-quote-generator.git
```

**2. Navigate to the project folder:**

```bash
cd motivational-quote-generator
```

**3. Install the required dependencies: You'll need to install Python and some Python libraries for the backend to work properly:**

```bash
pip install flask flask_cors requests beautifulsoup4
```

**4. Make sure the following files are in your project directory:**

+ `quotes-proj.db` (The SQLite3 database containing the quotes)
+ `app.py` (Flask backend server)
+ `index.html` (Frontend HTML)
+ `style.css` (Styling for the app)
+ `script.js` (Frontend logic)
+ `linkedin.svg`, `mail.svg`, `call.svg` (Icons for the app)
+ Optionally, if you want to create your own `quotes-proj.db` database, you can download `scrape_quotes.py` and run it to scrape new quotes from Shopify Blog.


## Usage
Once the project is installed, follow these steps to run the app locally:

1. **Start the backend server** by running `app.py`:

```bash
python app.py
```

2. **Open** `index.html` in your browser. It should load the page where you'll see the "Fetch Quote" button.

3. **Click the "Fetch Quote" button** on the page, and a random motivational quote (with its author) will be displayed.


### Requirements for Running `app.py`:
+ Python 3.x
+ Required Python libraries: `sqlite3`, `random`, `flask`, `flask_cors`, `jsonify`

To install the libraries, you can run:

```bash
pip install flask flask_cors requests beautifulsoup4
```

## Features
+ **Fetch Random Quotes**: Displays a random motivational quote along with its author when the user clicks the button.
+ **Simple Interface**: Clean and simple web interface.
+ **SQLite3 Database**: Quotes are stored in a local SQLite3 database (`quotes-proj.db`), which can be updated using the scraper.
+ **Customizable**: You can add or update quotes in the database by using the `scrape_quotes.py` script.


## Contributing
At this time, contributing to this project is not required. However, feel free to fork the repository and make improvements or create pull requests for enhancements!


## License
This project is open-source and free to use under the MIT License.


## Acknowledgements
+ **Requests**: To handle HTTP requests for the scraping process.
+ **BeautifulSoup**: For scraping quotes from the Shopify Blog.
+ **SQLite3**: For storing quotes in a local database.
+ **Flask**: For creating the web server to handle API requests.
+ **Flask-CORS**: For handling Cross-Origin Resource Sharing (CORS).
