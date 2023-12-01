from fastapi import APIRouter, HTTPException
from app.schemas import ReportDTO
from uuid import UUID
from app.services import ReportsService

report_router = APIRouter()


@report_router.get("/reports/excel", response_model=ReportDTO)
async def create_excel_report(universe_id: UUID):
    """Create a new Excel report"""
    try:
        return await ReportsService.get_excel_data(universe_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@report_router.get("/reports/word", response_model=ReportDTO)
async def create_word_report(universe_id: UUID):
    """Create a new Word report"""
    try:
        return await ReportsService.get_word_data(universe_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
