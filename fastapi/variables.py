from pydantic import BaseModel
#class thst explains variables
class Clickad(BaseModel):
    Daily_Time_Spent_on_Site:float
    Age:int
    Area_Income:float
    Daily_Internet_Usage:float
    Male:int