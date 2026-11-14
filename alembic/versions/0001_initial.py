from alembic import op
import sqlalchemy as sa
revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    op.create_table('categories', sa.Column('id', sa.Integer, primary_key=True), sa.Column('name', sa.String(200), unique=True), sa.Column('description', sa.Text), sa.Column('parent_id', sa.Integer, sa.ForeignKey('categories.id')))
    op.create_table('content', sa.Column('id', sa.Integer, primary_key=True), sa.Column('title', sa.String(300), nullable=False), sa.Column('slug', sa.String(300), unique=True), sa.Column('content_type', sa.String(40)), sa.Column('category_id', sa.Integer, sa.ForeignKey('categories.id')), sa.Column('description', sa.Text), sa.Column('content', sa.Text, nullable=False), sa.Column('language', sa.String(5), nullable=False), sa.Column('status', sa.String(20), nullable=False), sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()), sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now()))
    op.create_table('aliases', sa.Column('id', sa.Integer, primary_key=True), sa.Column('content_id', sa.Integer, sa.ForeignKey('content.id', ondelete='CASCADE'), index=True), sa.Column('alias', sa.String(300), nullable=False), sa.Column('language', sa.String(5), nullable=False), sa.UniqueConstraint('content_id','alias'))
    op.create_table('references', sa.Column('id', sa.Integer, primary_key=True), sa.Column('content_id', sa.Integer, sa.ForeignKey('content.id', ondelete='CASCADE'), index=True), sa.Column('reference_type', sa.String(50), nullable=False), sa.Column('reference_text', sa.String(500), nullable=False), sa.Column('url', sa.String(1000)))
def downgrade():
    op.drop_table('references'); op.drop_table('aliases'); op.drop_table('content'); op.drop_table('categories')
