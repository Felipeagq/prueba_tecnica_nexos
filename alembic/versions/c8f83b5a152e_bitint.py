"""bitint

Revision ID: c8f83b5a152e
Revises: 
Create Date: 2022-10-13 20:07:26.363724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8f83b5a152e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventory',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('FechaInventario', sa.Text(), nullable=True),
    sa.Column('GLN_Cliente', sa.Integer(), nullable=True),
    sa.Column('GLN_sucursal', sa.Integer(), nullable=True),
    sa.Column('Gtin_Producto', sa.Integer(), nullable=True),
    sa.Column('Inventario_Final', sa.Integer(), nullable=True),
    sa.Column('PrecioUnidad', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inventory_id'), 'inventory', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_inventory_id'), table_name='inventory')
    op.drop_table('inventory')
    # ### end Alembic commands ###