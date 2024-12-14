from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model='llama3:latest',
    base_url='http://localhost:11434/v1'
)

response = llm.invoke('Conte uma piada')
print(response)
