"""addppo

Revision ID: e783623110ff
Revises: 978913760046
Create Date: 2023-10-26 16:48:09.474712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e783623110ff'
down_revision = '978913760046'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('powerdotProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('href', sa.String(), nullable=True))

    with op.batch_alter_table('recoveryairProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('href', sa.String(), nullable=True))

    with op.batch_alter_table('smartgogglesProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('href', sa.String(), nullable=True))

    with op.batch_alter_table('theracupProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('href', sa.String(), nullable=True))

    with op.batch_alter_table('therafaceProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('href', sa.String(), nullable=True))

    with op.batch_alter_table('waveseriesProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('href', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('waveseriesProducts', schema=None) as batch_op:
        batch_op.drop_column('href')

    with op.batch_alter_table('therafaceProducts', schema=None) as batch_op:
        batch_op.drop_column('href')

    with op.batch_alter_table('theracupProducts', schema=None) as batch_op:
        batch_op.drop_column('href')

    with op.batch_alter_table('smartgogglesProducts', schema=None) as batch_op:
        batch_op.drop_column('href')

    with op.batch_alter_table('recoveryairProducts', schema=None) as batch_op:
        batch_op.drop_column('href')

    with op.batch_alter_table('powerdotProducts', schema=None) as batch_op:
        batch_op.drop_column('href')

    # ### end Alembic commands ###