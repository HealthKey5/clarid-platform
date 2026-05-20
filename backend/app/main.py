from fastapi import FastAPI

app = FastAPI(title="ClarID API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "env": "dev"}
