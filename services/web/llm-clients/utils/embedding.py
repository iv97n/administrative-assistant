import numpy as np
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
 

class DocumentRanker:
    def __init__(self):
        # Initialize TF-IDF Vectorizer
        self.stop_words = stopwords.words("catalan")

        self.vectorizer = TfidfVectorizer(stop_words=self.stop_words)

    def rank_documents(self, query, documents, top_k):
        """
        Rank the documents based on their relevance to the query.

        Parameters:
        - query: The query text to rank documents against.
        - documents: A list of documents (texts) to rank.
        
        Returns:
        - A sorted list of tuples (document_index, similarity_score)
        """
        # Combine the query with the documents
        all_texts = [query] + documents
        
        # Fit the TF-IDF vectorizer to the combined texts
        tfidf_matrix = self.vectorizer.fit_transform(all_texts)
        
        # Compute cosine similarity between the query and all documents
        query_vector = tfidf_matrix[0]
        document_vectors = tfidf_matrix[1:]
        similarity_scores = cosine_similarity(query_vector, document_vectors).flatten()

        # Rank documents based on their similarity to the query
        ranked_docs = [(index, score) for index, score in enumerate(similarity_scores)]
        ranked_docs = sorted(ranked_docs, key=lambda x: x[1], reverse=True)

        return ranked_docs[:top_k]
    
    def get_context_from_ranked_documents(self, query, documents, top_k=5):
        """
        Get the concatenated context from the top_k ranked documents based on their relevance to the query.

        Parameters:
        - query: The query text to rank documents against.
        - documents: A list of documents (texts) to rank.
        - top_k: The number of top documents to return for context.
        
        Returns:
        - A string that contains the concatenated text of the top_k most relevant documents.
        """
        # Rank the documents based on the query
        ranked_documents = self.rank_documents(query, documents, top_k=top_k)

        # Create the context by concatenating the content of the top_k ranked documents
        context = ""
        for index, score in ranked_documents:
            # Use the index to get the actual document from the original list
            context += documents[index] + "\n"
        
        return context






