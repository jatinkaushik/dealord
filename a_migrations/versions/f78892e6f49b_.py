"""empty message

Revision ID: f78892e6f49b
Revises: ac82e619089c
Create Date: 2020-06-16 13:12:33.838900

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f78892e6f49b'
down_revision = 'ac82e619089c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('global_product_features_recommended',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_feature_global_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('string_seleted_id', sa.Integer(), nullable=True),
    sa.Column('integer_seleted_id', sa.Integer(), nullable=True),
    sa.Column('double_seleted_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_feature_global_id'], ['global_product_category_feature.id'], ),
    sa.ForeignKeyConstraint(['double_seleted_id'], ['global_product_features_double_recommended.id'], ),
    sa.ForeignKeyConstraint(['integer_seleted_id'], ['global_product_features_integer_recommended.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['global_product_products.id'], ),
    sa.ForeignKeyConstraint(['string_seleted_id'], ['global_product_features_string_recommended.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('global_features_recommended')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('global_features_recommended',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('category_feature_global_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('product_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('string_seleted_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('integer_seleted_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('double_seleted_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['category_feature_global_id'], ['global_product_category_feature.id'], name='global_features_recommended_ibfk_1'),
    sa.ForeignKeyConstraint(['double_seleted_id'], ['global_product_features_double_recommended.id'], name='global_features_recommended_ibfk_2'),
    sa.ForeignKeyConstraint(['integer_seleted_id'], ['global_product_features_integer_recommended.id'], name='global_features_recommended_ibfk_3'),
    sa.ForeignKeyConstraint(['product_id'], ['global_product_products.id'], name='global_features_recommended_ibfk_4'),
    sa.ForeignKeyConstraint(['string_seleted_id'], ['global_product_features_string_recommended.id'], name='global_features_recommended_ibfk_5'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('global_product_features_recommended')
    # ### end Alembic commands ###
