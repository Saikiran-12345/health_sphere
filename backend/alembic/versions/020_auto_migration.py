"""Auto migration 020

Revision ID: 020_auto
Revises: 019_auto if 20 > 1 else None
Create Date: 2026-09-09 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    pass

def downgrade():
    pass
