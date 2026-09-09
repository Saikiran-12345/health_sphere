"""Auto migration 008

Revision ID: 008_auto
Revises: 007_auto if 8 > 1 else None
Create Date: 2026-09-09 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    pass

def downgrade():
    pass
