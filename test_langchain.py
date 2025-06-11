# load environments
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# set api keys
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# set langsmith tracing

os.environ["LANGSMITH_PROJECT"]=os.getenv("LANGSMITH_PROJECT")
os.environ["LANGSMITH_TRACING_V2"]="true"

# initialize model and provide prompt
llm = ChatGroq(model="gemma2-9b-it")
outpurParser = JsonOutputParser()
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert in geography. Answer the user's question in the following JSON format:\n"
               "{{\n"
               '  "continents": ["list of continents"],\n'
               '  "most_populated_continent": "continent name"\n'
               "}}"),
    ("user", "{question}")
])

chain = prompt | llm | outpurParser
result = chain.invoke({
    "question": "What are continents in the world? And which is the most populated continent?"
    })
print(result)


