# basic_langchain
LLM Application with langchain

- Python 3.12
- FastAPI
- LangChain
- OpenAI

### Directory Structure
```
basic_langchain/
├── chain/
│   ├── retrieval/
│   │   └── base.py
│   └── pdf_retrieval_chain.py
├── common/
│   └── utils/
│       └── utils.py
├── resources/
├── test/
│   └── test_chat.py
├── .env
├── .env_sample
├── Dockerfile
├── README.md
├── main.py
├── poetry.lock
├── pyproject.toml
└── __pycache__/
```

### Run (Poetry)
`poetry run uvicorn main:app --host 0.0.0.0 --port 8000`

### Run (Docker)
`docker build -t basic_langchain_app .`

`docker run -p 8000:8000 basic_langchain_app`
