from numpy import select
import streamlit as st
st.title('Hello Streamlit')
st.text('Hello Streamlit')
st.write('Hello Streamlit')


a = st.text_input('a', 'aa')
st.write(a)
select = st.selectbox("どちらが欲しい", ["大きい箱", "小さい箱"])
if st.button('開封'):
    if select == '大きい箱':
        st.write('空っぽでした')
    else:
        st.write('お宝が出てきました')
