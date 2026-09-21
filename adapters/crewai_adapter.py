from adapters.base import AdapterContract
from agent import SQLMedic

class CrewAIAdapter(AdapterContract):
    framework="crewai"
    def run(self,path):
        return SQLMedic().inspect(path).to_dict()
    def verify(self,path):
        result=self.run(path)
        return {"framework":self.framework,"mode":"portable","verified":super().verify(path),"result":result}
