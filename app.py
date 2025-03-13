import streamlit as st  # type: ignore
import sympy as sp # type: ignore

st.title("Growth mindset Challenge")

st.sidebar.header("Input Parameters")

problem_type = st.sidebar.selectbox("Select Problem Type", ["Math Equation", "Algebraic Expression"])

if problem_type == "Math Equation":
    st.subheader("Solve a Math Equation")
    equation = st.text_input("Enter the equation (e.g., x**2 - 4 = 0):", "x**2 - 4 = 0")
    
    if st.button("Solve"):
        try:
            lhs, rhs = equation.split('=')
            lhs = sp.sympify(lhs)
            rhs = sp.sympify(rhs)
            solution = sp.solve(lhs - rhs)
            st.success(f"Solution: {solution}")
        except Exception as e:
            st.error(f"Error: {e}")

elif problem_type == "Algebraic Expression":
    st.subheader("Simplify an Algebraic Expression")
    expression = st.text_input("Enter the expression (e.g., x**2 + 2*x + 1):", "x**2 + 2*x + 1")
    
    if st.button("Simplify"):
        try:
            simplified_expr = sp.simplify(expression)
            st.success(f"Simplified Expression: {simplified_expr}")
        except Exception as e:
            st.error(f"Error: {e}")

st.sidebar.markdown("### About")
st.sidebar.markdown("This app helps you solve math equations and simplify algebraic expressions using SymPy.")