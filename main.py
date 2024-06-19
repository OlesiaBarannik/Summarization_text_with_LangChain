from fastapi import FastAPI, Request, HTTPException
from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv


load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("MY_OPENAI_API_KEY")

# Initialize ChatOpenAI instance with GPT-3.5-turbo model
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

# Load summarization chain with map_reduce type
chain = load_summarize_chain(llm, chain_type="map_reduce")

app = FastAPI()

@app.post("/summarize")
async def summarize(request: Request):
    """
    Processes a POST request to /summarize endpoint to generate a summary of input text.

    Parameters:
    - request (Request): FastAPI request containing JSON with text to be summarized.

    Returns:
    - dict: JSON object with key "summary" containing the generated summary text,
      or JSON object with key "error" in case of an error.
    """
    try:
        data = await request.json()
        text = data.get("text", "")

        # Check if text is empty or not provided
        if not text.strip():
            raise HTTPException(status_code=400, detail="Text is empty or not provided")

        # Create a Document object with the input text
        document = Document(page_content=text)

        # Invoke the summarization chain with input text
        output_summary = chain.invoke([document])
        summary_text = output_summary.get("output_text", "")

        return {"summary": summary_text}

    except HTTPException as http_error:
        return {"error": str(http_error)}

    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI app with uvicorn server
    uvicorn.run(app, host="127.0.0.1", port=8000)