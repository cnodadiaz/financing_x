import streamlit as st

# Function to perform the calculations
def calculate_valuation(raise_amount, alimit, interest, time_months, next_round_capital, equity_trade_next_round):
    gov_contribution = min(raise_amount, alimit)
    total_capital = raise_amount + gov_contribution
    convertible_note_value = raise_amount * (1 + (interest * (time_months / 12)))
    pre_money_valuation = next_round_capital / equity_trade_next_round
    post_money_valuation = pre_money_valuation + next_round_capital
    equity_ownership_investors = convertible_note_value / post_money_valuation

    return {
        'gov_contribution': gov_contribution,
        'total_capital': total_capital,
        'convertible_note_value': convertible_note_value,
        'pre_money_valuation': pre_money_valuation,
        'post_money_valuation': post_money_valuation,
        'equity_ownership_investors': equity_ownership_investors
    }

# Streamlit app layout
st.title('Startup Fundraising Financial Model (Featuring ALMIs Innovationstöd)')
st.write('A simple tool for startups to communicate effectively with investors about their financial planning and valuation.')

with st.expander("Description and Explanation"):
    st.markdown("""
    **Startup Fundraising Financial Model (Featuring ALMIs Innovationstöd)**

    The tool clarifies the company's valuation by focusing on capital needs rather than relying on speculative or arbitrary factors. 
    Startups can transparently demonstrate how their projected capital requirements align with their strategic growth plans and fundraising goals using this tool.

    **Purpose**
    
    The primary purpose of this notebook is as follows:

    - **Calculate Initial Capital**: Determine the total initial capital raised from investors and supplemented by government contributions.
    
    - **Accrue Interest on Convertible Notes**: Compute the future value of convertible notes, considering the interest accrued over a specified period until the next funding round.
    
    - **Determine Capital Needs for Next Round**: Project the capital requirements for the next fundraising round.
    
    - **Establish Pre-Money Valuation**: Calculate the company's valuation before raising new funds based on the projected capital needs and the percentage of equity to be traded.
    
    - **Determine Post-Money Valuation**: Calculate the company's valuation immediately after raising the new capital, providing a clear picture of the company's worth post-investment.
    
    - **Equity Distribution**: Explain the distribution of equity ownership, mainly focusing on the impact of converting notes on investors' equity.

    **Logic of the Process**

    - **Initial Capital and Government Contribution**: The notebook gathers input on the initial capital raised from investors and any additional government contributions, like innovation grants. This establishes the startup's base financial status.
    
    - **Interest on Convertible Notes**: We calculate the future value of convertible notes using the interest rate and the period until the next funding round. Thus, we transparently account for the impact of interest accrual.
    
    - **Next Round Capital Needs**: By inputting the projected capital needs for the next round, startups can base their valuation on actual financial requirements, shifting the focus from speculative valuation methods to a needs-based approach.
    
    - **Pre-Money Valuation Calculation**: The capital must be divided by the equity fraction to be traded away in the next round, resulting in the pre-money valuation, providing a realistic valuation grounded in the company's financial goals and investment strategy.
    
    - **Post-Money Valuation**: Adding the new capital raised in the next round to the pre-money valuation gives the post-money valuation. This figure reflects the company's worth immediately after securing new investments, providing a transparent and honest valuation to present to potential investors.
    
    - **Equity Ownership**: The tool also calculates investors' equity ownership after the convertible notes convert, clarifying the ownership dilution and ensuring the impact on existing and future investors is clear and justifiable.
    """)

st.sidebar.header('Input Parameters')
raise_amount = st.sidebar.number_input('Amount raised from investors, e.g. convertible note ($)', min_value=0.0, format='%f')
alimit = st.sidebar.number_input('Upper limit for the government innovation grant ($)', min_value=0.0, format='%f')
interest = st.sidebar.number_input('Bank loan (or note) interest rate (%)', min_value=0.0, format='%f') / 100
time_months = st.sidebar.number_input('Time until the next funding round (in months)', min_value=1, step=1)
next_round_capital = st.sidebar.number_input('Projected capital needs for the next round ($)', min_value=0.0, format='%f')
equity_trade_next_round = 0.20

if st.sidebar.button('Calculate'):
    results = calculate_valuation(raise_amount, alimit, interest, time_months, next_round_capital, equity_trade_next_round)

    st.subheader('Results')
    st.write(f"Initial capital raised from investors, e.g. convertible note: ${raise_amount:.2f}")
    st.write(f"Government's contribution (e.g., Tillväxtverket): ${results['gov_contribution']:.2f}")
    st.write(f"Total capital for the startup: ${results['total_capital']:.2f}")
    st.write(f"Pre-money valuation for the next round: ${results['pre_money_valuation']:.2f}")
    st.write(f"Post-money valuation after next round: ${results['post_money_valuation']:.2f}")
    st.write(f"Value of the convertible note after interest: ${results['convertible_note_value']:.2f}")
    st.write(f"Equity ownership for investors after conversion: {results['equity_ownership_investors'] * 100:.2f}%")
    st.write(f"Amount to be raised in the next funding round: ${next_round_capital:.2f}")

# To run the app, use the following command in the terminal: streamlit run app.py
