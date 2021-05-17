"""create-categories

Revision ID: 9aa9a28f1574
Revises: 25d36e2e099a
Create Date: 2021-05-17 17:05:35.326765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9aa9a28f1574'
down_revision = '25d36e2e099a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String)
    )


def downgrade():
    op.drop_table('categories')
