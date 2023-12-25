"""add context column to posts table
Revision ID: da708be263ae
Revises: 98095e4c708b
Create Date: 2023-12-20 12:48:17.394777
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'da708be263ae'
down_revision: Union[str, None] = '98095e4c708b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts",sa.Column("content",sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column("posts",'content')
    pass
