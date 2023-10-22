# mtg-card-track
Dashboard to locally parse Magic the Gathering cards and visualize their prices 

## Overview

This is an interactive dashboard built in Python 3.11 using the Dash web framework. It's designed to parse MTGJSON's data and visualize card prices over time. Magic: The Gathering (MTG) enthusiasts and traders can use this dashboard to explore the historical price trends of their favorite Magic cards. The dashboard allows users to select cards, view price history, and customize the display to gain valuable insights.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Dashboard Structure](#dashboard-structure)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Features

- View historical price data for Magic: The Gathering cards.
- Interactive selection of cards from MTGJSON's data.
- Line charts to display card price history.
- Customization options for chart display.
- Easily export and share charts.

## Getting Started

To get started with the MTG Card Price Dashboard, make sure you have Python 3.11 installed on your system.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/mtg-card-price-dashboard.git
   ```

2. Change your current directory to the project folder:

   ```bash
   cd mtg-card-price-dashboard
   ```

3. Create a virtual environment (recommended):

   ```bash
   python3.11 -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the dashboard by running the following command:

   ```bash
   python app/app.py
   ```

2. Open a web browser and navigate to `http://127.0.0.1:8050/` to access the dashboard.

3. Use the interactive features to explore Magic card prices over time.

## Dashboard Structure

The dashboard consists of the following components:

- **Card Selection**: Use the dropdown menu to select a Magic: The Gathering card. The card's name, set, and legality will be displayed.

- **Price Chart**: This area displays a line chart showing the historical price trends for the selected card. Users can zoom in and out, hover over data points to view prices for specific dates, and export the chart as an image.

## Customization

The dashboard allows for some customization:

- **Date Range**: Use the date range slider to focus on a specific time period.

- **Chart Type**: Choose between line, bar, and scatter charts for different visualizations.

- **Price Scale**: Toggle between linear and logarithmic scales for the price axis.

## Contributing

Contributions are welcome! If you'd like to improve this dashboard or fix any issues, please follow these steps:

1. Fork the repository.

2. Create a new branch for your changes:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes, commit them, and push to your fork.

4. Create a pull request on the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Happy trading and enjoy exploring the historical prices of Magic: The Gathering cards with the MTG Card Price Dashboard!
