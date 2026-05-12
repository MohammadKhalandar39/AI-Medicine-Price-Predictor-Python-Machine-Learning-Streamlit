import streamlit as st
import pickle
import pandas as pd

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(page_title="Medicine AI", page_icon="💊", layout="wide")

# ==============================
# CUSTOM CSS (🔥 PREMIUM LOOK)
# ==============================
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
h1 {
    text-align: center;
    background: -webkit-linear-gradient(#00C9FF, #92FE9D);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    background: linear-gradient(90deg, #00C9FF, #92FE9D);
    color: black;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# LOAD MODEL
# ==============================
model = pickle.load(open("best_model.pkl", "rb"))

# ==============================
# LOAD DATA FOR DROPDOWNS
# ==============================
df = pd.read_csv("D:\ML project\Extensive_A_Z_medicines_dataset_of_India.csv")

df.columns = df.columns.str.lower().str.strip()
df = df.drop_duplicates()

# Create composition column
df['composition'] = (
    df.get('short_composition1', '').astype(str) + " " +
    df.get('short_composition2', '').astype(str)
)

# Top manufacturers
top_manufacturers = df['manufacturer_name'].value_counts().head(20).index.tolist()

# Top compositions
top_compositions = df['composition'].dropna().unique()[:50]

# ==============================
# SIDEBAR
# ==============================
st.sidebar.title("💊 Medicine AI")
st.sidebar.markdown("### 🔍 Enter Details")

# Manufacturer dropdown
manufacturer = st.sidebar.selectbox(
    "🏭 Manufacturer",
    top_manufacturers
)

# Type dropdown
type_val = st.sidebar.selectbox(
    "💊 Type",
    ["Tablet", "Capsule", "Syrup"]
)

# Composition option
composition_option = st.sidebar.selectbox(
    "Choose Composition",
    ["Select from list", "Enter manually"]
)

if composition_option == "Select from list":
    composition = st.sidebar.selectbox("🧪 Composition", top_compositions)
else:
    composition = st.sidebar.text_input("🧪 Enter Composition")

# Predict button
predict_btn = st.sidebar.button("🚀 Predict", key="predict_btn")

# ==============================
# MAIN HEADER
# ==============================
st.markdown("<h1>💊 AI Medicine Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("### 🚀 Smart AI system for predicting medicine price category")
st.markdown("---")

# ==============================
# RESULT AREA
# ==============================
if predict_btn:

    input_data = pd.DataFrame({
        'manufacturer_name': [manufacturer],
        'type': [type_val],
        'composition': [composition]
    })

    prediction = model.predict(input_data)[0]

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown("## 💡 Prediction Result")

        if prediction == "Low":
            st.success("💰 LOW Price Range")
            st.info("Affordable and budget-friendly medicine ✅")

        elif prediction == "Medium":
            st.warning("⚠️ MEDIUM Price Range")
            st.info("Moderate pricing 💊")

        else:
            st.error("🔥 HIGH Price Range")
            st.info("Expensive medicine 💸")

# ==============================
# DASHBOARD CARDS
# ==============================
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Model Type", value="ML Pipeline")

with col2:
    st.metric(label="Features Used", value="3")

with col3:
    st.metric(label="Output", value="Price Category")

# ==============================
# FOOTER
# ==============================
st.markdown("---")
st.markdown("<p style='text-align:center;'>🚀 Built with Streamlit | AI Project</p>", unsafe_allow_html=True)