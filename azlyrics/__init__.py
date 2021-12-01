from fastapi import FastAPI, Request
from slowapi.errors import RateLimitExceeded
from slowapi.extension import Limiter,_rate_limit_exceeded_handler
from slowapi.util import get_remote_address

app = FastAPI()
limiter =  Limiter(key_func=get_remote_address)

app.state.limiter = Limiter(key_func=get_remote_address)
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.get("/")
@limiter.limit("8/minute")
async def root(request : Request):
    return {"message": "Hello World"}
