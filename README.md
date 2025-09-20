# Weather Logger

Weather Logger is a Python automation script that fetches real-time weather data from the OpenWeatherMap API and logs it into a Google Sheet. This allows for the creation of a personal, automated weather history for any specified location.

---

## Features

-   Fetches current temperature and weather description from any city.
-   Automatically appends new data with a timestamp to a Google Sheet.
-   Securely handles API keys and credentials using environment variables.
-   Logs data in a clean, CSV-like format within the sheet: `Timestamp, City, Temperature (°C), Description`.

---

## Setup Guide

### Prerequisites

-   Python 3.6+
-   A Google Cloud Platform (GCP) account with a project set up.
-   An OpenWeatherMap account.

### 1. Installation & Dependencies

Clone the repository and install the required Python libraries.

1.  **Create a `requirements.txt` file** with the following content:
    ```
    gspread
    oauth2client
    requests
    ```

2.  **Install the libraries** using pip:
    ```bash
    pip install -r requirements.txt
    ```

### 2. Google Sheets & API Configuration

This project requires a Google Cloud Service Account to programmatically access your Google Sheet.

1.  **Enable APIs:** In your GCP project, enable the **Google Drive API** and the **Google Sheets API**.
2.  **Create a Service Account:**
    -   Navigate to "Credentials" in your GCP project.
    -   Click "Create Credentials" -> "Service account."
    -   Give it a name (e.g., "weather-logger-bot") and grant it the "Editor" role.
    -   Create the account, and when prompted, create and download a JSON key.
3.  **Rename the Key:** Rename the downloaded JSON file to `credentials.json` and place it in your project's root directory.
4.  **Create a Google Sheet:**
    -   Create a new, blank Google Sheet. You can name it "WeatherData."
    -   Find the `client_email` address inside your `credentials.json` file.
    -   Click the "Share" button in your Google Sheet, paste the `client_email`, and give it **Editor** permissions.

### 3. OpenWeatherMap API Key

1.  Log in to your [OpenWeatherMap account](https://home.openweathermap.org/).
2.  Navigate to the "My API Keys" tab and copy your default key. Note that it may take up to 2 hours for a new key to become active.

## Configuration

The script is configured using environment variables to keep your secret keys out of the code.

1.  **API Key:** In your terminal, set the environment variable for your OpenWeatherMap API key.
    -   **Windows (Command Prompt):**
        ```bash
        set OPENWEATHER_API_KEY=your_actual_api_key
        ```
    -   **macOS / Linux:**
        ```bash
        export OPENWEATHER_API_KEY="your_actual_api_key"
        ```

2.  **City (Optional):** You can also specify the city. The script defaults to Bengaluru if this is not set.
    -   **Windows (Command Drompt):**
        ```bash
        set WEATHER_CITY=London
        ```
    -   **macOS / Linux:**
        ```bash
        export WEATHER_CITY="London"
        ```

**Note:** Environment variables set this way are temporary and only last for the current terminal session.

## Usage

Once all the configuration steps are complete, simply run the Python script from your terminal:

```bash
python weather_logger.py
