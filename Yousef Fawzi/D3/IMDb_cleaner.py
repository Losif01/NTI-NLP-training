import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string
import re
from collections import Counter
import numpy as np

# Emoji and emoticon dictionary
EMOTIONS_DICT = {
    "😀": "grinning face",
    "😁": "beaming face with smiling eyes",
    "😂": "face with tears of joy",
    "🤣": "rolling on the floor laughing",
    "😃": "grinning face with big eyes",
    "😄": "grinning face with smiling eyes",
    "😅": "grinning face with sweat",
    "😉": "winking face",
    "😊": "smiling face with smiling eyes",
    "😍": "smiling face with heart eyes",
    "😘": "face blowing a kiss",
    "😎": "smiling face with sunglasses",
    "🥰": "smiling face with hearts",
    "😒": "unamused face",
    "😭": "loudly crying face",
    "😢": "crying face",
    "😡": "angry face",
    "😠": "angry face",
    "🤬": "face with symbols on mouth",
    "😩": "weary face",
    "😤": "face with steam from nose",
    "🤯": "exploding head",
    "😱": "screaming in fear",
    "👍": "thumbs up",
    "👎": "thumbs down",
    "❤️": "love",
    "💔": "broken heart",
    "🔥": "fire",
    "💯": "hundred points",
    "🙏": "folded hands",
    ":)": "smiley face",
    ":-)": "smiley face",
    ":D": "grinning face",
    ":-D": "grinning face",
    ":(": "sad face",
    ":-(": "sad face",
    ":/": "unsure face",
    ":-/": "unsure face",
    ":|": "neutral face",
    ":-|": "neutral face",
    ":'(": "crying face",
    ":'-)": "crying face",
    ":P": "playful face",
    ":-P": "playful face",
    ";)": "winking face",
    ";-)": "winking face",
    ">:(": "angry face",
    "<3": "love",
    "</3": "broken heart"
}

class IMDbPreprocessor:
    def __init__(self):
        """Initialize the preprocessor with NLTK tools."""
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.punctuation = set(string.punctuation)
        self.vocab = None
        self.word_to_idx = None
        self.max_len = None

    def load_data(self, path):
        """Load the IMDb dataset from a CSV file and remove missing values."""
        df = pd.read_csv(path)
        df = df.dropna()
        return df['review'].tolist(), df['sentiment'].tolist()

    def clean_text(self, text):
        """Clean and tokenize a single review text using NLTK, remove HTML tags, and replace emojis/emoticons."""
        text = text.lower()
        text = re.sub(r'<[^>]+>', '', text)
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
        for emoticon, meaning in EMOTIONS_DICT.items():
            escaped_emoticon = re.escape(emoticon)
            text = re.sub(rf'\b{escaped_emoticon}\b', meaning, text)
        text = ''.join([char for char in text if char not in self.punctuation])
        text = ''.join([char for char in text if not char.isdigit()])
        words = word_tokenize(text)
        words = [self.lemmatizer.lemmatize(word) for word in words if word not in self.stop_words]
        return words

    # def get_tokenized_reviews(self, path):
    #     """Return the tokenized words for each review before numerical conversion."""
    #     reviews, _ = self.load_data(path)
    #     tokenized = [self.clean_text(review) for review in reviews]
    #     return tokenized

    def build_vocab(self, tokenized_reviews, vocab_size=None):
        """Build a vocabulary from tokenized reviews."""
        all_words = [word for review in tokenized_reviews for word in review]
        word_counts = Counter(all_words)
        if vocab_size:
            self.vocab = [word for word, _ in word_counts.most_common(vocab_size - 1)]
        else:
            self.vocab = list(word_counts.keys())
        self.word_to_idx = {word: idx + 1 for idx, word in enumerate(self.vocab)}
        self.word_to_idx['UNK'] = len(self.word_to_idx) + 1

    def tokenize_and_convert(self, reviews):
        """Tokenize reviews and convert to numerical sequences."""
        tokenized = [self.clean_text(review) for review in reviews]
        if self.vocab is None:
            self.build_vocab(tokenized)
        sequences = [[self.word_to_idx.get(word, self.word_to_idx['UNK']) for word in review] for review in tokenized]
        return sequences

    def pad_sequences(self, sequences, max_len=None):
        """Pad sequences to a uniform length."""
        if max_len is None:
            max_len = max(len(seq) for seq in sequences)
        self.max_len = max_len
        padded = np.zeros((len(sequences), max_len), dtype=int)
        for i, seq in enumerate(sequences):
            if len(seq) > max_len:
                padded[i] = seq[:max_len]
            else:
                padded[i, :len(seq)] = seq
        return padded

    def encode_labels(self, labels):
        """Encode sentiment labels to numerical values (positive=1, negative=0)."""
        return [1 if label == 'positive' else 0 for label in labels]

    def preprocess(self, path, max_len=None):
        """Orchestrate the full preprocessing pipeline."""
        reviews, labels = self.load_data(path)
        sequences = self.tokenize_and_convert(reviews)
        padded_sequences = self.pad_sequences(sequences, max_len)
        encoded_labels = self.encode_labels(labels)
        return padded_sequences, encoded_labels


# preprocessor = IMDbPreprocessor()
# tokenized_reviews = preprocessor.get_tokenized_reviews(r'/home/skillissue/Desktop/FAIButBetter/NTI NLP/D3/IMDB Dataset.csv')
# for i, tokens in enumerate(tokenized_reviews[:5]):  
#     print(f"Review {i+1} tokens: {tokens}")