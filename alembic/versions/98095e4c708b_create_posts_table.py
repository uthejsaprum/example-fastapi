"""create posts table

Revision ID: 98095e4c708b
Revises: 
Create Date: 2023-12-20 10:35:03.990441

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98095e4c708b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table("posts",sa.Column('id',sa.Integer(),primary_key=True,nullable=False),
                    sa.Column('title',sa.String(),nullable=False)) 
    pass


def downgrade():
    op.drop_table("posts")
    pass
