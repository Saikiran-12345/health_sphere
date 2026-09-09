"""Auto migration 004

Revision ID: 004_auto
Revises: 003_auto if 4 > 1 else None
Create Date: 2026-09-09 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    pass

def downgrade():
    pass
