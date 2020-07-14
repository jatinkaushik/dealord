"""empty message

Revision ID: 1c1220c16b41
Revises: fdd71b797e32
Create Date: 2020-07-01 12:59:18.157529

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1c1220c16b41'
down_revision = 'fdd71b797e32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('global_product_features_units', 'selected_unit')
    op.add_column('global_product_features_units_types', sa.Column('selected_unit', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'global_product_features_units_types', 'global_product_features_units', ['selected_unit'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'global_product_features_units_types', type_='foreignkey')
    op.drop_column('global_product_features_units_types', 'selected_unit')
    op.add_column('global_product_features_units', sa.Column('selected_unit', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    # ### end Alembic commands ###