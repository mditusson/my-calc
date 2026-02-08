import streamlit as st
st.title("Мой калькулятор")
num1 = st.number_input("Число А")
num2 = st.number_input("Число Б")
if st.button("Сложить"):
    st.write(f"Результат: {num1 + num2}")
