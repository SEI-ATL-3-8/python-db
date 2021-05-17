"""add-category_id-to-dinos

Revision ID: 5eaa67b8b5a6
Revises: 9aa9a28f1574
Create Date: 2021-05-17 17:08:14.578647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5eaa67b8b5a6'
down_revision = '9aa9a28f1574'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('dinos', sa.Column('category_id', sa.Integer))


def downgrade():
    op.remove_column('dinos', 'category_id')
