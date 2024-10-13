"""Adicionando campos rua, bairro e numero_casa à tabela usuario

Revision ID: c4ded6524a45
Revises: 794f15d7abc4
Create Date: 2024-10-10 11:42:15.445453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4ded6524a45'
down_revision = '794f15d7abc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rua', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('bairro', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('numero_casa', sa.String(length=10), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_column('numero_casa')
        batch_op.drop_column('bairro')
        batch_op.drop_column('rua')

    # ### end Alembic commands ###
