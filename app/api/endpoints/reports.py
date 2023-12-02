from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.schemas import ReportDTO, GalaxyReportDTO
from app.services import ReportsService

report_router = APIRouter()


@report_router.get("/reports/data", response_model=GalaxyReportDTO)
async def get_report_data(galaxy_id: UUID):
    """Get report data"""
    try:
        return await ReportsService.get_report_data(galaxy_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@report_router.get("/reports/excel", response_model=ReportDTO)
async def create_excel_report(galaxy_id: UUID):
    """Create a new Excel report"""
    try:
        return await ReportsService.get_excel_data(galaxy_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@report_router.get("/reports/word", response_model=ReportDTO)
async def create_word_report(galaxy_id: UUID):
    """Create a new Word report"""
    try:
        return await ReportsService.get_word_data(galaxy_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
