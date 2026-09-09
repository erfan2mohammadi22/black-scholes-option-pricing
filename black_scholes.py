"""
Black-Scholes Option Pricing Model.
Contains functions for pricing European call and put options,
calculating Greeks, and verifying Put-Call parity.
"""
import numpy as np
from scipy.stats import norm

def _d1(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calculate the d1 term in the Black-Scholes formula.
    """
    return (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

def _d2(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calculate the d2 term in the Black-Scholes formula.
    """
    return _d1(S, K, T, r, sigma) - sigma * np.sqrt(T)

def black_scholes_call(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calculate the price of a European call option.

    Args:
        S: Spot price of the underlying asset.
        K: Strike price.
        T: Time to maturity in years.
        r: Risk-free interest rate.
        sigma: Annual volatility.

    Returns:
        The theoretical call option price.
    """
    if sigma <= 0 or T <= 0:
        return max(S - K, 0)
    d1 = _d1(S, K, T, r, sigma)
    d2 = _d2(S, K, T, r, sigma)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def black_scholes_put(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calculate the price of a European put option.

    Args:
        S: Spot price of the underlying asset.
        K: Strike price.
        T: Time to maturity in years.
        r: Risk-free interest rate.
        sigma: Annual volatility.

    Returns:
        The theoretical put option price.
    """
    if sigma <= 0 or T <= 0:
        return max(K - S, 0)
    d1 = _d1(S, K, T, r, sigma)
    d2 = _d2(S, K, T, r, sigma)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

def calculate_greeks(S: float, K: float, T: float, r: float, sigma: float, option_type: str = 'call') -> dict:
    """
    Calculate the Greeks for a European option.

    Args:
        S: Spot price.
        K: Strike price.
        T: Time to maturity.
        r: Risk-free rate.
        sigma: Volatility.
        option_type: 'call' or 'put'.

    Returns:
        Dictionary containing delta, gamma, vega, theta, and rho.
    """
    if sigma <= 0 or T <= 0:
        # Handle degenerate cases to avoid division by zero
        if option_type == 'call':
            delta = 1 if S > K else 0
            gamma = 0; vega = 0; theta = 0; rho = 0
        else:
            delta = -1 if S < K else 0
            gamma = 0; vega = 0; theta = 0; rho = 0
        return {'delta': delta, 'gamma': gamma, 'vega': vega, 'theta': theta, 'rho': rho}

    d1 = _d1(S, K, T, r, sigma)
    d2 = _d2(S, K, T, r, sigma)

    # Common Greeks
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T) / 100

    if option_type == 'call':
        delta = norm.cdf(d1)
        theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * norm.cdf(d2)) / 252
        rho = K * T * np.exp(-r * T) * norm.cdf(d2) / 100
    else:  # put
        delta = norm.cdf(d1) - 1
        theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * norm.cdf(-d2)) / 252
        rho = -K * T * np.exp(-r * T) * norm.cdf(-d2) / 100

    return {'delta': delta, 'gamma': gamma, 'vega': vega, 'theta': theta, 'rho': rho}

def put_call_parity(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Check the Put-Call parity relationship.

    Returns:
        The difference between Call - Put and (S - K * e^(-rT)).
    """
    call = black_scholes_call(S, K, T, r, sigma)
    put = black_scholes_put(S, K, T, r, sigma)
    return call - put - (S - K * np.exp(-r * T))