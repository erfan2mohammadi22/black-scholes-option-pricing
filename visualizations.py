"""
Plotly visualization functions for the Black-Scholes application.
"""
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from black_scholes import black_scholes_call, black_scholes_put, calculate_greeks

def plot_price_sensitivity(S: float, K: float, T: float, r: float, sigma: float) -> go.Figure:
    """Plot Call and Put option prices against varying underlying asset prices."""
    S_range = np.linspace(max(S * 0.5, 0.1), S * 1.5, 150)
    call_prices = [black_scholes_call(s, K, T, r, sigma) for s in S_range]
    put_prices = [black_scholes_put(s, K, T, r, sigma) for s in S_range]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=S_range, y=call_prices, mode='lines',
        name='Call Option', line=dict(color='#2D6B4A', width=4),
        fill='tozeroy', fillcolor='rgba(45,107,74,0.1)'
    ))

    fig.add_trace(go.Scatter(
        x=S_range, y=put_prices, mode='lines',
        name='Put Option', line=dict(color='#C47A2A', width=4),
        fill='tozeroy', fillcolor='rgba(196,122,42,0.1)'
    ))

    fig.add_vline(
        x=S, line_dash="dash", line_color="#2A5A2A",
        annotation_text=f"Current S: {S}", annotation_position="top",
        annotation_font=dict(color="#1A3F1A", size=13)
    )

    fig.update_layout(
        title=dict(text="<b>Option Price vs Underlying Asset Price</b>", font=dict(size=20, color="#1A2B1A")),
        xaxis_title="Asset Price (S)", yaxis_title="Option Price",
        template="plotly_white", height=450, hovermode="x unified",
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#2A3F2A", size=13),
        legend=dict(font=dict(color="#2A3F2A", size=13), bgcolor="rgba(255,255,255,0.8)",
                    bordercolor="rgba(186,200,177,0.3)", borderwidth=1)
    )
    return fig

def plot_sensitivity_heatmap(S: float, K: float, T: float, r: float, sigma: float) -> go.Figure:
    """Plot a heatmap of Call prices against Asset Price and Volatility."""
    S_range = np.linspace(S * 0.7, S * 1.3, 25)
    sigma_range = np.linspace(0.01, 0.8, 25)

    prices = np.zeros((len(S_range), len(sigma_range)))
    for i, s in enumerate(S_range):
        for j, sig in enumerate(sigma_range):
            prices[i, j] = black_scholes_call(s, K, T, r, sig)

    fig = go.Figure(data=go.Heatmap(
        z=prices, x=sigma_range, y=S_range,
        colorscale=[[0, '#D4E8D0'], [0.3, '#8BB89A'], [0.6, '#4A7A5A'], [1, '#1A4F2A']],
        colorbar=dict(title="Call Price", tickfont=dict(color="#1A2B1A", size=12),
                      title_font=dict(color="#1A2B1A", size=13)),
        hovertemplate='S: %{y:.2f}<br>σ: %{x:.2f}<br>Price: %{z:.2f}<extra></extra>'
    ))
    fig.update_layout(
        title=dict(text="<b>Heatmap: Call Price vs S & σ</b>", font=dict(size=20, color="#1A2B1A")),
        xaxis_title="Volatility (σ)", yaxis_title="Asset Price (S)",
        height=450, template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#2A3F2A", size=13)
    )
    return fig

