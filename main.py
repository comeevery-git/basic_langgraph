import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


class QueryModel(BaseModel):
    query: str


openai_api_key = os.getenv("OPENAI_API_KEY")

# LLM 및 프롬프트 템플릿 정의
llm = OpenAI(model="text-davinci-003", api_key=openai_api_key)
prompt_template = PromptTemplate(
    input_variables=["query"],
    template="Answer the following query: {query}"
)

llm_chain = LLMChain(llm=llm, prompt=prompt_template)


@app.post("/generate-response/")
async def generate_response(query_model: QueryModel):
    query = query_model.query
    try:
        response = llm_chain.run(query)
        return {"query": query, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def healthcheck():
    return {"status": "ok"}
