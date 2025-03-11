from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.ler_pdftool import ler_pdftool

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Bloggeneration():
	"""Bloggeneration crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	pdf_tool = ler_pdftool()

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def pdf_reader(self) -> Agent:
		return Agent(
			config=self.agents_config['pdf_reader'],
			verbose=True
		)

	@agent
	def information_extractor(self) -> Agent:
		return Agent(
			config=self.agents_config['information_extractor'],
			verbose=True
		)
	
	@agent
	def content_summarizer(self) -> Agent:
		return Agent(
			config=self.agents_config['content_summarizer'],
			verbose=True
		)
	
	@agent
	def content_formatter(self) -> Agent:
		return Agent(
			config=self.agents_config['content_formatter'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def document_processing_task(self) -> Task:
		return Task(
			config=self.tasks_config['document_processing_task'],
			tools=[self.pdf_tool]
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
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Bloggeneration crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