def plot_greeks_sensitivity(S: float, K: float, T: float, r: float, sigma: float) -> go.Figure:
    """Plot Delta, Gamma, and Vega sensitivity against the underlying asset price."""
    S_range = np.linspace(max(S * 0.5, 0.1), S * 1.5, 120)
    call_greeks = {'delta': [], 'gamma': [], 'vega': [], 'theta': [], 'rho': []}
    put_greeks = {'delta': [], 'gamma': [], 'vega': [], 'theta': [], 'rho': []}

    for s in S_range:
        g_c = calculate_greeks(s, K, T, r, sigma, 'call')
        g_p = calculate_greeks(s, K, T, r, sigma, 'put')
        for key in call_greeks:
            call_greeks[key].append(g_c[key])
            put_greeks[key].append(g_p[key])

    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=("<b>Delta (Δ)</b> – Price Sensitivity",
                        "<b>Gamma (Γ)</b> – Delta Change Rate",
                        "<b>Vega (ν)</b> – Volatility Sensitivity"),
        shared_xaxes=True, vertical_spacing=0.12
    )

    # Delta
    fig.add_trace(go.Scatter(x=S_range, y=call_greeks['delta'], mode='lines', name='Call Delta',
                             line=dict(color='#4A7A8A', width=3.5)), row=1, col=1)
    fig.add_trace(go.Scatter(x=S_range, y=put_greeks['delta'], mode='lines', name='Put Delta',
                             line=dict(color='#B84A3A', width=3.5, dash='dash')), row=1, col=1)

    # Gamma
    fig.add_trace(go.Scatter(x=S_range, y=call_greeks['gamma'], mode='lines', name='Gamma',
                             line=dict(color='#B88A2A', width=3.5)), row=2, col=1)

    # Vega
    fig.add_trace(go.Scatter(x=S_range, y=call_greeks['vega'], mode='lines', name='Vega',
                             line=dict(color='#2A8A7A', width=3.5)), row=3, col=1)

    # Vertical line at current S
    for row in [1, 2, 3]:
        fig.add_vline(x=S, line_dash="dash", line_color="#4A7A5A", row=row, col=1)

    fig.update_layout(
        height=700, template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#2A3F2A", size=13),
        showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=1.02)
    )
    fig.update_xaxes(title_text="Asset Price (S)", row=3, col=1, title_font=dict(color="#1A2B1A", size=14))
    fig.update_yaxes(title_text="Δ", row=1, col=1, title_font=dict(color="#1A2B1A", size=14))
    fig.update_yaxes(title_text="Γ", row=2, col=1, title_font=dict(color="#1A2B1A", size=14))
    fig.update_yaxes(title_text="ν", row=3, col=1, title_font=dict(color="#1A2B1A", size=14))

    return fig

def plot_3d_surface(S: float, K: float, T: float, r: float, sigma: float) -> go.Figure:
    """Plot a 3D surface of Call prices against Asset Price and Time."""
    S_range = np.linspace(S * 0.5, S * 1.5, 40)
    T_range = np.linspace(0.1, 2.0, 40)
    prices = np.zeros((len(S_range), len(T_range)))

    for i, s in enumerate(S_range):
        for j, t in enumerate(T_range):
            prices[i, j] = black_scholes_call(s, K, t, r, sigma)

    fig = go.Figure(data=[go.Surface(z=prices, x=T_range, y=S_range, colorscale='Greens')])
    fig.update_layout(
        title=dict(text="<b>Call Price Surface: S vs T</b>", font=dict(size=20, color="#1A2B1A")),
        scene=dict(xaxis_title="Time (T)", yaxis_title="Asset Price (S)", zaxis_title="Call Price",
                   bgcolor='rgba(0,0,0,0)'),
        height=500, template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#2A3F2A", size=13)
    )
    return fig

def plot_put_call_parity(S: float, K: float, T: float, r: float, sigma: float) -> go.Figure:
    """Plot the residual of the Put-Call parity to check model consistency."""
    S_range = np.linspace(max(S * 0.5, 0.1), S * 1.5, 100)
    call = [black_scholes_call(s, K, T, r, sigma) for s in S_range]
    put = [black_scholes_put(s, K, T, r, sigma) for s in S_range]
    parity = [c - p - (s - K * np.exp(-r * T)) for s, c, p in zip(S_range, call, put)]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=S_range, y=parity, mode='lines', name='Call - Put - S + K·e^(-rT)',
                             line=dict(color='#7B9669', width=3)))
    fig.add_hline(y=0, line_dash="dash", line_color="#B84A3A")
    fig.update_layout(
        title=dict(text="<b>Put-Call Parity Check</b>", font=dict(size=20, color="#1A2B1A")),
        xaxis_title="Asset Price (S)", yaxis_title="Parity Residual",
        template="plotly_white", height=400,
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#2A3F2A", size=13)
    )
    return fig