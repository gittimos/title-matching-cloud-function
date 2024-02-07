import functions_framework
import numpy as np
from openai import OpenAI
from google.cloud import storage

openai_client = OpenAI()

def get_embedding(text, model="text-embedding-ada-002"):
    """ Returns the embedding of the text from OpenAI's API """
    return openai_client.embeddings.create(input=[text], model=model).data[0].embedding


@functions_framework.http
def title_matching(request):

    request_json = request.get_json(silent=True)
    request_args = request.args

    storage_client = storage.Client()
    bucket = storage_client.get_bucket("embeddingdata")

    # load titles
    blob = bucket.blob("titles.txt")
    blob.download_to_filename("titles.txt")
    titles = []
    f = open("titles.txt", "r")
    for title in f:
        titles.append(title)

    # load embeddings
    blob = bucket.blob("embeddings.npy")
    blob.download_to_filename("embeddings.npy")
    embeddings = np.load("embeddings.npy")

    # find matching title
    if request_json and "title" in request_json:
        title = request_json["title"]
        vector = get_embedding(title)
        scalar_products = np.dot(embeddings.T, vector)
        max_index = np.argmax(scalar_products)
        matching_title = titles[max_index]
    elif request_args and "title" in request_args:
        title = request_json["title"]
        vector = get_embedding(title)
        scalar_products = np.dot(embeddings.T, vector)
        max_index = np.argmax(scalar_products)
        matching_title = titles[max_index]
    else:
        matching_title = "No match found!"
    
    return f"{matching_title}"