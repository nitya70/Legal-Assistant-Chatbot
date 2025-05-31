import os
import glob
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

# Initialize HuggingFace embeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Define domains and paths
domains = ['crime', 'family', 'land']
data_dir = "./data"
vector_db_dir = "./law_vector_db"

# Ensure vector DB directory exists
os.makedirs(vector_db_dir, exist_ok=True)

for domain in domains:
    domain_path = os.path.join(data_dir, domain)
    db_path = os.path.join(vector_db_dir, domain)
    os.makedirs(db_path, exist_ok=True)

    print(f"\n📚 Processing domain: {domain}")

    # Load PDFs in the domain folder
    pdf_files = glob.glob(os.path.join(domain_path, "*.pdf"))
    documents = []

    for pdf in pdf_files:
        print(f"   📄 Loading: {pdf}")
        loader = PyPDFLoader(pdf)
        documents.extend(loader.load())

    if not documents:
        print(f"   ⚠️ No documents found in {domain_path}")
        continue

    # Split into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)

    # Create and save FAISS vector DB
    db = FAISS.from_documents(texts, embedding_model)
    db.save_local(db_path)
    print(f"   ✅ Vector DB saved to: {db_path}")
