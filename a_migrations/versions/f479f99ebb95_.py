"""empty message

Revision ID: f479f99ebb95
Revises: 53c79c9792b0
Create Date: 2020-06-16 19:24:47.628201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f479f99ebb95'
down_revision = '53c79c9792b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('global_product_category_feature_ibfk_4', 'global_product_category_feature', type_='foreignkey')
    op.create_foreign_key(None, 'global_product_category_feature', 'global_product_features_units_types', ['unit_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'global_product_category_feature', type_='foreignkey')
    op.create_foreign_key('global_product_category_feature_ibfk_4', 'global_product_category_feature', 'global_product_features_units', ['unit_id'], ['id'])
    # ### end Alembic commands ###
