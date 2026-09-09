"""Auto migration 001

Revision ID: 001_auto
Revises: 000_auto if 1 > 1 else None
Create Date: 2026-09-09 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    pass

def downgrade():
    pass
