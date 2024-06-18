from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
import textwrap
import os
from dotenv import load_dotenv


load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("MY_OPENAI_API_KEY")

llm = ChatOpenAI(model_name="gpt-3.5-turbo")

test_string = """
My fellow Americans, this is the 34th time I'll speak to you from the Oval Office, and the last. We've been together eight years now, and soon it'll be time for me to go. But before I do, I wanted to share some thoughts, some of which I have been saving for a long time.
It's been the honor of my life to be your President. So many of you have written the past few weeks to say thanks, but I could say as much to you. Nancy and I are grateful for the opportunity you gave us to serve.
"""

text_splitter = CharacterTextSplitter()
texts = text_splitter.split_text(test_string)

docs = [Document(page_content=t) for t in texts[:3]]  # Only using the first 3 pages for demonstration

chain = load_summarize_chain(llm, chain_type="map_reduce")

output_summary = chain.invoke(docs)

summary_text = output_summary.get("output_text", "")

wrapped_text = textwrap.fill(summary_text, width=180)
print(wrapped_text)
