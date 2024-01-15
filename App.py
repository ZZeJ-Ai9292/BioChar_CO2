import streamlit as st
import joblib
import numpy as np

model = joblib.load('model.pkl')

st.set_page_config(layout="wide")
st.markdown('<h1 style="text-align: center; font-family: \'Times New Roman\', Times, serif;">Prediction of CO<sub style="font-size: 70%;">2</sub> adsorption capacity of biochar</h1>', unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Biomass</p>', unsafe_allow_html=True)
    feature1 = st.slider('VM (%)', min_value=0.00, max_value=100.00, step=0.01, value=76.42)
    feature2 = st.slider('Ash (%)', min_value=0.00, max_value=100.00, step=0.01, value=3.98)
    feature3 = st.slider('FC (%)', min_value=0.00, max_value=100.00, step=0.01, value=19.61)
    feature4 = st.slider('C (%)', min_value=0.00, max_value=100.00, step=0.01, value=46.44)
    feature5 = st.slider('H (%)', min_value=0.00, max_value=100.00, step=0.01, value=6.36)
    feature6 = st.slider('N (%)', min_value=0.00, max_value=100.00, step=0.01, value=0.91)
    feature7 = st.slider('S (%)', min_value=0.00, max_value=100.00, step=0.01, value=0.38)
    feature8 = st.slider('O (%)', min_value=0.00, max_value=100.00, step=0.01, value=45.92)

with col2:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Pyrolysis</p>', unsafe_allow_html=True)
    feature26 = st.slider('Wash_Pre (HCl/H2O(−1/1))', min_value=-1, max_value=1, step=1, value=0)
    feature27 = st.slider('Wash_Post (HCl/H2O(−1/1))', min_value=-1, max_value=1, step=1, value=-1)
    feature28 = st.slider('HR (°C/min)', min_value=0, max_value=50, step=1, value=3)
    feature29 = st.slider('PT (°C)', min_value=0, max_value=1000, step=1, value=440)
    feature30 = st.slider('Pt (min)', min_value=0, max_value=240, step=1, value=50)

with col3:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Impregnation activation</p>', unsafe_allow_html=True)
    feature9 = st.slider('Chem_Act_Imp_S (biomass/biochar(−1/1))', min_value=-1, max_value=1, step=1, value=1)
    if feature9 == -1:
        feature10, feature11, feature12, feature13, feature14, feature15 = 0, 0, 0, 0, feature29, feature30
    elif feature9 == 0:
        feature10, feature11, feature12, feature13, feature14, feature15 = 0, 0, 0, 0, 0, 0
    else:
        feature10 = st.slider('Chem_Act_Imp_A (pKB)', min_value=-1.10, max_value=20.00, step=0.01, value=-0.56)
        feature11 = st.slider('Chem_Act_Imp_t (min)', min_value=0, max_value=1440, step=1, value=530)
        feature12 = st.slider('Chem_Act_Imp_T (°C)', min_value=0, max_value=80, step=1, value=24)
        feature13 = st.slider('Chem_Act_Imp_R', min_value=0.0, max_value=3.0, step=0.1, value=3.0)
        feature14 = st.slider('Chem_Act_Imp_AT (°C)', min_value=0, max_value=1000, step=10, value=840)
        feature15 = st.slider('Chem_Act_Imp_At (min)', min_value=0, max_value=120, step=1, value=110)

with col4:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Mixing activation</p>', unsafe_allow_html=True)
    feature16 = st.slider('Chem_Act_Mix_S (biomass/biochar(−1/1))', min_value=-1, max_value=1, step=1, value=0)
    if feature16 == -1:
        feature17, feature18, feature19, feature20 = 0, 0, feature29, feature30
    elif feature16 == 0:
        feature17, feature18, feature19, feature20 = 0, 0, 0, 0
    else:
        feature17 = st.slider('Chem_Act_Mix_A (pKB)', min_value=-1.10, max_value=11.30, step=0.01, value=0.00)
        feature18 = st.slider('Chem_Act_Mix_R', min_value=0.0, max_value=5.0, step=0.1, value=0.0)
        feature19 = st.slider('Chem_Act_Mix_AT (°C)', min_value=0, max_value=1000, step=10, value=0)
        feature20 = st.slider('Chem_Act_Mix_At (min)', min_value=0, max_value=180, step=1, value=0)

with col5:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Physical activation</p>', unsafe_allow_html=True)
    feature21 = st.slider('Ph_Act_Gas_S (biomass/biochar(−1/1))', min_value=-1, max_value=1, step=1, value=0)
    if feature21 == -1:
        feature22, feature23, feature24, feature25 = 0, 0, feature29, feature30
    elif feature21 == 0:
        feature22, feature23, feature24, feature25 = 0, 0, 0, 0
    else:
        feature22 = st.slider('Ph_Act_Gas_A (steam/CO2(−1/1))', min_value=-1, max_value=1, step=1, value=0)
        feature23 = st.slider('Ph_Act_Gas_F (mL/min)', min_value=0.0, max_value=100.0, step=0.1, value=0.0)
        feature24 = st.slider('Ph_Act_Gas_AT (°C)', min_value=0, max_value=900, step=10, value=0)
        feature25 = st.slider('Ph_Act_Gas_At (min)', min_value=0, max_value=180, step=1, value=0)

with col6:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Adsorption</p>', unsafe_allow_html=True)
    feature31 = st.slider('CO2_AT (°C)', min_value=0, max_value=75, step=25, value=0)
    feature32 = st.slider('CO2_Ap (bar)', min_value=0.1, max_value=1.0, step=0.1, value=1.0)

# 预测按钮
if st.button('Predict'):
    if feature9 == -1:
        feature10, feature11, feature12, feature13, feature14, feature15 = 0, 0, 0, 0, feature29, feature30
    elif feature9 == 0:
        feature10, feature11, feature12, feature13, feature14, feature15 = 0, 0, 0, 0, 0, 0
    if feature16 == -1:
        feature17, feature18, feature19, feature20 = 0, 0, feature29, feature30
    elif feature16 == 0:
        feature17, feature18, feature19, feature20 = 0, 0, 0, 0
    if feature21 == -1:
        feature22, feature23, feature24, feature25 = 0, 0, feature29, feature30
    elif feature21 == 0:
        feature22, feature23, feature24, feature25 = 0, 0, 0, 0
    input_data = np.array([[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8,
                            feature9, feature10, feature11, feature12, feature13, feature14, feature15,
                            feature16, feature17, feature18, feature19, feature20, feature21, feature22,
                            feature23, feature24, feature25, feature26, feature27, feature28, feature29,
                            feature30, feature31, feature32]])
    prediction = model.predict(input_data)
    formatted_prediction = "{:.2f}".format(prediction[0])
    st.write(f'<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">CO<sub>2</sub> Adsorption Capacity (mmol/g): {formatted_prediction}</p>', unsafe_allow_html=True)