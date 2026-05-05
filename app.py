import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.preprocessing import LabelEncoder

# ── Generate Dataset ──────────────────────────────────────────
@st.cache_data
def generate_data():
    np.random.seed(42)
    n = 1000

    cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai',
              'Pune', 'Kolkata', 'Jaipur', 'Ahmedabad', 'Lucknow']
    city_multiplier = {
        'Mumbai': 2.5, 'Delhi': 2.0, 'Bangalore': 1.8,
        'Hyderabad': 1.5, 'Chennai': 1.4, 'Pune': 1.3,
        'Kolkata': 1.2, 'Jaipur': 1.0, 'Ahmedabad': 1.0, 'Lucknow': 0.9
    }
    furnishing = ['Unfurnished', 'Semi-Furnished', 'Fully Furnished']
    furnish_multiplier = {'Unfurnished': 1.0, 'Semi-Furnished': 1.15, 'Fully Furnished': 1.3}

    data = []
    for _ in range(n):
        city = np.random.choice(cities)
        area = np.random.randint(400, 5000)
        bedrooms = np.random.randint(1, 6)
        bathrooms = np.random.randint(1, 4)
        floors = np.random.randint(1, 30)
        age = np.random.randint(0, 30)
        parking = np.random.randint(0, 3)
        furnish = np.random.choice(furnishing)

        base_price = (
            area * 4500 * city_multiplier[city] +
            bedrooms * 200000 +
            bathrooms * 150000 +
            parking * 100000 -
            age * 50000 +
            floors * 20000
        ) * furnish_multiplier[furnish]

        noise = np.random.normal(0, base_price * 0.05)
        price = max(500000, base_price + noise)

        data.append({
            'City': city,
            'Area_sqft': area,
            'Bedrooms': bedrooms,
            'Bathrooms': bathrooms,
            'Floor': floors,
            'Age_years': age,
            'Parking': parking,
            'Furnishing': furnish,
            'Price': round(price, -3)
        })

    return pd.DataFrame(data)

# ── Train Model ───────────────────────────────────────────────
@st.cache_data
def train_model():
    df = generate_data()
    le_city = LabelEncoder()
    le_furnish = LabelEncoder()
    df['City_encoded'] = le_city.fit_transform(df['City'])
    df['Furnish_encoded'] = le_furnish.fit_transform(df['Furnishing'])

    features = ['Area_sqft', 'Bedrooms', 'Bathrooms', 'Floor',
                'Age_years', 'Parking', 'City_encoded', 'Furnish_encoded']
    X = df[features]
    y = df['Price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    return model, le_city, le_furnish, r2, mae, df, features

# ── App ───────────────────────────────────────────────────────
st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="wide")
st.title("🏠 House Price Predictor")
st.caption("Day 6 of 30-Day AI/ML Challenge by Udit Narayan Mohanty")
st.divider()

model, le_city, le_furnish, r2, mae, df, features = train_model()

# Model Stats
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🎯 Model Accuracy (R²)", f"{round(r2*100, 2)}%")
with col2:
    st.metric("📊 Mean Error", f"₹{mae:,.0f}")
with col3:
    st.metric("🏘️ Algorithm", "Random Forest")

st.divider()

# ── Input Form ────────────────────────────────────────────────
st.subheader("🏡 Enter House Details")

col1, col2, col3 = st.columns(3)

with col1:
    city = st.selectbox("🌆 City", ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad',
                                     'Chennai', 'Pune', 'Kolkata', 'Jaipur',
                                     'Ahmedabad', 'Lucknow'])
    area = st.slider("📐 Area (sq ft)", 400, 5000, 1200, 50)
    bedrooms = st.selectbox("🛏️ Bedrooms", [1, 2, 3, 4, 5])

with col2:
    bathrooms = st.selectbox("🚿 Bathrooms", [1, 2, 3])
    floor = st.slider("🏢 Floor Number", 1, 30, 5)
    parking = st.selectbox("🚗 Parking Spots", [0, 1, 2])

with col3:
    age = st.slider("🏗️ Property Age (years)", 0, 30, 5)
    furnishing = st.selectbox("🛋️ Furnishing", ['Unfurnished', 'Semi-Furnished', 'Fully Furnished'])

if st.button("🔍 Predict Price", use_container_width=True):
    city_encoded = le_city.transform([city])[0]
    furnish_encoded = le_furnish.transform([furnishing])[0]

    input_data = pd.DataFrame([[area, bedrooms, bathrooms, floor,
                                 age, parking, city_encoded, furnish_encoded]],
                               columns=features)

    predicted_price = model.predict(input_data)[0]
    low = predicted_price * 0.9
    high = predicted_price * 1.1

    st.divider()
    st.subheader("💰 Prediction Result")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🏷️ Minimum Price", f"₹{low:,.0f}")
    with col2:
        st.success(f"### 🎯 Predicted Price\n# ₹{predicted_price:,.0f}")
    with col3:
        st.metric("🏷️ Maximum Price", f"₹{high:,.0f}")

    price_per_sqft = predicted_price / area
    st.info(f"📐 Price per sq ft: **₹{price_per_sqft:,.0f}**")

    # Feature Importance Chart
    st.divider()
    st.subheader("📊 What Affects the Price Most?")
    importance_df = pd.DataFrame({
        'Feature': ['Area', 'Bedrooms', 'Bathrooms', 'Floor', 'Age', 'Parking', 'City', 'Furnishing'],
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=True)

    fig = px.bar(importance_df, x='Importance', y='Feature',
                 orientation='h', color='Importance',
                 color_continuous_scale='Viridis',
                 template='plotly_dark')
    fig.update_layout(height=350, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

    # Price comparison chart
    st.subheader(f"🌆 Price Comparison — {city} vs Other Cities")
    city_prices = df.groupby('City')['Price'].mean().reset_index()
    city_prices = city_prices.sort_values('Price', ascending=False)
    city_prices['Color'] = city_prices['City'].apply(lambda x: '🎯 Your City' if x == city else 'Other Cities')

    fig2 = px.bar(city_prices, x='City', y='Price',
                  color='Color',
                  color_discrete_map={'🎯 Your City': '#FF4B4B', 'Other Cities': '#4B8BFF'},
                  template='plotly_dark')
    fig2.update_layout(height=350)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()
st.caption("Built with Python + Streamlit + Random Forest | Udit Narayan Mohanty")