import chromadb
from chromadb.utils import embedding_functions
import os
from pypdf import PdfReader

# --- Configuration ---
DOCS_FOLDER = "documents"
COLLECTION_NAME = "private_docs"
PERSIST_DIRECTORY = "db_storage" # Folder to save the database

print("--- Starting Document Ingestion ---")

# --- Initialize ChromaDB and the Embedding Model ---
# Using a high-quality, free, and local model for creating embeddings
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Set up the ChromaDB client
client = chromadb.PersistentClient(path=PERSIST_DIRECTORY)

# Get or create the collection
collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_func,
    metadata={"hnsw:space": "cosine"} # Using cosine distance for similarity
)

# --- Read and Chunk Documents ---
documents = []
metadatas = []
ids = []
doc_id_counter = 1

for filename in os.listdir(DOCS_FOLDER):
    if filename.endswith(".pdf"):
        filepath = os.path.join(DOCS_FOLDER, filename)
        print(f"-> Reading PDF: {filename}")
        reader = PdfReader(filepath)

        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                # Each page becomes a separate "document" in the DB
                documents.append(text)
                metadatas.append({'source': filename, 'page': i + 1})
                ids.append(f"{filename}_page_{i+1}")
                doc_id_counter += 1

# --- Ingest into ChromaDB ---
if documents:
    print(f"\n-> Found {len(documents)} text chunks to ingest.")
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    print(f"✅ Successfully ingested documents into the '{COLLECTION_NAME}' collection.")
else:
    print("-> No new documents found to ingest.")

print("--- Ingestion Complete ---")