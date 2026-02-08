import random
import streamlit as st
st.title("Мой калькулятор")
num1 = st.number_input("Число А")
num2 = st.number_input("Число Б")
if st.button("Сложить"):
    st.write(f"Результат: {num1 + num2}")
st.divider() # Рисует горизонтальную черту
if st.button("🔮 Получить предсказание"):
    predictions = [
        "Сегодня твои расчеты будут идеальны!",
        "Ожидай приятный сюрприз в коде.",
        "Внимательно проверяй знаки плюс и минус.",
        "Твой калькулятор говорит: пора отдохнуть!",
        "Удача на твоей стороне, действуй!"
    ]
    st.info(random.choice(predictions))
