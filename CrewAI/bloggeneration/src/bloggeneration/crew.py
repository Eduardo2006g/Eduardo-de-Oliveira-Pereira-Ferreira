from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from tools.ReadPDFTool import ReadPDFTool
from dotenv import load_dotenv
import os

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

llm = LLM(
    model="gemini/gemini-1.5-pro", 
    verbose=True,
    temperature=0.5,
    api_key=google_api_key      
)

@CrewBase
class BlogGeneration():
    """Bloggeneration crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self, pdfDir: str, *args, **kwargs):
        self.pdfDir = pdfDir
        super().__init__(*args, **kwargs)

    @agent
    def pdf_reader(self) -> Agent:
        return Agent(
            config=self.agents_config['pdf_reader'],
            verbose=True,
            llm=llm,
            tools=[ReadPDFTool(pdfDir=self.pdfDir)]  
        )

    @agent
    def information_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['information_extractor'],
            llm=llm,
            verbose=True
        )

    @agent
    def content_summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_summarizer'],
			llm=llm,
            verbose=True
        )

    @agent
    def content_formatter(self) -> Agent:
        return Agent(
            config=self.agents_config['content_formatter'],
			llm=llm,
            verbose=True
        )

    @task
    def document_processing_task(self) -> Task:
        return Task(
            config=self.tasks_config['document_processing_task'],
            tools=[ReadPDFTool(pdfDir=self.pdfDir)]  
        )

    @task
    def data_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_extraction_task'],
            context=[self.document_processing_task()]
        )

    @task
    def content_summary_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_summary_task'],
            context=[self.data_extraction_task()]
        )

    @task
    def blog_post_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['blog_post_creation_task'],
            context=[self.content_summary_task()],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Bloggeneration crew"""
        return Crew(
            agents=self.agents, 
            tasks=self.tasks,    
            process=Process.sequential,
            verbose=True,
        )