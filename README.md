# Document Summarizer Chatbot (CLI)

This is a simple Python-based command-line chatbot that summarizes long documents using the Hugging Face BART model.

## 📦 Features

- Accepts text or `.txt` files up to 10,000 words
- Summarizes using BART (`facebook/bart-large-cnn`)
- Handles long documents with chunking
- Supports short, medium, and long summary lengths
- Language detection (English only)
- Saves output to a file with progress indicators

## 🚀 Installation

```bash
git clone https://github.com/yourusername/summarizer-chatbot.git
cd summarizer-chatbot
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🧠 Usage

```bash
# Summarize a text file with medium-length summary
python summarizer_chatbot.py --file input.txt --length medium --output summary.txt

# Direct text input
python summarizer_chatbot.py --text "Your text here..." --length short
```

## 📝 Sample Summaries

Find 5 sample summaries in the `sample_summaries/` folder.

## 📚 Requirements

- Python 3.8+
- transformers
- torch
- nltk
- langdetect
- tqdm

## 🧪 Tested On

- News articles
- Blog posts
- Research papers
- Product reviews
- Short stories

## 📄 License

MIT License