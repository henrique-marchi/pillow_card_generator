import uvicorn


def main():
    uvicorn.run(
        app="api:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="debug"
    )


if __name__ == '__main__':
    main()