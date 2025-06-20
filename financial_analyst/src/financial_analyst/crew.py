from crewai import Agent, Crew, Process, Task

from crewai.project import CrewBase, agent, crew, task

from crewai.agents.agent_builder.base_agent import BaseAgent

from crewai_tools import SerperDevTool

from typing import List

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class FinancialAnalyst():
    """FinancialAnalyst crew"""

    agents_config = 'agents.yaml'

    tasks_config = 'tasks.yaml'

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    web_search_tool = SerperDevTool()

    @agent
    def financial_researcher(self) -> Agent:
        return Agent(

            config=self.agents_config['financial_researcher'],
            
            verbose=True,

            tools = [web_search_tool]

        )

    @agent
    def financial_analyst(self) -> Agent:
        return Agent(

            config=self.agents_config['financial_analyst'],
              
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def financial_research_task(self) -> Task:

        return Task(

            config=self.tasks_config['financial_research_task'], # type: ignore[index]
        )

    @task
    def financial_analysis_task(self) -> Task:

        return Task(

            config=self.tasks_config['financial_analyst_task'], # type: ignore[index]

        )

    @crew
    def crew(self) -> Crew:
        """Creates the FinancialAnalyst crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(

            agents=self.agents,
                         
            tasks=self.tasks, 
            
            process=Process.sequential,

            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
