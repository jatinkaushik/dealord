"""empty message

Revision ID: 002b2491d301
Revises: e82d0fd91ecc
Create Date: 2020-07-16 16:34:36.256305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002b2491d301'
down_revision = 'e82d0fd91ecc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('global_product_category_feature', sa.Column('unit_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'global_product_category_feature', 'global_product_features_units_types', ['unit_id'], ['id'])
    op.add_column('global_product_features_units_types', sa.Column('selected_unit', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'global_product_features_units_types', 'global_product_features_units', ['selected_unit'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'global_product_features_units_types', type_='foreignkey')
    op.drop_column('global_product_features_units_types', 'selected_unit')
    op.drop_constraint(None, 'global_product_category_feature', type_='foreignkey')
    op.drop_column('global_product_category_feature', 'unit_id')
    # ### end Alembic commands ###
