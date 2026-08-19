
# 📮 Postal PIN Code Finder

A simple Python-based web application that allows users to search for **Indian Post Office details using a 6-digit PIN Code**.

The application uses the **Postal PIN Code API** to fetch real-time post office information and displays the results in a clean web interface.

## 🚀 Features

* 🔢 Accepts a 6-digit Indian PIN Code
* ✅ Validates the entered PIN Code
* 🌐 Fetches data using Postal PIN Code API
* 📍 Displays Post Office details
* 💻 Opens automatically in the web browser
* ⚠️ Shows error messages for invalid or unavailable PIN Codes
* 🐍 Uses Python's built-in HTTP server
* 🎨 Includes a simple and responsive HTML/CSS interface

## 🛠️ Technologies Used

* **Python**
* **HTML**
* **CSS**
* **Postal PIN Code API**
* **Python HTTP Server**

### Python Libraries

* `http.server` — Creates the local web server
* `urllib.parse` — Reads the PIN Code from the URL
* `urllib.request` — Sends requests to the API
* `json` — Processes API response data
* `webbrowser` — Opens the application automatically in the browser
* `threading` — Opens the browser while the server starts

## 📂 Project Structure

```text
POSTAL_PIN_CODE_PROJECT/
│
├── postal_pin_code.py
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project folder

```bash
cd POSTAL_PIN_CODE_PROJECT
```

### 3. Run the Python file

```bash
python postal_pin_code.py
```

### 4. Open the application

The application automatically opens in the browser at:

```text
http://localhost:8000
```

## 🔍 How It Works

1. User enters a **6-digit PIN Code**.
2. Python receives the PIN Code through the URL.
3. The program validates whether the PIN Code contains exactly 6 digits.
4. A request is sent to the Postal PIN Code API.
5. The API returns the Post Office information in JSON format.
6. Python processes the JSON response.
7. The required details are converted into HTML.
8. The generated webpage is sent to the browser.

## 📋 Information Displayed

For each matching Post Office, the application displays:

* Post Office Name
* Branch Type
* Delivery Status
* District
* Division
* Region
* State
* Country

## ⚠️ Error Handling

The application handles:

* Invalid PIN Codes
* PIN Codes with fewer or more than 6 digits
* PIN Codes containing non-numeric characters
* PIN Codes that are not found
* Internet/API connection errors

## 🎯 Purpose of the Project

This project demonstrates how **Python can be used to create a simple web application and communicate with an external API**.

It also provides practical understanding of:

* API integration
* JSON data processing
* HTTP requests
* URL query parameters
* Web server creation
* Dynamic HTML generation

## 🔮 Future Improvements

Possible improvements include:

* Add search history
* Add loading animation
* Add dark mode
* Improve mobile responsiveness
* Add Google Maps integration
* Add PIN Code suggestions
* Display the location on an interactive map

## 👩‍💻 Author

**Raksha Sahu**

### ⭐ Project

**Postal PIN Code Finder**

Made with Python 🐍 and Postal PIN Code API 📮
