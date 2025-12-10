#############################

  User guide for 'pelachat'
  
  
Author: Guillaume Chero
November 2025
Version: Python 3.9
#############################  

Prerequiste:
- Install Ollama from (https://ollama.com/)
- Download model from terminal
-- ollama pull nomic-embed-text
-- ollama pull mistral
- Set Python 3.9 as interpreter and create a .venv

0) Activate .venv 
Run in the command:
"""
 .venv\Scripts\activate       
"""
and install requirement

1) populate_database.py
This script allows you to populate the PDF file database.
Simply add the PDFs to the project's data file and run the command:
"""
python .\populate_database.py   
"""
You will be able to see the number of chunks added to the dataset.
Please note that the function may stop with an error if you add too many PFDs at once. 


2) query_data.py
This script allows you to submit a request to pelachat. Simply call the function followed by your question:
"""
python query_data.py "what is the abundance estimate for Harbour porpoise in 2022 ?"
python query_data.py "what is the abundance estimate for Harbour porpoise in 2022 in the Belt Sea?"
"""

3) streamlit.py
Streamlit allows you to create an HTML page to serve as an application interface for querying pelachat: 
"""
streamlit run .\streamlit.py
"""


4) get_embedding_function.py
This script encapsulates the embedding function that is reused in other scripts.



5) Project Structure
The Python project must contain several folders:
- ./data: to contain the PDFs to be read
- ./chroma: to store the databases created