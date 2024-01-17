import streamlit as st
import joblib
import numpy as np

model = joblib.load('model.pkl')

st.set_page_config(layout="wide")
st.markdown('<h1 style="text-align: center; font-family: \'Times New Roman\', Times, serif;">Prediction of CO<sub style="font-size: 70%;">2</sub> adsorption capacity of biochar</h1>', unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.markdown('<p style="font-size: 24px; color: red; font-family: \'Times New Roman\', Times, serif; ">Biomass</p>', unsafe_allow_html=True)
    
    def styled_slider(label, min_value, max_value, step, value, format="%.2f", color="black", label_margin_right="10px", slider_margin_top="10px"):
        st.markdown(f'<span style="color: {color}; font-weight: bold; margin-right: {label_margin_right};">{label}</span>', unsafe_allow_html=True)
        st.markdown(f'<div style="margin-top: {slider_margin_top};">{st.slider("", min_value=min_value, max_value=max_value, step=step, value=value, format=format, key=label)}</div>', unsafe_allow_html=True)

    feature1 = styled_slider('VM (%)', min_value=0.00, max_value=100.00, step=0.01, value=76.42, color="orange", label_margin_right="20px", slider_margin_top="20px")
    feature2 = styled_slider('Ash (%)', min_value=0.00, max_value=100.00, step=0.01, value=3.98, color="orange", label_margin_right="20px", slider_margin_top="20px")
    feature3 = styled_slider('FC (%)', min_value=0.00, max_value=100.00, step=0.01, value=19.61, color="orange", label_margin_right="20px", slider_margin_top="20px")
    feature4 = styled_slider('C (%)', min_value=0.00, max_value=100.00, step=0.01, value=46.44, color="orange", label_margin_right="20px", slider_margin_top="20px")
    feature5 = styled_slider('H (%)', min_value=0.00, max_value=100.00, step=0.01, value=6.36, color="orange", label_margin_right="20px", slider_margin_top="20px")
    feature6 = styled_slider('N (%)', min_value=0.00, max_value=100.00, step=0.01, value=0.91, color="orange", label_margin_right="20px", slider_margin_top="20px")
    feature7 = styled_slider('S (%)', min_value=0.00, max_value=100.00, step=0.01, value=0.38, color="orange", label_margin_right="20px", slider_margin_top="20px")
    feature8 = styled_slider('O (%)', min_value=0.00, max_value=100.00, step=0.01, value=45.92, color="orange", label_margin_right="20px", slider_margin_top="20px")

with col2:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Pyrolysis</p>', unsafe_allow_html=True)
    feature26 = st.slider('Wash-Pre (HCl/none/H2O — −1/0/1)', min_value=-1, max_value=1, step=1, value=0)
    feature27 = st.slider('Wash-Post (HCl/none/H2O — −1/0/1)', min_value=-1, max_value=1, step=1, value=-1)
    feature28 = st.slider('HR (°C/min)', min_value=0, max_value=50, step=1, value=3)
    feature29 = st.slider('PT (°C)', min_value=0, max_value=1000, step=1, value=440)
    feature30 = st.slider('Pt (min)', min_value=0, max_value=240, step=1, value=50)

with col3:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Impregnation activation</p>', unsafe_allow_html=True)
    feature9 = st.slider('Imp-Seq (biomass/none/biochar — -1/0/1)', min_value=-1, max_value=1, step=1, value=1)
    if feature9 == 0:
        feature10, feature11, feature12, feature13, feature14, feature15 = 0, 0, 0, 0, 0, 0
        st.write(f'Without impregnation activation')
    elif feature9 == -1:
        feature10 = st.slider('Imp-Agent (pKB)', min_value=-1.10, max_value=20.00, step=0.01, value=-0.56)
        feature11 = st.slider('Imp-t (min)', min_value=0, max_value=1440, step=1, value=530)
        feature12 = st.slider('Imp-T (°C)', min_value=0, max_value=80, step=1, value=24)
        feature13 = st.slider('Imp-Ratio', min_value=0.0, max_value=3.0, step=0.1, value=3.0)
        feature14 = feature29
        feature15 = feature30
        st.write(f'Imp-AT (°C): {feature14}')
        st.write(f'Imp-At (min): {feature15}')
    else:
        feature10 = st.slider('Imp-Agent (pKB)', min_value=-1.10, max_value=20.00, step=0.01, value=-0.56)
        feature11 = st.slider('Imp-t (min)', min_value=0, max_value=1440, step=1, value=530)
        feature12 = st.slider('Imp-T (°C)', min_value=0, max_value=80, step=1, value=24)
        feature13 = st.slider('Imp-Ratio', min_value=0.0, max_value=3.0, step=0.1, value=3.0)
        feature14 = st.slider('Imp-AT (°C)', min_value=0, max_value=1000, step=10, value=840)
        feature15 = st.slider('Imp-At (min)', min_value=0, max_value=120, step=1, value=110)

with col4:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Mixing activation</p>', unsafe_allow_html=True)
    feature16 = st.slider('Mix-Seq (biomass/none/biochar — -1/0/1)', min_value=-1, max_value=1, step=1, value=0)
    if feature16 == 0:
        feature17, feature18, feature19, feature20 = 0, 0, 0, 0
        st.write(f'Without mixing activation')
    elif feature16 == -1:
        feature17 = st.slider('Mix-Agent (pKB)', min_value=-1.10, max_value=11.30, step=0.01, value=0.00)
        feature18 = st.slider('Mix-Ratio', min_value=0.0, max_value=5.0, step=0.1, value=0.0)
        feature19 = feature29
        feature20 = feature30
        st.write(f'Mix-AT (°C): {feature19}')
        st.write(f'Mix-At (min): {feature20}')
    else:
        feature17 = st.slider('Mix-Agent (pKB)', min_value=-1.10, max_value=11.30, step=0.01, value=0.00)
        feature18 = st.slider('Mix-Ratio', min_value=0.0, max_value=5.0, step=0.1, value=0.0)
        feature19 = st.slider('Mix-AT (°C)', min_value=0, max_value=1000, step=10, value=0)
        feature20 = st.slider('Mix-At (min)', min_value=0, max_value=180, step=1, value=0)

with col5:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Physical activation</p>', unsafe_allow_html=True)
    feature21 = st.slider('Gas-Seq (biomass/none/biochar — -1/0/1)', min_value=-1, max_value=1, step=1, value=0)
    if feature21 == 0:
        feature22, feature23, feature24, feature25 = 0, 0, 0, 0
        st.write(f'Without physical activation')
    elif feature21 == -1:
        feature22 = st.slider('Gas-Agent (steam/CO2/None(−1/1/0))', min_value=-1, max_value=1, step=1, value=0)
        feature23 = st.slider('Gas-Flow (mL/min)', min_value=0.0, max_value=100.0, step=0.1, value=0.0)
        feature24 = feature29
        feature25 = feature30
        st.write(f'Gas-AT (°C): {feature24}') 
        st.write(f'Gas-At (min): {feature25}')
    else:
        feature22 = st.slider('Gas-Agent (steam/none/CO2 — -1/0/1)', min_value=-1, max_value=1, step=1, value=0)
        feature23 = st.slider('Gas-Flow (mL/min)', min_value=0.0, max_value=100.0, step=0.1, value=0.0)
        feature24 = st.slider('Gas-AT (°C)', min_value=0, max_value=900, step=10, value=0)
        feature25 = st.slider('Gas-At (min)', min_value=0, max_value=180, step=1, value=0)

with col6:
    st.markdown('<p style="font-size: 24px; color: red; font-weight: bold; font-family: \'Times New Roman\', Times, serif; ">Adsorption</p>', unsafe_allow_html=True)
    feature31 = st.slider('CO2Ad-T (°C)', min_value=0, max_value=75, step=25, value=0)
    feature32 = st.slider('CO2Ad-P (bar)', min_value=0.1, max_value=1.0, step=0.1, value=1.0)

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