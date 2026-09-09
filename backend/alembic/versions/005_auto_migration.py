"""Auto migration 005

Revision ID: 005_auto
Revises: 004_auto if 5 > 1 else None
Create Date: 2026-09-09 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    pass

def downgrade():
    pass
