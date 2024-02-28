## import statements
import os

import pandas as pd
import torch
from tqdm import tqdm
import numpy as np

from opensearchpy import OpenSearch, helpers
from langchain.text_splitter import RecursiveCharacterTextSplitter

from sentence_transformers import SentenceTransformer

from concurrent.futures import ThreadPoolExecutor
import threading


def read_xlsx_return_df (xlsx_filename): 
    reader = pd.read_csv(
        xlsx_filename,
    )
    reader.fillna('', inplace=True)

    reader.columns = ["id", "doi", "authors","title", "abstract"]
    conv_data = rows_to_dict(reader)[170:180]
    lines = reader.shape[0]
    return conv_data, lines

    authors = str(paper['authors']).replace("[","").replace("]","").replace("'","")

    information = INFORMATION_TEMPLATE.format(
        authors = authors,
        title = paper['title'],
        abstract = paper['abstract']
    )

    # chunk the document
    text_splits = text_splitter.split_text(information)

    logfile.write(f"Information: {information}\n")
    logfile.write(f"Chunk size: {len(text_splits)}\n")
    logfile.write("* * * "*10)

    for id, chunk in enumerate(text_splits):

        # create embedding of the chunk
        embedding = model.encode(chunk)

        doc_id = f"{paper['id']}_{id}"

        doc = {
            "id": doc_id,
            "doi": paper["doi"],
            "authors": authors,
            "text": chunk,
            "embedding": embedding
        }

        logfile.write(f"Chunk: {chunk}\n")

        try:
            # Index the document
            res = client.index(index=INDEX_NAME, body=doc)
            logfile.write(str(res))

        except Exception as e:
            print(f"Missed {paper['id']}")
            logfile.write(f"missed {paper['id']} \n")
            print(e)

        logfile.write("- - - - "*20)

# Function to convert each row to a dictionary
def rows_to_dict(dataframe):
    # Convert each row to a dictionary and append to an array
    dict_array = [row.to_dict() for index, row in dataframe.iterrows()]

    return dict_array
       
if __name__ == "__main__":

    #client data 
    client = OpenSearch(
    hosts=["https://admin:2NCbjLJWWzIFw@ec2-34-207-194-37.compute-1.amazonaws.com:9200/"],
        http_compress=True,
        use_ssl=True,
        verify_certs=False,
        ssl_assert_hostname=False,
        ssl_show_warn=False,
    )

    INDEX_NAME = "search-pubmed-data"
    filePath = "./extracted_outputs.csv"
    logfile = open("./log.txt","a+")

    # Chunking module
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""],
    )

    # Embedding model
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    INFORMATION_TEMPLATE = '''Authors: {authors}
    Title: {title}
    Abstract: {abstract}'''

    conv_data, lines = read_xlsx_return_df(filePath)

    def chunk_upload_data(paper): 
        print("THREAD ID: ", threading.get_ident())
        authors = str(paper['authors']).replace("[","").replace("]","").replace("'","")

        information = INFORMATION_TEMPLATE.format(
            authors = authors,
            title = paper['title'],
            abstract = paper['abstract']
        )

        # chunk the document
        text_splits = text_splitter.split_text(information)

        logfile.write(f"Information: {information}\n")
        logfile.write(f"Chunk size: {len(text_splits)}\n")
        logfile.write("* * * "*10)

        for id, chunk in enumerate(text_splits):

            # create embedding of the chunk
            embedding = model.encode(chunk)

            doc_id = f"{paper['id']}_{id}"

            doc = {
                "id": doc_id,
                "doi": paper["doi"],
                "authors": authors,
                "text": chunk,
                "embedding": embedding
            }

            logfile.write(f"Chunk: {chunk}\n")

            try:
                # Index the document
                #res = client.index(index=INDEX_NAME, body=doc)
                #logfile.write(str(res))
                print("DOC ID: ", doc["id"])

            except Exception as e:
                print(f"Missed {paper['id']}")
                logfile.write(f"missed {paper['id']} \n")
                print(e)

            logfile.write("- - - - "*20)

    with ThreadPoolExecutor() as executor:
        executor.map(chunk_upload_data, conv_data)