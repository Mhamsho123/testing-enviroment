# app/chroma_store.py

import chromadb


client = chromadb.PersistentClient(
    path="./data/chroma"
)


collection = client.get_or_create_collection(
    name="articles"
)


def add_article_to_chroma(
    article_id: int,
    title: str,
    content: str
) -> None:
    collection.upsert(
        ids=[str(article_id)],
        documents=[content],
        metadatas=[
            {
                "title": title
            }
        ]
    )


def delete_article_from_chroma(article_id: int) -> None:
    collection.delete(
        ids=[str(article_id)]
    )


def search_articles_in_chroma(
    query: str,
    n_results: int = 3
) -> list[dict]:
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    output = []

    ids = results.get("ids", [[]])[0]
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    for i in range(len(ids)):
        output.append(
            {
                "id": ids[i],
                "title": metadatas[i].get("title"),
                "content": documents[i],
                "distance": distances[i]
            }
        )

    return output