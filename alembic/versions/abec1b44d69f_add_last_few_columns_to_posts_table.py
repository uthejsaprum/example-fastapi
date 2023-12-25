"""add last few columns to posts table

Revision ID: abec1b44d69f
Revises: d0c2d412031f
Create Date: 2023-12-25 12:26:14.105624

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'abec1b44d69f'
down_revision: Union[str, None] = 'd0c2d412031f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts",sa.Column("published",sa.Boolean,
                                    nullable=False,server_default='TRUE'))
    op.add_column("posts",sa.Column("created_at",sa.TIMESTAMP(timezone=True),
                                    nullable=False,server_default=sa.text('now()')))
    pass


def downgrade():
    op.drop_column("posts",'published')
    op.drop_column("posts",'created_at')
    pass
