from haystack.components.fetchers.link_content import LinkContentFetcher
from haystack.components.converters import HTMLToDocument
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.generators import GPTGenerator
from haystack.components.builders.prompt_builder import PromptBuilder
from haystack import Pipeline
import os
import streamlit as st


@st.cache_data
@st.cache_resource
def generate_product_description_url(product_url):
    openai_api_key = os.environ["OPENAI_API_KEY"]
    fetcher = LinkContentFetcher()
    converter = HTMLToDocument()
    document_splitter = DocumentSplitter(split_by="word", split_length=50)
    generator = GPTGenerator(api_key=openai_api_key)

    prompt_template = """
    According to these documents:

    {% for doc in documents %}
    {{ doc.content }}
    {% endfor %}

    Answer the given question: {{question}}
    Answer:
    """
    prompt_builder = PromptBuilder(template=prompt_template)

    pipeline = Pipeline()
    pipeline.add_component("fetcher", fetcher)
    pipeline.add_component("converter", converter)
    pipeline.add_component("splitter", document_splitter)
    pipeline.add_component("prompt_builder", prompt_builder)
    pipeline.add_component("llm", generator)

    pipeline.connect("fetcher.streams", "converter.sources")
    pipeline.connect("converter.documents", "splitter.documents")
    pipeline.connect("splitter.documents", "prompt_builder.documents")
    pipeline.connect("prompt_builder.prompt", "llm.prompt")

    question = """
    Summarize the available information to generate a brief product description in no more than 5 sentences. 
    """

    print("start pipeline")
    result = pipeline.run(
        {"prompt_builder": {"question": question}, "fetcher": {"urls": [product_url]}}
    )
    product_description = result["llm"]["replies"][0]
    print("finish pipeline")
    print(product_description)
    return product_description


@st.cache_data
@st.cache_resource
def generate_product_description_spec(product_spec):
    openai_api_key = os.environ["OPENAI_API_KEY"]
    generator = GPTGenerator(api_key=openai_api_key)

    prompt_template = """
    You are given the technical specifications of a product:
    {{product_spec}}
    Please use only the available information above to generate a brief product description in no more than 5 sentences.
    """
    prompt_builder = PromptBuilder(template=prompt_template)

    pipeline = Pipeline()
    pipeline.add_component("prompt_builder", prompt_builder)
    pipeline.add_component("llm", generator)
    pipeline.connect("prompt_builder.prompt", "llm.prompt")

    print("start pipeline")
    result = pipeline.run({"prompt_builder": {"product_spec": product_spec}})
    product_description = result["llm"]["replies"][0]
    print("finish pipeline")
    print(product_description)
    return product_description


def run_test_url():
    product_url = (
        "https://www.brother.com.au/en/products/all-printers/printers/mfc-l9670cdn"
    )
    generate_product_description_url(product_url)


# test
# run_test_url()
