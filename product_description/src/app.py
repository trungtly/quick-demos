import streamlit as st
from backend import generate_product_description

st.title('SAI Demo: Product Description with Generative AI')

product_url = st.text_input('Enter the product URL', 'https://www.sai-digital.com/catalyzer/smartprice')
# https://www.brother.com.au/en/products/all-printers/printers/dcp-l3560cdw
# https://www.brother.com.au/en/products/all-printers/printers/mfc-l9670cdn
# https://www.brother.com.au/en/products/all-printers/printers/hl-l9470cdn

if st.button("Generate Description"):
    product_description = generate_product_description(product_url)
    st.write(product_description)