from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import SessionLocal
from app.models import Audit


class CRUDAudit:
    @staticmethod
    async def get_audit_logs(limit: int = None, offset: int = None) -> list:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(Audit)
            if limit:
                query = query.limit(limit)
            if offset:
                query = query.offset(offset)
            result = await session.execute(query)
            audits = result.scalars().all()
            return audits
