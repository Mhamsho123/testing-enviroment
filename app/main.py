# app/main.py

from contextlib import asynccontextmanager

from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.chroma_store import add_article_to_chroma
from app.chroma_store import delete_article_from_chroma
from app.chroma_store import search_articles_in_chroma
from app.database import create_db_and_tables
from app.database import get_db
from app.models import Article
from app.schemas import ArticleCreate
from app.schemas import ArticleRead
from app.schemas import ArticleUpdate
from app.schemas import SearchRequest


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def home():
    return {
        "message": "Helpdesk API is running"
    }


@app.post("/articles", response_model=ArticleRead)
async def create_article(
    article_data: ArticleCreate,
    db: AsyncSession = Depends(get_db)
):
    # TODO 1:
    # Create an Article object.
    #
    # article = Article(
    #     title=???,
    #     content=???
    # )

    # TODO 2:
    # Add it to the database.
    #
    # db.add(article)

    # TODO 3:
    # Commit the database.
    #
    # await db.commit()

    # TODO 4:
    # Refresh the article so it gets its ID.
    #
    # await db.refresh(article)

    # TODO 5:
    # Add the article to ChromaDB.
    #
    # add_article_to_chroma(
    #     article_id=article.id,
    #     title=article.title,
    #     content=article.content
    # )

    # TODO 6:
    # Return the article.
    pass


@app.get("/articles", response_model=list[ArticleRead])
async def get_articles(
    db: AsyncSession = Depends(get_db)
):
    # TODO 1:
    # Execute a select query.
    #
    # result = await db.execute(select(Article))

    # TODO 2:
    # Convert result into list of Article objects.
    #
    # articles = result.scalars().all()

    # TODO 3:
    # Return articles.
    pass


@app.get("/articles/{article_id}", response_model=ArticleRead)
async def get_article(
    article_id: int,
    db: AsyncSession = Depends(get_db)
):
    # TODO 1:
    # Get article by ID.
    #
    # article = await db.get(Article, article_id)

    # TODO 2:
    # If article is None, raise 404 error.
    #
    # if article is None:
    #     raise HTTPException(status_code=404, detail="Article not found")

    # TODO 3:
    # Return article.
    pass


@app.put("/articles/{article_id}", response_model=ArticleRead)
async def update_article(
    article_id: int,
    article_data: ArticleUpdate,
    db: AsyncSession = Depends(get_db)
):
    # TODO 1:
    # Get article by ID.

    # TODO 2:
    # If not found, raise 404.

    # TODO 3:
    # If article_data.title is not None, update title.

    # TODO 4:
    # If article_data.content is not None, update content.

    # TODO 5:
    # Commit database.

    # TODO 6:
    # Refresh article.

    # TODO 7:
    # Update ChromaDB too using add_article_to_chroma.

    # TODO 8:
    # Return article.
    pass


@app.delete("/articles/{article_id}")
async def delete_article(
    article_id: int,
    db: AsyncSession = Depends(get_db)
):
    # TODO 1:
    # Get article by ID.

    # TODO 2:
    # If not found, raise 404.

    # TODO 3:
    # Delete article from SQLite.
    #
    # await db.delete(article)

    # TODO 4:
    # Commit database.
    #
    # await db.commit()

    # TODO 5:
    # Delete from ChromaDB.
    #
    # delete_article_from_chroma(article_id)

    # TODO 6:
    # Return message.
    #
    # return {"message": "Article deleted"}
    pass


@app.post("/search")
def search_articles(search_data: SearchRequest):
    # TODO 1:
    # Search ChromaDB.
    #
    # results = search_articles_in_chroma(search_data.query)

    # TODO 2:
    # Return query and results.
    #
    # return {
    #     "query": search_data.query,
    #     "results": results
    # }
    pass