import numpy as np
import pickle
import pandas as pd
import streamlit as st

pickle_in = open("rf.pk1","rb")
rf= pickle.load(pickle_in)

def predict_rent_price(Eng_Displ,Cyl,Gears,Max_Ethanol,Trans_Creeper_Gear,Trans_Desc,Exhaust_Valves_Per_Cyl,Intake_Valves_Per_Cyl,Carline_Class_Desc,Label_Recalc,Stop_Start_System,Eng_Displ_na,Max_Ethanol_Gasoline_na):
    prediction = rf.predict([[Eng_Displ,Cyl,Gears,Max_Ethanol,Trans_Creeper_Gear,Trans_Desc,Exhaust_Valves_Per_Cyl,Intake_Valves_Per_Cyl,Carline_Class_Desc,Label_Recalc,Stop_Start_System,Eng_Displ_na,Max_Ethanol_Gasoline_na]])
    print (prediction)
    return prediction
                            
                            
#user interface
def main():
    st.title("Conventional Fuel prediction")
    Eng_Displ = st.text_input("# of Eng_Displ","Type Here")
    Cyl = st.text_input("# of Cyl","Type Here")
    Gears = st.text_input("# of Gears","Type Here")
    Max_Ethanol = st.text_input("# of Max_Ethanol","Type Here")
    Trans_Creeper_Gear = st.text_input("# of Trans_Creeper_Gear","Type Here")
    Trans_Desc = st.text_input("# of Trans_Desc","Type Here")
    Exhaust_Valves_Per_Cyl = st.text_input("# of Exhaust_Valves_Per_Cyl","Type Here")
    Intake_Valves_Per_Cyl = st.text_input("# of Intake_Valves_Per_Cyl","Type Here")
    Carline_Class_Desc = st.text_input("# of Carline_Class_Desc","Type Here")
    Label_Recalc = st.text_input("# of Label_Recalc","Type Here")
    Stop_Start_System = st.text_input("# of Stop_Start_System,","Type Here")
    Eng_Displ_na = st.text_input("# of Eng_Displ_na,","Type Here")
    Max_Ethanol_Gasoline_na = st.text_input("# of Max_Ethanol_Gasoline_na,","Type Here")
    result=""
    if st.button("Predict"):
        result = predict_rent_price(Eng_Displ,Cyl,Gears,Max_Ethanol,Trans_Creeper_Gear,Trans_Desc,Exhaust_Valves_Per_Cyl,Intake_Valves_Per_Cyl,Carline_Class_Desc,Label_Recalc,Stop_Start_System,Eng_Displ_na,Max_Ethanol_Gasoline_na)
    st.success('The output is {}'.format(result))
                            
if __name__=='__main__':
    main()