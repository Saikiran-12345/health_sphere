"""Auto migration 006

Revision ID: 006_auto
Revises: 005_auto if 6 > 1 else None
Create Date: 2026-09-09 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    pass

def downgrade():
    pass
