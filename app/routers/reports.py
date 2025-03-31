from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import datetime

from app.db.session import get_db
from app.dependencies import require_role
from app.models.report import Report
from app.schemas.report import ReportCreate, ReportRead

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/", response_model=List[ReportRead])
def list_reports(db: Session = Depends(get_db)):
    return db.query(Report).order_by(Report.created_at.desc()).all()


@router.post("/", response_model=ReportRead, status_code=status.HTTP_201_CREATED)
def create_report(data: ReportCreate, db: Session = Depends(get_db), current_user: dict = Depends(require_role("student"))):
    report = Report(
        student_id=current_user["id"],
        **data.dict(),
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    return report


@router.post("/{report_id}/verify", response_model=ReportRead)
def verify_report(report_id: int, db: Session = Depends(get_db), current_user: dict = Depends(require_role("teacher"))):
    report = db.query(Report).get(report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    report.verified_by = current_user["id"]
    report.verified_at = datetime.datetime.utcnow()

    db.commit()
    db.refresh(report)
    return report
