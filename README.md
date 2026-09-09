# Black-Scholes Option Pricing Engine

A professional and interactive web application for pricing European options using the Black-Scholes-Merton model. Built with Streamlit, Plotly, and Python.

## Live Demo

You can access the live application here:  
[https://bs-option-pricing.streamlit.app](https://bs-option-pricing.streamlit.app)

---

## Overview

The **Black-Scholes Option Pricing Engine** is a fully interactive web application designed to help users understand and compute the theoretical price of European options, along with their corresponding risk sensitivities (Greeks). It features a custom, clean green theme and extensive interactive visualizations.

---

## Features

- **European Call & Put Pricing**: Accurate calculation using the Black-Scholes formula.
- **Greeks Calculation**: Complete risk metrics including Delta, Gamma, Vega, Theta, and Rho for both Call and Put options.
- **Interactive Visualizations** (5 powerful tabs):
  - **Price vs S**: Sensitivity of option prices to the underlying asset price.
  - **Heatmap**: Call price sensitivity to both Asset Price and Volatility.
  - **Greeks**: Visualizing Delta, Gamma, and Vega sensitivity curves.
  - **3D Surface**: 3D visualization of Call price vs Time and Asset Price.
  - **Put-Call Parity**: Verifying the consistency of the model.
- **Custom Green Theme**: A modern, professional, and user-friendly interface with custom CSS.
- **Responsive Design**: Fully functional on desktop and mobile devices.

---

## Technologies Used

- [Streamlit](https://streamlit.io/) - Web Application Framework
- [Plotly](https://plotly.com/python/) - Interactive Visualizations
- [NumPy](https://numpy.org/) - Numerical Computing
- [SciPy](https://scipy.org/) - Statistical Functions

---

## Project Structure

```text
black-scholes-option-pricing/
├── app.py                 # Main Streamlit application file
├── black_scholes.py       # Core mathematical model and Greeks logic
├── visualizations.py      # Plotly chart generation functions
├── style.css              # Custom styling (Green Theme)
├── .streamlit/
│   └── config.toml        # Streamlit configuration
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Installation (Local)

1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/erfan2mohammadi22/black-scholes-option-pricing.git
   cd black-scholes-option-pricing
   ```

2. **Create a virtual environment (Recommended):**
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. Open your browser and navigate to `http://localhost:8501`.
2. Set the Option Parameters (Spot Price, Strike Price, Time, Risk-Free Rate, Volatility).
3. Click **"Calculate Option Price"** to view immediate results.
4. Explore the interactive **Greeks** and **Sensitivity Analysis** charts.

---

## Author

**Erfan Mohammadi**

* **Telegram:** [@ERFANmmmig29](https://t.me/ERFANmmmig29)
* **GitHub:** [erfan2mohammadi22](https://github.com/erfan2mohammadi22)
* **LinkedIn:** [erfan2mohammadi22](https://www.linkedin.com/in/erfan2mohammadi22)
* **Email:** [erfan2mohammadi@gmail.com](mailto:erfan2mohammadi@gmail.com)

---

## Disclaimer

> **Note:** This project is for educational purposes only. It is not intended for real trading decisions. Use at your own risk.


