import streamlit as st

st.title("Rent Calculator for Hostel Boys")

# Input fields 
rent = st.number_input("Enter Your hostel/flat rent:", min_value=0.0)
food = st.number_input("Enter the amount of food ordered:", min_value=0.0)
electricity_spend = st.number_input("Enter the total number of units of electricity spent:", min_value=0.0)
charge_per_unit = st.number_input("Enter the charge per unit:", min_value=0.0)
number_of_persons = st.number_input("Number of persons:", min_value=1)

# Function to calculate rent per person
def rent_calc(rent, food, electricity_bill, number_of_persons):
    return (rent + food + electricity_bill) / number_of_persons

# Button to trigger calculation
if st.button("Calculate"):
    electricity_bill = electricity_spend * charge_per_unit
    charge_fee_person = rent_calc(rent, food, electricity_bill, number_of_persons)
    
    st.subheader("Total Charges Per Person:")
    st.success(f"Each person should pay: Rs-/{charge_fee_person:.2f}")
