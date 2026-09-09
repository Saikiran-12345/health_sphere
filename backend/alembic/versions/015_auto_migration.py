"""Auto migration 015

Revision ID: 015_auto
Revises: 014_auto if 15 > 1 else None
Create Date: 2026-09-09 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    pass

def downgrade():
    pass
