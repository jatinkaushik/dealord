"""empty message

Revision ID: f7696a012821
Revises: 800588b24ccb
Create Date: 2020-07-16 16:26:12.687950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7696a012821'
down_revision = '800588b24ccb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('global_product_features_boolean',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.Boolean(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_varient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['global_product_category_feature.id'], ),
    sa.ForeignKeyConstraint(['product_varient_id'], ['global_product_products_varient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('global_product_features_date',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.DateTime(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_varient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['global_product_category_feature.id'], ),
    sa.ForeignKeyConstraint(['product_varient_id'], ['global_product_products_varient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('global_product_features_double',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.Float(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_varient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['global_product_category_feature.id'], ),
    sa.ForeignKeyConstraint(['product_varient_id'], ['global_product_products_varient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('global_product_features_integer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.Integer(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_varient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['global_product_category_feature.id'], ),
    sa.ForeignKeyConstraint(['product_varient_id'], ['global_product_products_varient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('global_product_features_string',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.String(length=1000), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_varient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['global_product_category_feature.id'], ),
    sa.ForeignKeyConstraint(['product_varient_id'], ['global_product_products_varient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('global_product_features_string')
    op.drop_table('global_product_features_integer')
    op.drop_table('global_product_features_double')
    op.drop_table('global_product_features_date')
    op.drop_table('global_product_features_boolean')
    # ### end Alembic commands ###
