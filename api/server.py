import uvicorn

if __name__ == "__main__":
    # uvicorn.run("api/index:app", host="0.0.0.0", port=8080, reload=True)
    uvicorn.run("index:app", reload=True)
