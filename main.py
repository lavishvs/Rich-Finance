import streamlit as st
from prediction_helper import predict

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(page_title="Rich Finance: Credit Risk Modelling", page_icon="📊", layout="wide")

# ---------------------------
# Fixed Theme (Light Mode)
# ---------------------------
primary_bg = "#F9FAFB"
text_color = "#111827"
card_bg = "#FFFFFF"

st.markdown(
    f"""
    <style>
    body {{
        background-color: {primary_bg};
        color: {text_color};
    }}
    .result-card {{
        background-color: {card_bg};
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        margin-top: 15px;
    }}
    .footer {{
        text-align: center;
        font-size: 14px;
        margin-top: 40px;
        color: #6B7280;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# Title
# ---------------------------
st.markdown("<h1 style='color:#1E3A8A;'>📊 Rich Finance: Credit Risk Modelling</h1>", unsafe_allow_html=True)

# ---------------------------
# Input Section
# ---------------------------
st.subheader("🔧 Input Parameters")
st.write("Provide your details below to calculate credit risk:")

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
with row1[1]:
    income = st.number_input('Income (₹)', min_value=10000, value=1200000)
with row1[2]:
    loan_amount = st.number_input('Loan Amount (₹)', min_value=0, value=2560000)

# ✅ Automatically Calculate Loan-to-Income Ratio (Read-Only Display)
loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[0]:
    st.metric("Loan-to-Income Ratio", f"{loan_to_income_ratio:.2f}")

with row2[1]:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=1, step=1, value=36)
with row2[2]:
    avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=20)

with row3[0]:
    delinquency_ratio = st.number_input('Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30)
with row3[1]:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio (%)', min_value=0, max_value=100, step=1, value=30)
with row3[2]:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=10, step=1, value=2)

with row4[0]:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
with row4[1]:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with row4[2]:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

# ---------------------------
# Calculate Button & Results
# ---------------------------
st.markdown("---")
if st.button('💡 Calculate Risk', use_container_width=True):
    with st.spinner("Calculating risk..."):
        probability, credit_score, rating = predict(
            age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
            delinquency_ratio, credit_utilization_ratio, num_open_accounts,
            residence_type, loan_purpose, loan_type
        )

    # Result Card
    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
    st.subheader("📊 Results")
    st.write(f"**Default Probability:** {probability:.2%}")
    st.progress(min(probability, 1.0))
    st.write(f"**Credit Score:** {credit_score}")

    color = "#16A34A" if rating == "A" else "#FACC15" if rating == "B" else "#DC2626"
    st.markdown(f"<p style='font-weight:700;color:{color};'>Rating: {rating}</p>", unsafe_allow_html=True)

    # Explainability
    st.markdown("### 🧠 Why This Result?")
    st.write(f"- **Loan-to-Income Ratio:** {loan_to_income_ratio:.2f} → Higher ratios usually increase risk.")
    st.write(f"- **Delinquency Ratio:** {delinquency_ratio}% → Past payment issues detected.")
    st.write(f"- **Credit Utilization:** {credit_utilization_ratio}% → Higher usage = more risk.")
    st.write(f"- **Avg DPD:** {avg_dpd_per_delinquency} → Indicates how late payments have been.")
    st.write(f"- **Open Accounts:** {num_open_accounts} → More obligations = more financial pressure.")

    st.success("✅ A lower probability and higher score indicate better credit health.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# Footer
# ---------------------------
st.markdown("<div class='footer'>Made with ❤️ by Rich Finance</div>", unsafe_allow_html=True)
