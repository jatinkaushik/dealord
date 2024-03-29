"""empty message

Revision ID: 9cb50b78b17e
Revises: f75f95b0e2b3
Create Date: 2020-08-01 23:55:23.556471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cb50b78b17e'
down_revision = 'f75f95b0e2b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('general_data_units_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('global_product_varient_features', sa.Column('product_varient_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'global_product_varient_features', 'global_product_products_varient', ['product_varient_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'global_product_varient_features', type_='foreignkey')
    op.drop_column('global_product_varient_features', 'product_varient_id')
    op.drop_table('general_data_units_types')
    # ### end Alembic commands ###
