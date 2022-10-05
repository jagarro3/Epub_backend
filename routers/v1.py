"""app.routers.v1.py"""
import os
from fastapi import APIRouter, UploadFile
from services import lector

EpubRouter = APIRouter()

@EpubRouter.post("/words-most-common")
async def get_words_most_common(file: UploadFile, numWords: int):
    book = lector.readEpub(file)
    return lector.word_most_common(book, numWords)

@EpubRouter.post("/bigrams-most-common")
async def get_words_most_common(file: UploadFile, numWords: int):
    book = lector.readEpub(file)
    return lector.bigrams_most_common(book, numWords)

@EpubRouter.post("/tigrams-most-common")
async def get_words_most_common(file: UploadFile, numWords: int):
    book = lector.readEpub(file)
    return lector.tigrams_most_common(book, numWords)


@EpubRouter.post("/info")
async def get_info(file: UploadFile):
    book = lector.readEpub(file)
    return lector.info(book)