import os
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

# Create embedding model
embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Create ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

# Create collection
collection = client.get_or_create_collection(
    name="faculty_profiles",
    embedding_function=embedding_function
)

faculty_folder = "./data/faculty"

documents = []
ids = []

for index, filename in enumerate(os.listdir(faculty_folder)):
    if filename.endswith(".txt"):
        file_path = os.path.join(faculty_folder, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        documents.append(text)
        ids.append(f"faculty_{index}")

collection.add(
    documents=documents,
    ids=ids
)

print(f"Successfully added {len(documents)} faculty profiles!")