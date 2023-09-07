from pydantic import BaseModel

class New(BaseModel):
    generated: str
    scheme: str
    src: str
    name: str