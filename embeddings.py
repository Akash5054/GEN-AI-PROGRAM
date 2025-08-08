import os
from dotenv import load_dotenv
load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

#call embedding model
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vector_embedding = embedding_model.embed_query("apple tree")
print(vector_embedding[:5])

