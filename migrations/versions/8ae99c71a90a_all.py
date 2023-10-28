"""all

Revision ID: 8ae99c71a90a
Revises: e5b3a5fbc53a
Create Date: 2023-10-28 00:17:06.508627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ae99c71a90a'
down_revision = 'e5b3a5fbc53a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('portableElectrotherapy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('portableElectrotherapy')
    # ### end Alembic commands ###