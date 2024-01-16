import streamlit as st
from backend import generate_product_description_url, generate_product_description_spec

st.title("SAI Demo: Product Description with Generative AI")


# https://www.brother.com.au/en/products/all-printers/printers/dcp-l3560cdw
# https://www.brother.com.au/en/products/all-printers/printers/mfc-l9670cdn
test_product_url = (
    "https://www.brother.com.au/en/products/all-printers/printers/hl-l9470cdn"
)
product_url = st.text_input("Enter the Product URL", value=test_product_url)

if st.button("Generate Description from url"):
    product_description = generate_product_description_url(product_url)
    st.write(product_description)


# copy the specs from here:
# https://koreab2b.sai-digital.com/koreab2bstorefront/koreab2b/en/USD/Products/Polymers-%26-Resins/Commodity-Polymers-%26-Raw-Materials/Poly%28tetramethylene-ether%29glycol/p/p159511

test_product_spec = """
Common Names 	        Tetrahydrofuran
Odor 	                Odorless
Molecular Weight 	    225
Flash Point 	        181°C
Freezing Point 	        -20°C
Specific heat(kJ/kg･K) 	2
Viscosity(mPa･s) 	    320°C
Appearance 	Colorless transparent liquid when melted
"""
product_spec = st.text_area(
    "Enter the Product Specifications", value=test_product_spec, height=200
)

if st.button("Generate Description from sepc"):
    product_description = generate_product_description_spec(product_spec)
    st.write(product_description)
