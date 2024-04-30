from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_recommenders():
    return {"topic_recommender", "preference-based_recommender"}


@app.get("/train/{recommender}")
def train(recommender: str):
    return {"item_id": recommender}