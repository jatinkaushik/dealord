"""empty message

Revision ID: 78ba2cd193e0
Revises: 8f16d919c1e9
Create Date: 2020-07-16 16:18:41.998868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78ba2cd193e0'
down_revision = '8f16d919c1e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('global_product_category_feature',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('features_datatype_id', sa.Integer(), nullable=True),
    sa.Column('recommendation', sa.Boolean(), nullable=True),
    sa.Column('feature_required', sa.Boolean(), nullable=True),
    sa.Column('filterable', sa.Boolean(), nullable=True),
    sa.Column('features_groups_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['global_product_category.id'], ),
    sa.ForeignKeyConstraint(['features_datatype_id'], ['global_product_features_datatype.id'], ),
    sa.ForeignKeyConstraint(['features_groups_id'], ['global_product_features_groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('global_product_category_feature')
    # ### end Alembic commands ###
