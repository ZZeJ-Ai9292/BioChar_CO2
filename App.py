import streamlit as st
import joblib
import numpy as np

model = joblib.load('model.pkl')

st.set_page_config(layout="wide")
st.markdown('<h1 style="text-align: center; font-family: \'Times New Roman\', Times, serif;">Prediction of CO<sub style="font-size: 70%;">2</sub> adsorption capacity of biochar</h1>', unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Biomass</p>', unsafe_allow_html=True)
    feature1 = st.slider('<b>VM (%)</b>', min_value=0.00, max_value=100.00, step=0.01, value=76.42, unsafe_allow_html=True)
    feature2 = st.slider('<b>Ash (%)</b>', min_value=0.00, max_value=100.00, step=0.01, value=3.98, unsafe_allow_html=True)
    feature3 = st.slider('<b>FC (%)</b>', min_value=0.00, max_value=100.00, step=0.01, value=19.61, unsafe_allow_html=True)
    feature4 = st.slider('<b>C (%)</b>', min_value=0.00, max_value=100.00, step=0.01, value=46.44, unsafe_allow_html=True)
    feature5 = st.slider('<b>H (%)</b>', min_value=0.00, max_value=100.00, step=0.01, value=6.36, unsafe_allow_html=True)
    feature6 = st.slider('<b>N (%)</b>', min_value=0.00, max_value=100.00, step=0.01, value=0.91, unsafe_allow_html=True)
    feature7 = st.slider('<b>S (%)</b>', min_value=0.00, max_value=100.00, step=0.01, value=0.38, unsafe_allow_html=True)
    feature8 = st.slider('<b>O (%)</b>', min_value=0.00, max_value=100.00, step=0.01, value=45.92, unsafe_allow_html=True)

with col2:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Pyrolysis</p>', unsafe_allow_html=True)
    feature26 = st.slider('<b>Wash-Pre (HCl/none/H<sub>2</sub>O — −1/0/1)</b>', min_value=-1, max_value=1, step=1, value=0, unsafe_allow_html=True)
    feature27 = st.slider('<b>Wash-Post (HCl/none/H<sub>2</sub>O — −1/0/1)</b>', min_value=-1, max_value=1, step=1, value=-1, unsafe_allow_html=True)
    feature28 = st.slider('<b>HR (°C/min)</b>', min_value=0, max_value=50, step=1, value=3, unsafe_allow_html=True)
    feature29 = st.slider('<b>PT (°C)</b>', min_value=0, max_value=1000, step=1, value=440, unsafe_allow_html=True)
    feature30 = st.slider('<b>Pt (min)</b>', min_value=0, max_value=240, step=1, value=50, unsafe_allow_html=True)

with col3:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Impregnation activation</p>', unsafe_allow_html=True)
    feature9 = st.slider('<b>Imp-Seq (biomass/none/biochar — -1/0/1)</b>', min_value=-1, max_value=1, step=1, value=1, unsafe_allow_html=True)
    if feature9 == 0:
        feature10, feature11, feature12, feature13, feature14, feature15 = 0, 0, 0, 0, 0, 0
        st.write(f'Without impregnation activation')
    elif feature9 == -1:
        feature10 = st.slider('<b>Imp-Agent (pK<sub>B</sub>)</b>', min_value=-1.10, max_value=20.00, step=0.01, value=-0.56, unsafe_allow_html=True)
        feature11 = st.slider('<b>Imp-t (min)</b>', min_value=0, max_value=1440, step=1, value=530, unsafe_allow_html=True)
        feature12 = st.slider('<b>Imp-T (°C)</b>', min_value=0, max_value=80, step=1, value=24, unsafe_allow_html=True)
        feature13 = st.slider('<b>Imp-Ratio</b>', min_value=0.0, max_value=3.0, step=0.1, value=3.0, unsafe_allow_html=True)
        feature14 = feature29
        feature15 = feature30
        st.write(f'<b>Imp-AT (°C): {feature14}')
        st.write(f'<b>Imp-At (min): {feature15}')
    else:
        feature10 = st.slider('<b>Imp-Agent (pK<sub>B</sub>)</b>', min_value=-1.10, max_value=20.00, step=0.01, value=-0.56, unsafe_allow_html=True)
        feature11 = st.slider('<b>Imp-t (min)</b>', min_value=0, max_value=1440, step=1, value=530, unsafe_allow_html=True)
        feature12 = st.slider('<b>Imp-T (°C)</b>', min_value=0, max_value=80, step=1, value=24, unsafe_allow_html=True)
        feature13 = st.slider('<b>Imp-Ratio</b>', min_value=0.0, max_value=3.0, step=0.1, value=3.0, unsafe_allow_html=True)
        feature14 = st.slider('<b>Imp-AT (°C)</b>', min_value=0, max_value=1000, step=10, value=840, unsafe_allow_html=True)
        feature15 = st.slider('<b>Imp-At (min)</b>', min_value=0, max_value=120, step=1, value=110, unsafe_allow_html=True)

with col4:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Mixing activation</p>', unsafe_allow_html=True)
    feature16 = st.slider('<b>Mix-Seq (biomass/none/biochar — -1/0/1)</b>', min_value=-1, max_value=1, step=1, value=0, unsafe_allow_html=True)
    if feature16 == 0:
        feature17, feature18, feature19, feature20 = 0, 0, 0, 0
        st.write(f'Without mixing activation')
    elif feature16 == -1:
        feature17 = st.slider('<b>Mix-Agent (pK<sub>B</sub>)</b>', min_value=-1.10, max_value=11.30, step=0.01, value=0.00, unsafe_allow_html=True)
        feature18 = st.slider('<b>Mix-Ratio</b>', min_value=0.0, max_value=5.0, step=0.1, value=0.0, unsafe_allow_html=True)
        feature19 = feature29
        feature20 = feature30
        st.write(f'Mix-AT (°C): {feature19}')
        st.write(f'Mix-At (min): {feature20}')
    else:
        feature17 = st.slider('<b>Mix-Agent (pK<sub>B</sub>)</b>', min_value=-1.10, max_value=11.30, step=0.01, value=0.00, unsafe_allow_html=True)
        feature18 = st.slider('<b>Mix-Ratio</b>', min_value=0.0, max_value=5.0, step=0.1, value=0.0, unsafe_allow_html=True)
        feature19 = st.slider('<b>Mix-AT (°C)</b>', min_value=0, max_value=1000, step=10, value=0, unsafe_allow_html=True)
        feature20 = st.slider('<b>Mix-At (min)</b>', min_value=0, max_value=180, step=1, value=0, unsafe_allow_html=True)

with col5:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Physical activation</p>', unsafe_allow_html=True)
    feature21 = st.slider('Gas-Seq (biomass/none/biochar — -1/0/1)', min_value=-1, max_value=1, step=1, value=0, unsafe_allow_html=True)
    if feature21 == 0:
        feature22, feature23, feature24, feature25 = 0, 0, 0, 0
        st.write(f'Without physical activation')
    elif feature21 == -1:
        feature22 = st.slider('<b>Gas-Agent (steam/CO<sub>2</sub>/None(−1/1/0))</b>', min_value=-1, max_value=1, step=1, value=0, unsafe_allow_html=True)
        feature23 = st.slider('<b>Gas-Flow (mL/min)</b>', min_value=0.0, max_value=100.0, step=0.1, value=0.0, unsafe_allow_html=True)
        feature24 = feature29
        feature25 = feature30
        st.write(f'Gas-AT (°C): {feature24}') 
        st.write(f'Gas-At (min): {feature25}')
    else:
        feature22 = st.slider('<b>Ph_Act_Gas_A (steam/none/CO<sub>2</sub> — -1/0/1</b>', min_value=-1, max_value=1, step=1, value=0, unsafe_allow_html=True)
        feature23 = st.slider('<b>Gas-Flow (mL/min)</b>', min_value=0.0, max_value=100.0, step=0.1, value=0.0, unsafe_allow_html=True)
        feature24 = st.slider('<b>Gas-AT (°C)</b>', min_value=0, max_value=900, step=10, value=0, unsafe_allow_html=True)
        feature25 = st.slider('<b>Gas-At (min)</b>', min_value=0, max_value=180, step=1, value=0, unsafe_allow_html=True)

with col6:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Adsorption</p>', unsafe_allow_html=True)
    feature31 = st.slider('<b>CO2Ad-T (°C)', min_value=0, max_value=75, step=25, value=0, unsafe_allow_html=True)
    feature32 = st.slider('<b>CO2Ad-P (bar)', min_value=0.1, max_value=1.0, step=0.1, value=1.0, unsafe_allow_html=True)

# 预测按钮
if st.button('Predict'):
    input_data = np.array([[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8,
                            feature9, feature10, feature11, feature12, feature13, feature14, feature15,
                            feature16, feature17, feature18, feature19, feature20, feature21, feature22,
                            feature23, feature24, feature25, feature26, feature27, feature28, feature29,
                            feature30, feature31, feature32]])
    prediction = model.predict(input_data)
    formatted_prediction = "{:.2f}".format(prediction[0])
    st.write(f'<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">CO<sub>2</sub> Adsorption Capacity (mmol/g): {formatted_prediction}</p>', unsafe_allow_html=True)