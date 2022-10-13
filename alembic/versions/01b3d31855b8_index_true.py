"""index true

Revision ID: 01b3d31855b8
Revises: 26c6eec616e0
Create Date: 2022-10-13 00:00:07.816339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01b3d31855b8'
down_revision = '26c6eec616e0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_inventory_id'), 'inventory', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_inventory_id'), table_name='inventory')
    # ### end Alembic commands ###
