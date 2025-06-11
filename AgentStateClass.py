from typing import TypedDict,Annotated,Sequence
from langchain_core.messages import BaseMessage
import operator

# this class send the output message of each node to next node (i.e. base messsage) in langgraph
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    validation_result: str