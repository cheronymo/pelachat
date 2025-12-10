# Pelachat 	
Pelachat is a Python tool that allows you to set up an LLM (Large Language Model) to create a chatbot.  
This chatbot answers specific questions because it is trained on a local database. The database is set up from a PDF library. 

## Ollama
Pelachat is based on AI stored on the <a href="[http://example.com/](https://ollama.com/)">Ollama</a> platform. This chatbot uses two different models:
* nomic-embed-text: for the embedding function :open_book:	
* mistral: for the chatbot :robot:

## Project structure

### populate_database.py 
This script allows you to populate the PDF file database.
Simply add the PDFs to the project's data file and run the command:

You will be able to see the number of chunks added to the dataset.
Please note that the function may stop with an error if you add too many PFDs at once. 


### query_data.py
This script allows you to submit a request to pelachat. Simply call the function followed by your question:

### streamlit.py
Streamlit allows you to create an HTML page to serve as an application interface for querying pelachat: 

### get_embedding_function.py
This script encapsulates the embedding function that is reused in other scripts.

### Folder chroma and data
In this directory, the data and chroma folders are missing. 
