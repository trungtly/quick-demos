# Generate product description with LLM
This demo showcases how to generate a product description from a product URL using a Large Language Model. The demo uses the `haystack` library for the LLM pipeline and `streamlit` for the UI.

Reference: https://haystack.deepset.ai/advent-of-haystack/day-2#challenge

## Instructions
To use this demo, follow these steps:

- Create the virtual env and install the required libraries: `haystack` and `streamlit`.
```bash
cd quick-demos/product_description
python3.11 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
- set the your `OPENAI_API_KEY` from the terminal
```bash
export OPENAI_API_KEY=...
```
- Run the `app.py` file using the command `env/bin/streamlit run src/app.py`.
- Enter the product URL and click on the `Generate Description` button.
The product description will be generated and displayed on the screen.
