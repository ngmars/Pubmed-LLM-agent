Authors of Repo: 
1. ngmars - Nitish Gopinath (Matrikel Nr - 4738384)
2. Dilmukhammed - Turdimuratov Dilmukhammed (Matrikel Nr - 4738284)
3. Richa Garg 
4. Palkin Singh
   
## Please send an email to nitish.gopinath@stud.uni-heidelberg.de, to turn on the AWS EC2 instance where the OpenSearch DB is hosted

## Repository Structure

  

```
└──  /

├──  Data_Extractor.ipynb

├──  Gemini_LLM_connector.ipynb

├──  LICENSE

├──  OpenSearchConnection

│  ├──  completionRecord.txt

│  ├──  missedIds.txt

│  └──  vecDbTesting.ipynb

├──  RAG.ipynb

├──  README.md

├──  docker-compose-openSearch

│  └──  docker-compose.yml

├──  modelEvaluation.ipynb

├──  requirements.txt

└──  uploadDataToDb.py

```

## Modules

  


| File | Summary |

| [requirements.txt](requirements.txt) | <code>► File to set up the virtual environment</code> |

| [docker-compose.yml](docker-compose-openSearch/docker-compose.yml) | <code>► docker compose file to start the opensearch docker container</code> |

| [Data_Extractor.ipynb](Data_Extractor.ipynb) | <code>► Extracts data and cleans data obtained via Esearch in the XML file and saves only relevant data in the CSV file</code> |

| [uploadDataToDb.py](uploadDataToDb.py) | <code>► Uses created CSV file to upload data to the vector DB, for speed and efficiency multi threading is used</code> |

| [Gemini_LLM_connector.ipynb](Gemini_LLM_connector.ipynb) | <code>► Connection to Gemini LLM, the UI begins to run when all the cells in this file has been run</code> |

| [modelEvaluation.ipynb](modelEvaluation.ipynb) | <code>► Evaluates the output results from the LLM</code> |

| [RAG.ipynb](RAG.ipynb) | <code>► Old code, using Open AI -- DO NOT USE</code> |

---

  

## Getting Started

  

**System Requirements:**
- Ubuntu v16.04/v18.04/v20.04 (8GB RAM minimum)
- Python v3.9 to v3.11

### Installation

  

<h4>From <code>source</code></h4>

  

1. Clone the repository:
 ```
 $ git clone https://github.com/ngmars/Group35-INLPT-WS2023.git

 ```


 2. Change to the project directory:

 ```

 $ cd Group35-INLPT-WS2023

 ```



3. Install the dependencies:

 ```

 $ pip install -r requirements.txt

 ```

3. Extract data from PUBMED - install Esearch CLI and run in the terminal: 

 ```

 esearch -db pubmed -query "("intelligence"[Title/Abstract]) AND ((fha[Filter]) AND (2014:2024[pdat]))" | efetch -format xml > pubmed_results.xml

 ```
  
4. Save extracted data in CSV file: 

 ```
 Run all cells in Data_Extractor.ipynb - This saves responses in extracted_outputs.csv

 ```
5. Create index in Vector DB: 

 ```

 Run all cells in createIndex.ipynb - This saves responses in extracted_outputs.csv

 ```
 6. Upload data to Vector DB: 

 ```

 python uploadDataToDb.py

 ```
7. Start Chatbot UI

 ```

 Run all cells in Gemini_LLM_connector.ipynb - The last cell starts the chatbot

 ```
8. Run LLM evaluation
 ```

 Run all cells in modelEvaluation.ipynb - The evaluates the LLM

 ```
