from fastapi import FastAPI
from src.models import start_analysis, read_report
from src.schemas import Scanner

app = FastAPI()


@app.post('/scan')
async def scanRepo(scanner: Scanner):
    timestamp = start_analysis(scanner.source_code_url, scanner.scanner_name,
                               scanner.language)
    ret = {"report_id": timestamp, "message": "success"}
    return ret


@app.get('/scan/reports/{report_id}')
async def getReport(report_id: int):
    data = read_report(report_id)
    return data