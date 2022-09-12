from pydantic import BaseModel


class Scanner(BaseModel):
    scanner_name: str
    language: str
    source_code_url: str