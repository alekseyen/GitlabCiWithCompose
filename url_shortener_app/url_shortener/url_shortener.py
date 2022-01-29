import typing as tp
import uuid

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()

DB_URL = {}


class ToShort(BaseModel):
    url: str


class Shorted(BaseModel):
    url: str
    key: str


@app.post('/shorten', status_code=status.HTTP_201_CREATED, response_model=Shorted)
async def short_url(to_short: ToShort) -> tp.Dict[str, str]:
    key = str(uuid.uuid3(uuid.NAMESPACE_URL, to_short.url))[:10]
    DB_URL[key] = to_short.url

    return {'url': to_short.url, 'key': key}


@app.get('/go/{key}', status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def redirect_to_url(key: str, response: RedirectResponse) -> None:
    if key not in DB_URL:
        raise HTTPException(status_code=404, detail='Url not found.')

    response.headers['location'] = DB_URL[key]

