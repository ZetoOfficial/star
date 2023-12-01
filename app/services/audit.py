from app.repositories import CRUDAudit


class AuditService:
    @staticmethod
    async def get_audit_logs(limit: int = None, offset: int = None) -> list:
        return await CRUDAudit.get_audit_logs(limit, offset)
