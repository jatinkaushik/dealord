"""empty message

Revision ID: cfb890094ea4
Revises: 4f10b8b1f585
Create Date: 2020-06-20 10:20:04.551354

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cfb890094ea4'
down_revision = '4f10b8b1f585'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('global_product_features_units', sa.Column('units_type_id', sa.Integer(), nullable=True))
    op.drop_constraint('global_product_features_units_ibfk_1', 'global_product_features_units', type_='foreignkey')
    op.create_foreign_key(None, 'global_product_features_units', 'global_product_features_units_types', ['units_type_id'], ['id'])
    op.drop_column('global_product_features_units', 'units_types_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('global_product_features_units', sa.Column('units_types_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'global_product_features_units', type_='foreignkey')
    op.create_foreign_key('global_product_features_units_ibfk_1', 'global_product_features_units', 'global_product_features_units_types', ['units_types_id'], ['id'])
    op.drop_column('global_product_features_units', 'units_type_id')
    # ### end Alembic commands ###
