from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from app.models.content import Content
from app.utils.arabic import normalize_arabic
def find_content(db: Session, query: str) -> Content | None:
    needle = normalize_arabic(query)
    rows = db.scalars(select(Content).options(selectinload(Content.aliases), selectinload(Content.references)).where(Content.status == 'approved')).all()
    exact = [c for c in rows for a in c.aliases if normalize_arabic(a.alias) == needle]
    if len({c.id for c in exact}) == 1: return exact[0]
    titles = [c for c in rows if normalize_arabic(c.title) == needle]
    if len(titles) == 1: return titles[0]
    partial = {c.id: c for c in rows if any(needle in normalize_arabic(a.alias) or normalize_arabic(a.alias) in needle for a in c.aliases) or needle in normalize_arabic(c.title) or normalize_arabic(c.title) in needle}
    return next(iter(partial.values())) if len(partial) == 1 else None
