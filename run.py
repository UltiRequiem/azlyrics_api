import os

import dotenv
import uvicorn

dotenv.load_dotenv()

config = {
    "debug": False,
    "reload": False,
}

if os.environ.get("ENV") == "development":
    config["debug"], config["reload"] = True, True

if __name__ == "__main__":
    uvicorn.run(
        "azlyrics:app",
        debug=config["debug"],
        reload=config["reload"],
        port=8080,
        host="0.0.0.0",
    )
