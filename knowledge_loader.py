from pathlib import Path

def load_docs():
    docs_path = Path(__file__).parent / "knowledge"

    if not docs_path.exists():
        return ""

    documents = []

    for file in sorted(docs_path.rglob("*.md")):
        try:
            content = file.read_text(encoding="utf-8")

            documents.append(
                f"""
==================================================
DOCUMENT: {file.name}
==================================================

{content}
"""
            )
        except Exception as e:
            print(f"Could not load {file}: {e}")

    return "\n".join(documents)