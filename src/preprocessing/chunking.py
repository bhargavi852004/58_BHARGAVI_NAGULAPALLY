import os
import uuid
from typing import List, Dict
INPUT_DIR = "data/filings_text"
CHUNK_SIZE = 800        # tokens (approx words here)
CHUNK_OVERLAP = 100
def chunk_text(text: str, chunk_size: int, overlap: int) -> List[str]:
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunks.append(" ".join(chunk_words))
        start = end - overlap

    return chunks
def parse_filename(filename: str) -> Dict[str, str]:
    name = filename.replace(".txt", "")
    parts = name.split("_")

    return {
        "ticker": parts[0],
        "form_type": parts[1],
        "filed_year": parts[2] if len(parts) > 2 else "unknown",
        "source_file": filename
    }
def generate_chunks() -> List[Dict]:
    all_chunks = []

    for file in os.listdir(INPUT_DIR):
        if not file.endswith(".txt"):
            continue

        file_path = os.path.join(INPUT_DIR, file)

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        metadata = parse_filename(file)
        chunks = chunk_text(text, CHUNK_SIZE, CHUNK_OVERLAP)

        for idx, chunk in enumerate(chunks):
            chunk_id = f"{metadata['ticker']}_{metadata['form_type']}_{metadata['filed_year']}_{idx}"

            all_chunks.append({
                "chunk_id": chunk_id,
                "text": chunk,
                "metadata": metadata
            })

    print(f"Generated {len(all_chunks)} chunks")
    return all_chunks
if __name__ == "__main__":
    chunks = generate_chunks()
    print(chunks[0])
