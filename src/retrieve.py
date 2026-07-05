"""
Retrieval module for querying faculty profiles using ChromaDB vector similarity search.
Provides functions to search and retrieve faculty research information.
"""

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction


def initialize_collection():
    """
    Initialize and return the ChromaDB collection for faculty profiles.
    Uses SentenceTransformer embeddings for semantic search.
    
    Returns:
        chromadb.Collection: The faculty_profiles collection
    """
    # Initialize embedding function - same as used during data ingestion
    embedding_function = SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Connect to ChromaDB
    client = chromadb.PersistentClient(path="./chroma_db")
    
    # Get the faculty profiles collection
    collection = client.get_collection(
        name="faculty_profiles",
        embedding_function=embedding_function
    )
    
    return collection


def search_faculty(query, num_results=3):
    """
    Search for faculty members based on a research query.
    Uses semantic similarity to find relevant faculty profiles.
    
    Args:
        query (str): The search query (e.g., "machine learning expert")
        num_results (int): Number of results to return (default: 3)
    
    Returns:
        dict: Query results with documents and metadata
    """
    collection = initialize_collection()
    
    results = collection.query(
        query_texts=[query],
        n_results=num_results
    )
    
    return results


def display_search_results(results):
    """
    Display search results in a user-friendly format.
    
    Args:
        results (dict): Query results from ChromaDB
    """
    if not results["documents"] or not results["documents"][0]:
        print("\n❌ No matching faculty profiles found. Please try a different query.")
        return
    
    print("\n✅ Matching Faculty Profiles:")
    print("-" * 60)
    
    for i, document in enumerate(results["documents"][0], 1):
        print(f"\nMatch {i}:")
        print(document)
        print("-" * 60)