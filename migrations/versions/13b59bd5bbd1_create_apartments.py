"""create-apartments

Revision ID: 13b59bd5bbd1
Revises: 
Create Date: 2021-05-17 22:27:12.048808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13b59bd5bbd1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'apartments',
        sa.Column('id',sa.Integer, primary_key=True),
        sa.Column('name',sa.String),
        sa.Column('units',sa.Integer),
        sa.Column('owner_id',sa.Integer)
    )


def downgrade():
    op.drop_table('apartments')
