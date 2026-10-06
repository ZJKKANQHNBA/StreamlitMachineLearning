import streamlit as st

st.title('Simple Calculator')
st.write('เครื่องคิดเลขอย่างง่าย')

num1 = st.number_input('ป้อนตัวเลขแรก:', value=0.0)
num2 = st.number_input('ป้อนตัวเลขที่สอง:', value=0.0)
operation = st.selectbox('เลือกเครื่องหมาย:', ['+', '-', '*', '/'])

if st.button('คำนวณ'):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'ไม่สามารถหารด้วยศูนย์ได้'

    st.success(f'ผลลัพธ์: {result}')