"""add foreign-key to posts table

Revision ID: d0c2d412031f
Revises: baa6edf66f9b
Create Date: 2023-12-25 11:45:14.168518

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0c2d412031f'
down_revision: Union[str, None] = 'baa6edf66f9b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_user_fk',source_table='posts',referent_table='users',
                          local_cols=['owner_id'],remote_cols=['id'],
                          ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint("post_user_fk",table_name='posts')
    op.drop_column("posts",'owner_id')

    pass
