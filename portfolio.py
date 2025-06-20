import pandas as pd
import chromadb
import uuid
import os


class Portfolio:
    def __init__(self, file_path=None):
        if file_path is None:
            # Auto-resolve relative to the current file
            base_path = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(base_path, "resource", "my_portfolio.csv")

        self.file_path = file_path
        self.data = pd.read_csv(self.file_path)
        self.chroma_client = chromadb.PersistentClient(path="vectorstore")
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if self.collection.count() == 0:
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["Techstack"]],  # <- must be list
                    metadatas=[{"links": row["Links"]}],  # <- must be list
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        results = self.collection.query(query_texts=skills, n_results=2)
        return results.get('metadatas', [[]])[0]  # returns the first list of metadata
