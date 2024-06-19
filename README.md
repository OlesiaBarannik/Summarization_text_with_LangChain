# FastAPI Text Summarizer

## Setup

### Create a virtual environment (optional but recommended)

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### Install dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Set up environment variables

Create a `.env` file in the root directory of your project with the following content:

```dotenv
# add your OpenAI secret key
MY_OPENAI_API_KEY = "your-openai-key"
```

Replace `"your-openai-key"` with your actual OpenAI API key.

### Run the application

Start the FastAPI application using uvicorn:

```bash
uvicorn main:app --reload
```

The API will start running at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Usage

### Summarize Text

Send a POST request to `http://127.0.0.1:8000/summarize` with a JSON body containing the text to be summarized:

```json
{
  "text": "Your input text goes here."
}
```

Replace `"Your input text goes here."` with the text you want to summarize.

### Example

Assuming the FastAPI server is running locally, you can test the endpoint by sending a POST request with JSON data 
to `http://127.0.0.1:8000/summarize`.

**Request:**

```json
{
   "text": "My fellow Americans, this is the 34th time I'll speak to you from the Oval Office, and the last. We've been together eight years now, and soon it'll be time for me to go. But before I do, I wanted to share some thoughts, some of which I have been saving for a long time. It's been the honor of my life to be your President. So many of you have written the past few weeks to say thanks, but I could say as much to you. Nancy and I are grateful for the opportunity you gave us to serve."
}
```

**Expected Output:**

```json
{
    "summary": "The current President of the United States delivers their final address from the Oval Office after eight years in office, expressing gratitude for the opportunity to serve and sharing final thoughts with the American people."
}
```