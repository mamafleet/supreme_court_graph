import fitz  # PyMuPDF
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

# Download NLTK resources if not already done
nltk.download('stopwords')

# Function to extract text from one PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Clean and tokenize text
import re

def tokenize_text(text):
    # Lowercase and extract word-like tokens
    tokens = re.findall(r'\b\w+\b', text.lower())
    stop_words = set(stopwords.words('english'))

    # Filter out stopwords and purely numeric tokens
    cleaned_tokens = [t for t in tokens if t not in stop_words and not t.isnumeric()]
    return cleaned_tokens


# Visualize token data
def visualize_tokens_by_pdf(token_data, top_n=20):
    for filename, tokens in token_data.items():
        print(f"\n📄 {filename}: {len(tokens)} tokens")
        counter = Counter(tokens)
        most_common = counter.most_common(top_n)

        if not most_common:
            print(f"No valid tokens found in {filename}.")
            continue

        words, counts = zip(*most_common)
   
    for label, tokens in token_data.items():
        print(f"\n🔢 Top words in {label}:")
        counter = Counter(tokens)
        for word, count in counter.most_common(10):
            print(f"{word}: {count}")

# Main analysis for specific PDFs
def analyze_selected_pdfs():
    token_data = {}

     # Replace these paths with your actual local paths in VS Code
    pdfs = {
    "Trump v. Anderson": "Trump v. Anderson.pdf",
    "Trump v. Anderson OA": "Trump v. Anderson OA.pdf",
    "United States v. Rahimi": "United States v. Rahimi.pdf",
    "United States v. Rahimi OA": "United States v. Rahimi OA.pdf",
    "Garland v. Cargill": "Garland v. Cargill.pdf",
    "Garland v. Cargill OA": "Garland v. Cargill OA.pdf",
    "Corner Post, Inc. v. Board of Governors": "Corner Post, Inc. v. Board of Governors.pdf",
    "Corner Post, Inc. v. Bd. of Governors, FRS OA": "Corner Post, Inc. v. Bd. of Governors, FRS OA.pdf",
    "McIntosh v. United States": "McIntosh v. United States.pdf",
    "McIntosh v. United States OA": "McIntosh v. United States OA.pdf",
    "Moody v. NetChoice, LLC": "Moody v. NetChoice, LLC.pdf",
    "Moody v. NetChoice, LLC OA": "Moody v. NetChoice, LLC OA.pdf",
    "Ohio v. EPA": "Ohio v. EPA.pdf",
    "Ohio v. EPA OA": "Ohio v. EPA OA.pdf",
    "Coinbase v. Suski": "Coinbase v. Suski.pdf",
    "Coinbase, Inc. v. Suski OA": "Coinbase, Inc. v. Suski OA.pdf",
    "Cantero v. Bank of America, N. A.": "Cantero v. Bank of America, N. A..pdf",
    "Cantero v. Bank of America, N.A. OA": "Cantero v. Bank of America, N.A. OA.pdf",
    "Bissonnette v. LePage Bakeries Park St., LLC": "Bissonnette v. LePage Bakeries Park St., LLC.pdf",
    "Bissonnette v. LePage Bakeries Park St., LLC OA": "Bissonnette v. LePage Bakeries Park St., LLC OA.pdf",
    "Warner Chappell Music, Inc. v. Nealy": "Warner Chappell Music, Inc. v. Nealy.pdf",
    "Warner Chappell Music, Inc. v. Nealy OA": "Warner Chappell Music, Inc. v. Nealy OA.pdf"
}


    for label, path in pdfs.items():
        print(f"🔍 Processing: {label}")
        text = extract_text_from_pdf(path)
        tokens = tokenize_text(text)
        token_data[label] = tokens

    visualize_tokens_by_pdf(token_data)

# Run the analysis
if __name__ == "__main__":
    analyze_selected_pdfs()

