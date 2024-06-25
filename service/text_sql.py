from pydantic import BaseModel

from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain import SQLDatabase
from langchain_community.llms import OpenAI
from langchain.agents.agent_types import AgentType
from config import DB_URL


class TextSql(BaseModel):

    @property
    def db(self) -> SQLDatabase:
        return SQLDatabase.from_uri(DB_URL)

    @property
    def tool_kit(self) -> SQLDatabaseToolkit:
        return SQLDatabaseToolkit(db=self.db, llm=OpenAI(temperature=0))

    @property
    def sql_agent(self):
        return create_sql_agent(
            llm=OpenAI(temperature=0),
            toolkit=self.tool_kit,
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        )

    def query(self, question):
        response = self.sql_agent.run(question)
        return response