import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    else:
        return a / b

st.title("Simple Calculator")

# Change the hover effect of the operator selectbox
st.markdown(
    """
    <style>
    .stSelectbox>div:hover {
        border-color: #63ace5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

operation = st.selectbox("Select operation", ("Addition", "Subtraction", "Multiplication", "Division"))

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

# Add a Calculate button
if st.button("Calculate"):
    result = None

    if operation == "Addition":
        result = add(num1, num2)
    elif operation == "Subtraction":
        result = subtract(num1, num2)
    elif operation == "Multiplication":
        result = multiply(num1, num2)
    elif operation == "Division":
        result = divide(num1, num2)

    if result is not None:
        st.write(f"Result of {operation.lower()} is: {result}")
