"""empty message

Revision ID: 5cb826d246ac
Revises: 
Create Date: 2023-11-07 19:34:52.752212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cb826d246ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clinicsupplies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('electrodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('electrotherapy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hot and cold',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lightforceTherapy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mobility',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('portableElectrotherapy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('powerdotProducts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('classification', sa.String(), nullable=True),
    sa.Column('compatible', sa.String(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('classification', sa.String(), nullable=True),
    sa.Column('compatible', sa.String(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recoveryairProducts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('classification', sa.String(), nullable=True),
    sa.Column('compatible', sa.String(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recoverythermProducts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('classification', sa.String(), nullable=True),
    sa.Column('compatible', sa.String(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shockwave & RPW',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('smartgogglesProducts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('classification', sa.String(), nullable=True),
    sa.Column('compatible', sa.String(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tables',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('theracupProducts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('classification', sa.String(), nullable=True),
    sa.Column('compatible', sa.String(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('therafaceProducts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('classification', sa.String(), nullable=True),
    sa.Column('compatible', sa.String(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('theragunProducts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('classification', sa.String(), nullable=True),
    sa.Column('compatible', sa.String(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('_password_hash', sa.String(), nullable=True),
    sa.Column('firstName', sa.String(), nullable=True),
    sa.Column('lastName', sa.String(), nullable=True),
    sa.Column('phoneNumber', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vitalstimTherapy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('waveseriesProducts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('classification', sa.String(), nullable=True),
    sa.Column('compatible', sa.String(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('href', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('waveseriesProducts')
    op.drop_table('vitalstimTherapy')
    op.drop_table('users')
    op.drop_table('theragunProducts')
    op.drop_table('therafaceProducts')
    op.drop_table('theracupProducts')
    op.drop_table('tables')
    op.drop_table('smartgogglesProducts')
    op.drop_table('shockwave & RPW')
    op.drop_table('recoverythermProducts')
    op.drop_table('recoveryairProducts')
    op.drop_table('products')
    op.drop_table('powerdotProducts')
    op.drop_table('portableElectrotherapy')
    op.drop_table('mobility')
    op.drop_table('lightforceTherapy')
    op.drop_table('hot and cold')
    op.drop_table('electrotherapy')
    op.drop_table('electrodes')
    op.drop_table('clinicsupplies')
    # ### end Alembic commands ###
