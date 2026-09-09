# Black-Scholes Option Pricing Engine

A professional and interactive web application for pricing European options using the Black-Scholes-Merton model. Built with Streamlit, Plotly, and Python.

## Features

- **European Call & Put Pricing**: Accurate calculation using Black-Scholes formula
- **Greeks Calculation**: Delta, Gamma, Vega, Theta, and Rho for both Call and Put options
- **Interactive Visualizations**:
  - Price sensitivity vs underlying asset price
  - Heatmap of call price vs volatility and asset price
  - Greeks sensitivity analysis (Delta, Gamma, Vega)
  - 3D surface plot of call price vs time and asset price
  - Put-Call parity check
- **Custom Green Theme**: A clean, modern, and professional user interface
- **Responsive Design**: Works on desktop and mobile devices

## Technologies Used

- [Streamlit](https://streamlit.io/) - Web application framework
- [Plotly](https://plotly.com/python/) - Interactive visualizations
- [NumPy](https://numpy.org/) - Numerical computing
- [SciPy](https://scipy.org/) - Statistical functions
- [Black-Scholes Model](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model) - Option pricing theory

## Installation

1. Clone the repository:
   
   ```bash
   git clone https://github.com/erfan2mohammadi22/black-scholes-option-pricing.git
   cd black-scholes-option-pricing
   ```

2. Create a virtual environment (optional but recommended):
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open your browser and go to `http://localhost:8501`
2. Set the option parameters (Spot Price, Strike Price, Time, Risk-Free Rate, Volatility)
3. Click **"Calculate Option Price"** to see the results
4. Explore the interactive charts and Greeks

## Screenshots

*Add screenshots of your app here if available*

## Author

**Erfan Mohammadi**

- Telegram: [@ERFANmmmig29](https://t.me/ERFANmmmig29)
- GitHub: [erfan2mohammadi22](https://github.com/erfan2mohammadi22)
- LinkedIn: [erfan2mohammadi22](https://www.linkedin.com/in/erfan2mohammadi22)
- Email: [erfan2mohammadi@gmail.com](mailto:erfan2mohammadi@gmail.com)

## License

This project is for **educational purposes only** and is not intended for real trading decisions. Use at your own risk.
