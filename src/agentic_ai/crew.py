from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os
from agentic_ai.tools.custom_tool import (
    CropDiseaseKnowledgeTool,
    WeatherConditionsTool,
    SoilAnalysisTool,
    PestIdentificationTool
)

@CrewBase
class AgenticAi():
    """
    Plantix - AI Farming Assistant
    Created by TejasS1233
    """

    agents: List[BaseAgent]
    tasks: List[Task]

    @property
    def llm(self) -> LLM:
        """Get the configured LLM from environment variables"""
        return LLM(
            model=os.getenv("MODEL", "gemini/gemini-2.5-flash-preview-04-17"),
            api_key=os.getenv("GEMINI_API_KEY") or os.getenv("OPENAI_API_KEY")
        )
    
    @agent
    def crop_disease_diagnostician(self) -> Agent:
        return Agent(
            config=self.agents_config['crop_disease_diagnostician'],
            tools=[
                CropDiseaseKnowledgeTool(),
                WeatherConditionsTool(),
                PestIdentificationTool()
            ],
            llm=self.llm,
            verbose=True
        )

    @agent
    def treatment_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['treatment_specialist'],
            tools=[
                CropDiseaseKnowledgeTool(),
                SoilAnalysisTool()
            ],
            llm=self.llm,
            verbose=True
        )

    @agent
    def prevention_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['prevention_advisor'],
            tools=[
                CropDiseaseKnowledgeTool(),
                SoilAnalysisTool(),
                WeatherConditionsTool()
            ],
            llm=self.llm,
            verbose=True
        )

    @agent
    def farming_consultant(self) -> Agent:
        return Agent(
            config=self.agents_config['farming_consultant'],
            tools=[
                SoilAnalysisTool(),
                WeatherConditionsTool()
            ],
            llm=self.llm,
            verbose=True
        )
    @task
    def disease_diagnosis_task(self) -> Task:
        return Task(
            config=self.tasks_config['disease_diagnosis_task'],
        )

    @task
    def treatment_recommendation_task(self) -> Task:
        return Task(
            config=self.tasks_config['treatment_recommendation_task'],
        )

    @task
    def prevention_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['prevention_strategy_task'],
        )

    @task
    def farming_advice_task(self) -> Task:
        return Task(
            config=self.tasks_config['farming_advice_task'],
            output_file='plantix_farming_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Plantix AI Crew for crop disease diagnosis and farming assistance"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

