import argparse
import os
from transformers import pipeline
from langdetect import detect
from tqdm import tqdm
import nltk

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Load model globally
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

def chunk_text(text, max_tokens=1024):
    sentences = sent_tokenize(text)
    chunks, current_chunk = [], ""
    for sentence in sentences:
        if len(current_chunk.split()) + len(sentence.split()) <= max_tokens:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def summarize_text(text, min_len=150, max_len=300):
    chunks = chunk_text(text)
    summarized_chunks = []
    for chunk in tqdm(chunks, desc="Summarizing chunks"):
        summary = summarizer(chunk, min_length=min_len, max_length=max_len, do_sample=False)[0]['summary_text']
        summarized_chunks.append(summary.strip())
    return " ".join(summarized_chunks)

def main():
    parser = argparse.ArgumentParser(description="Summarize long documents using BART model.")
    parser.add_argument('--text', type=str, help="Direct text input")
    parser.add_argument('--file', type=str, help="Path to input .txt file")
    parser.add_argument('--length', choices=['short', 'medium', 'long'], default='medium', help="Summary length")
    parser.add_argument('--output', type=str, default='summary_output.txt', help="File to save summary")

    args = parser.parse_args()

    if args.text:
        input_text = args.text
    elif args.file:
        if not os.path.exists(args.file):
            print("Error: File not found.")
            return
        with open(args.file, 'r', encoding='utf-8') as f:
            input_text = f.read()
    else:
        print("Please provide input via --text or --file.")
        return

    if detect_language(input_text) != 'en':
        print("Error: Only English text is supported.")
        return

    # Set summary length parameters
    if args.length == 'short':
        min_len, max_len = 50, 100
    elif args.length == 'long':
        min_len, max_len = 300, 500
    else:
        min_len, max_len = 150, 300

    summary = summarize_text(input_text, min_len, max_len)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(summary)
    print(f"✅ Summary saved to {args.output}")

if __name__ == "__main__":
    main()