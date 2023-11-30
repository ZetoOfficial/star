from datetime import datetime
from uuid import UUID

import pandas as pd
from docx import Document

from app.repositories import ReportRepository
from app.schemas import ReportDTO
from settings import load_settings

settings_ = load_settings()


def get_public_url(file_path: str) -> str:
    file_path = file_path.lstrip("/")
    return f"/{file_path}"


def to_dict(obj):
    if hasattr(obj, "__dict__"):
        return vars(obj)
    else:
        return {
            attr: getattr(obj, attr) for attr in dir(obj) if not attr.startswith("_")
        }


class ReportsService:
    @staticmethod
    async def get_excel_data(universe_id: UUID):
        report_data = await ReportRepository.get_report_data(universe_id)

        universe_data = pd.DataFrame([to_dict(report_data["universe"])])
        galaxies_data = pd.DataFrame(
            [to_dict(galaxy) for galaxy in report_data["galaxies"]]
        )
        stars_data = pd.DataFrame([to_dict(star) for star in report_data["stars"]])

        universe_name = report_data["universe"].name
        report_name = f"{settings_.app.static_dir}/report_{universe_name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
        with pd.ExcelWriter(report_name) as writer:
            universe_data.to_excel(writer, sheet_name="Universe", index=False)
            galaxies_data.to_excel(writer, sheet_name="Galaxies", index=False)
            stars_data.to_excel(writer, sheet_name="Stars", index=False)

        return ReportDTO(name=report_name, link=get_public_url(report_name))

    @staticmethod
    async def get_word_data(universe_id: UUID):
        report_data = await ReportRepository.get_report_data(universe_id)

        document = Document()
        document.add_heading("Universe Report", 0)

        universe = report_data["universe"]
        document.add_heading("Universe", level=1)
        for attr, value in to_dict(universe).items():
            document.add_paragraph(f"{attr}: {value}")

        document.add_heading("Galaxies", level=1)
        for galaxy in report_data["galaxies"]:
            for attr, value in to_dict(galaxy).items():
                document.add_paragraph(f"{attr}: {value}")
            document.add_paragraph()

        document.add_heading("Stars", level=1)
        for star in report_data["stars"]:
            for attr, value in to_dict(star).items():
                document.add_paragraph(f"{attr}: {value}")
            document.add_paragraph()

        report_name = (
            f"report_{universe_id}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.docx"
        )
        document.save(report_name)
        return ReportDTO(name=report_name, link=get_public_url(report_name))
