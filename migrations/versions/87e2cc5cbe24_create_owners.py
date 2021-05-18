"""create-owners

Revision ID: 87e2cc5cbe24
Revises: 13b59bd5bbd1
Create Date: 2021-05-17 22:27:20.860777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87e2cc5cbe24'
down_revision = '13b59bd5bbd1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'owners',
        sa.Column('id',sa.Integer, primary_key=True),
        sa.Column('name',sa.String),
        sa.Column('age',sa.Integer)
    )


def downgrade():
    pass
