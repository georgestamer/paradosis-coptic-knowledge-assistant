from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String, Text, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base
class Category(Base):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), unique=True)
    description: Mapped[str | None] = mapped_column(Text)
    parent_id: Mapped[int | None] = mapped_column(ForeignKey('categories.id'))
class Content(Base):
    __tablename__ = 'content'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(300), index=True)
    slug: Mapped[str] = mapped_column(String(300), unique=True)
    content_type: Mapped[str] = mapped_column(String(40))
    category_id: Mapped[int | None] = mapped_column(ForeignKey('categories.id'))
    description: Mapped[str | None] = mapped_column(Text)
    content: Mapped[str] = mapped_column(Text)
    language: Mapped[str] = mapped_column(String(5), default='ar')
    status: Mapped[str] = mapped_column(String(20), default='draft', index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    aliases: Mapped[list['Alias']] = relationship(cascade='all, delete-orphan')
    references: Mapped[list['Reference']] = relationship(cascade='all, delete-orphan')
class Alias(Base):
    __tablename__ = 'aliases'
    id: Mapped[int] = mapped_column(primary_key=True)
    content_id: Mapped[int] = mapped_column(ForeignKey('content.id', ondelete='CASCADE'), index=True)
    alias: Mapped[str] = mapped_column(String(300), index=True)
    language: Mapped[str] = mapped_column(String(5), default='ar')
    __table_args__ = (UniqueConstraint('content_id', 'alias', name='uq_content_alias'),)
class Reference(Base):
    __tablename__ = 'references'
    id: Mapped[int] = mapped_column(primary_key=True)
    content_id: Mapped[int] = mapped_column(ForeignKey('content.id', ondelete='CASCADE'), index=True)
    reference_type: Mapped[str] = mapped_column(String(50))
    reference_text: Mapped[str] = mapped_column(String(500))
    url: Mapped[str | None] = mapped_column(String(1000))
