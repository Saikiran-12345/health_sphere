"""Auto migration 002

Revision ID: 002_auto
Revises: 001_auto if 2 > 1 else None
Create Date: 2026-09-09 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    pass

def downgrade():
    pass
