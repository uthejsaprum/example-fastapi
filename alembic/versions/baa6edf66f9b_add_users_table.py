"""add users table

Revision ID: baa6edf66f9b
Revises: da708be263ae
Create Date: 2023-12-21 14:56:40.315504

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'baa6edf66f9b'
down_revision: Union[str, None] = 'da708be263ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table("users",sa.Column("id",sa.Integer(),nullable=False)
                    ,sa.Column("email",sa.String(),nullable=False),
                    sa.Column("password",sa.String(),nullable=False),
                    sa.Column("created_at",sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'),nullable=False),
                              sa.PrimaryKeyConstraint('id'),
                              sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table("users")
    pass
