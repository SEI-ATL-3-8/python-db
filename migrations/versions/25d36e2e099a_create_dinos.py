"""create-dinos

Revision ID: 25d36e2e099a
Revises: 
Create Date: 2021-05-17 15:31:57.415011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25d36e2e099a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'dinos',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False, unique=True),
        sa.Column('type', sa.String)
    )


def downgrade():
    op.drop_table('dinos')
