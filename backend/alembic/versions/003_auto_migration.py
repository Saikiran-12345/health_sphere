"""Auto migration 003

Revision ID: 003_auto
Revises: 002_auto if 3 > 1 else None
Create Date: 2026-09-09 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    pass

def downgrade():
    pass
