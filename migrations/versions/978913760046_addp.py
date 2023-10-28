"""addp

Revision ID: 978913760046
Revises: 53b84dc1974c
Create Date: 2023-10-26 16:01:53.966712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '978913760046'
down_revision = '53b84dc1974c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('powerdotProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('brand', sa.String(), nullable=True))

    with op.batch_alter_table('recoveryairProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('brand', sa.String(), nullable=True))

    with op.batch_alter_table('recoverythermProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('href', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('brand', sa.String(), nullable=True))

    with op.batch_alter_table('smartgogglesProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description_url', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('brand', sa.String(), nullable=True))

    with op.batch_alter_table('theracupProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('brand', sa.String(), nullable=True))

    with op.batch_alter_table('therafaceProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('brand', sa.String(), nullable=True))

    with op.batch_alter_table('theragunProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('brand', sa.String(), nullable=True))

    with op.batch_alter_table('waveseriesProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('brand', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('waveseriesProducts', schema=None) as batch_op:
        batch_op.drop_column('brand')

    with op.batch_alter_table('theragunProducts', schema=None) as batch_op:
        batch_op.drop_column('brand')

    with op.batch_alter_table('therafaceProducts', schema=None) as batch_op:
        batch_op.drop_column('brand')

    with op.batch_alter_table('theracupProducts', schema=None) as batch_op:
        batch_op.drop_column('brand')

    with op.batch_alter_table('smartgogglesProducts', schema=None) as batch_op:
        batch_op.drop_column('brand')
        batch_op.drop_column('description_url')

    with op.batch_alter_table('recoverythermProducts', schema=None) as batch_op:
        batch_op.drop_column('brand')
        batch_op.drop_column('href')

    with op.batch_alter_table('recoveryairProducts', schema=None) as batch_op:
        batch_op.drop_column('brand')

    with op.batch_alter_table('powerdotProducts', schema=None) as batch_op:
        batch_op.drop_column('brand')

    # ### end Alembic commands ###