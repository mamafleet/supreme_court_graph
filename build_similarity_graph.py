import os
import fitz  # PyMuPDF
import re
import json
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import cosine_similarity

# Tokenize and clean PDF text
def extract_and_clean_text(path):
    text = ""
    with fitz.open(path) as doc:
        for page in doc:
            text += page.get_text()

    tokens = re.findall(r'\b\w+\b', text.lower())
    tokens = [t for t in tokens if t not in ENGLISH_STOP_WORDS and not t.isnumeric()]
    return ' '.join(tokens)

# Set your PDF folder
pdf_folder = "."

# Collect all PDFs and extract text
documents = {}
for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        try:
            filepath = os.path.join(pdf_folder, filename)
            documents[filename] = extract_and_clean_text(filepath)
        except Exception as e:
            print(f"Error with {filename}: {e}")

# Compute cosine similarity
case_names = list(documents.keys())
corpus = [documents[name] for name in case_names]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
similarity_matrix = cosine_similarity(X)

# Build nodes and edges
nodes = [{"id": name} for name in case_names]
links = []
threshold = 0.15  # Tune this to control density

for i in range(len(case_names)):
    for j in range(i + 1, len(case_names)):
        sim = similarity_matrix[i, j]
        if sim >= threshold:
            links.append({
                "source": case_names[i],
                "target": case_names[j],
                "value": round(float(sim), 3)
            })

graph = {"nodes": nodes, "links": links}

# Export to JSON
with open("case_similarity_graph.json", "w") as f:
    json.dump(graph, f, indent=2)

print("✅ case_similarity_graph.json created!")
