import streamlit as st

def data_cal():
    price_amount = st.session_state['amount']
    trans_amount = st.session_state['times']
    total_fee = (price_amount * 2.6) * .01
    total_amount = total_fee * trans_amount + .10
    take_home = price_amount * trans_amount - total_amount
    return f'Square Keeps: {round(total_amount,2)}, You Take ${take_home}'

st.text('Square Calculator ')
st.number_input('Enter Amount', key='amount')
st.number_input('How many Transaction ', step=1, key='times')
show = data_cal()
results = st.write(show)
st.button('Calculate', results)


