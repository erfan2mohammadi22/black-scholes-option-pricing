"""
Black-Scholes Option Pricing Engine - Streamlit Application.
"""
import streamlit as st
import numpy as np
import time

from black_scholes import black_scholes_call, black_scholes_put, calculate_greeks
import visualizations as viz

# ============================================
# Page Configuration
# ============================================
st.set_page_config(
    page_title="Black-Scholes Option Pricing",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# Load Custom CSS
# ============================================
def load_css() -> None:
    """Loads the external CSS file for custom styling."""
    with open("style.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ============================================
# Sidebar
# ============================================
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1.2rem 0 0.5rem 0;">
        <div style="font-size: 2.8rem; font-weight: 700; color: #4A7A5A; font-family: 'Space Grotesk', sans-serif;">
            BS
        </div>
        <h2 style="color: #1A2B1A; font-weight: 700; margin: 0.3rem 0; font-family: 'Space Grotesk', sans-serif;">
            Black-Scholes
        </h2>
        <p style="color: #3D5540; font-size: 0.75rem; letter-spacing: 2px; font-weight: 600;">
            OPTION PRICING ENGINE
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div class="sidebar-info">
        <p class="title">MODEL PARAMETERS</p>
        <div class="sidebar-param">
            <span class="label">S</span>
            <span class="value">Spot Price</span>
        </div>
        <div class="sidebar-param">
            <span class="label">K</span>
            <span class="value">Strike Price</span>
        </div>
        <div class="sidebar-param">
            <span class="label">T</span>
            <span class="value">Time (Years)</span>
        </div>
        <div class="sidebar-param">
            <span class="label">r</span>
            <span class="value">Risk-Free Rate</span>
        </div>
        <div class="sidebar-param">
            <span class="label">σ</span>
            <span class="value">Volatility</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div class="sidebar-info">
        <p style="color: #3D5540; font-size: 0.6rem; line-height: 1.8; font-weight: 500;">
            <strong style="color: #1A2B1A;">Educational Purpose Only</strong><br>
            Not intended for real trading decisions.
        </p>
        <p style="color: #7A8F75; font-size: 0.55rem; margin-top: 0.5rem; font-weight: 500;">
            Black-Scholes-Merton • European Options
        </p>
        <hr style="border-top: 1px solid rgba(186, 200, 177, 0.3); margin: 0.8rem 0;">
        <p style="color: #7A8F75; font-size: 0.55rem; font-weight: 500; margin-bottom: 0.3rem;">
            <strong style="color: #1A2B1A; font-size: 0.65rem;">Developed by:</strong>
        </p>
        <p style="color: #1A2B1A; font-size: 0.7rem; font-weight: 700; margin-bottom: 0.5rem;">
            Erfan Mohammadi
        </p>
        <p style="font-size: 0.6rem; line-height: 1.6; margin-bottom: 0.3rem;">
            <a href="https://t.me/ERFANmmmig29" target="_blank" style="color: #4A7A5A; text-decoration: none;">Telegram: @ERFANmmmig29</a><br>
            <a href="https://github.com/erfan2mohammadi22" target="_blank" style="color: #4A7A5A; text-decoration: none;">GitHub: erfan2mohammadi22</a><br>
            <a href="https://www.linkedin.com/in/erfan2mohammadi22" target="_blank" style="color: #4A7A5A; text-decoration: none;">LinkedIn: erfan2mohammadi22</a><br>
            <a href="mailto:erfan2mohammadi@gmail.com" style="color: #4A7A5A; text-decoration: none;">Email: erfan2mohammadi@gmail.com</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# Main Header
# ============================================
st.markdown("""
<div class="main-header fade-in">
    <div style="display: flex; align-items: center; gap: 1.2rem; flex-wrap: wrap;">
        <div style="font-size: 3.5rem; font-weight: 300; color: #4A7A5A; font-family: 'Space Grotesk', sans-serif;">
            ∂
        </div>
        <div>
            <div class="main-title">Black-Scholes <span>Engine</span></div>
            <div class="main-subtitle">
                European Option Pricing &amp; Sensitivity Analysis
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================
# Inputs
# ============================================
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<p class="section-label">ASSET PARAMETERS</p>', unsafe_allow_html=True)
    S = st.number_input("Spot Price (S)", min_value=0.01, value=100.0, step=1.0,
                        help="Current price of the underlying asset")
    K = st.number_input("Strike Price (K)", min_value=0.01, value=105.0, step=1.0,
                        help="Price at which the option can be exercised")
    T = st.number_input("Time to Maturity (T) - Years", min_value=0.01, value=1.0, step=0.1,
                        help="Time remaining until expiration")

with col2:
    st.markdown('<p class="section-label">MARKET PARAMETERS</p>', unsafe_allow_html=True)
    r = st.number_input("Risk-Free Rate (r)", min_value=0.0, max_value=1.0, value=0.05, step=0.01,
                        help="Annual risk-free interest rate")
    sigma = st.slider("Volatility (σ)", min_value=0.01, max_value=1.0, value=0.20, step=0.01,
                      help="Annual volatility of the underlying asset")

st.markdown("---")

# ============================================
# Calculate Button
# ============================================
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    calculate = st.button("Calculate Option Price", type="primary", use_container_width=True, key="calc_btn")

# ============================================
# Main Logic & Calculation
# ============================================
if calculate:
    with st.spinner("Calculating..."):
        time.sleep(0.4)

    # Calculations
    call_price = black_scholes_call(S, K, T, r, sigma)
    put_price = black_scholes_put(S, K, T, r, sigma)

    # Greeks
    greeks_call = calculate_greeks(S, K, T, r, sigma, option_type='call')
    greeks_put = calculate_greeks(S, K, T, r, sigma, option_type='put')

    st.markdown("---")

    # ============================================
    # Pricing Results
    # ============================================
    st.markdown('<p class="section-label">PRICING RESULTS</p>', unsafe_allow_html=True)

    col_result1, col_result2, col_result3 = st.columns(3)

    with col_result1:
        st.metric(
            label="Call Option",
            value=f"${call_price:.2f}",
            delta=f"{call_price - max(S - K, 0):.2f}"
        )

    with col_result2:
        st.metric(
            label="Put Option",
            value=f"${put_price:.2f}",
            delta=f"{put_price - max(K - S, 0):.2f}"
        )

    with col_result3:
        st.metric(
            label="Intrinsic Value",
            value=f"${max(S - K, 0):.2f}",
            delta="Max profit if exercised"
        )

    st.markdown("---")

    # ============================================
    # Greeks Display
    # ============================================
    st.markdown('<p class="section-label">GREEKS</p>', unsafe_allow_html=True)

    col_g1, col_g2, col_g3, col_g4, col_g5 = st.columns(5)

    with col_g1:
        st.metric("Δ Delta", f"{greeks_call['delta']:.4f}", help="Sensitivity to underlying price")
    with col_g2:
        st.metric("Γ Gamma", f"{greeks_call['gamma']:.4f}", help="Rate of change of Delta")
    with col_g3:
        st.metric("ν Vega", f"{greeks_call['vega']:.4f}", help="Sensitivity to 1% volatility change")
    with col_g4:
        st.metric("Θ Theta", f"{greeks_call['theta']:.4f}", help="Time decay per day")
    with col_g5:
        st.metric("ρ Rho", f"{greeks_call['rho']:.4f}", help="Sensitivity to 1% interest rate change")

    with st.expander("View Put Greeks"):
        col_p1, col_p2, col_p3, col_p4, col_p5 = st.columns(5)
        with col_p1:
            st.metric("Δ Delta", f"{greeks_put['delta']:.4f}")
        with col_p2:
            st.metric("Γ Gamma", f"{greeks_put['gamma']:.4f}")
        with col_p3:
            st.metric("ν Vega", f"{greeks_put['vega']:.4f}")
        with col_p4:
            st.metric("Θ Theta", f"{greeks_put['theta']:.4f}")
        with col_p5:
            st.metric("ρ Rho", f"{greeks_put['rho']:.4f}")

    st.markdown("---")

    # ============================================
    # Sensitivity Analysis (Charts)
    # ============================================
    st.markdown('<p class="section-label">SENSITIVITY ANALYSIS</p>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Price vs S",
        "Heatmap",
        "Greeks",
        "3D Surface",
        "Put-Call Parity"
    ])

    with tab1:
        fig1 = viz.plot_price_sensitivity(S, K, T, r, sigma)
        st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False})

    with tab2:
        fig2 = viz.plot_sensitivity_heatmap(S, K, T, r, sigma)
        st.plotly_chart(fig2, use_container_width=True, config={'displayModeBar': False})

    with tab3:
        fig3 = viz.plot_greeks_sensitivity(S, K, T, r, sigma)
        st.plotly_chart(fig3, use_container_width=True, config={'displayModeBar': False})

    with tab4:
        fig4 = viz.plot_3d_surface(S, K, T, r, sigma)
        st.plotly_chart(fig4, use_container_width=True, config={'displayModeBar': False})

    with tab5:
        fig5 = viz.plot_put_call_parity(S, K, T, r, sigma)
        st.plotly_chart(fig5, use_container_width=True, config={'displayModeBar': False})

# ============================================
# Footer
# ============================================
st.markdown("""
<div class="app-footer fade-in">
    <div class="footer-divider"></div>
    <div class="footer-name">Erfan Mohammadi</div>
    <div class="footer-links">
        <a href="https://t.me/ERFANmmmig29" target="_blank">Telegram</a>
        <a href="https://github.com/erfan2mohammadi22" target="_blank">GitHub</a>
        <a href="https://www.linkedin.com/in/erfan2mohammadi22" target="_blank">LinkedIn</a>
        <a href="mailto:erfan2mohammadi@gmail.com">Email</a>
    </div>
    <div class="footer-copyright">
        © 2026 Black-Scholes Engine
    </div>
</div>
""", unsafe_allow_html=True)