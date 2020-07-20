"""empty message

Revision ID: e82d0fd91ecc
Revises: e926d1032f55
Create Date: 2020-07-16 16:33:20.504896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e82d0fd91ecc'
down_revision = 'e926d1032f55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('global_product_features_units',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('units_type_id', sa.Integer(), nullable=True),
    sa.Column('exp', sa.String(length=5), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['units_type_id'], ['global_product_features_units_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('global_product_products_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_path', sa.String(length=200), nullable=True),
    sa.Column('product_varient_id', sa.Integer(), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_varient_id'], ['global_product_products_varient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('global_product_products_image')
    op.drop_table('global_product_features_units')
    # ### end Alembic commands ###