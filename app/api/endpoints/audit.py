from fastapi import APIRouter, HTTPException

from app.schemas import AuditDTO
from app.services import AuditService

audit_router = APIRouter()


@audit_router.get("/audit", response_model=list[AuditDTO])
async def get_audit_logs(limit: int = 100, offset: int = 0):
    """Get all audit logs from the database"""
    try:
        return await AuditService.get_audit_logs(limit, offset)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
