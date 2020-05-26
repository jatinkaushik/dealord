"""empty message

Revision ID: 6562a4601a2b
Revises: 
Create Date: 2020-05-24 16:36:17.057464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6562a4601a2b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('password', sa.String(length=1000), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('parent', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tokens', sa.String(length=1000), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sub__category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('sub_category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sub_category_id'], ['sub__category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sub__category__feature',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('sub_category_id', sa.Integer(), nullable=True),
    sa.Column('feature_type', sa.Integer(), nullable=True),
    sa.Column('units', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sub_category_id'], ['sub__category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('boolean__features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.Boolean(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['sub__category__feature.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('date__features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.DateTime(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['sub__category__feature.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('double__features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.Float(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['sub__category__feature.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('extra__features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('units', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('integer__features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.Integer(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['sub__category__feature.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('string__features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.String(length=1000), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['sub__category__feature.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('varient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('varient')
    op.drop_table('string__features')
    op.drop_table('integer__features')
    op.drop_table('extra__features')
    op.drop_table('double__features')
    op.drop_table('date__features')
    op.drop_table('boolean__features')
    op.drop_table('sub__category__feature')
    op.drop_table('products')
    op.drop_table('sub__category')
    op.drop_table('token')
    op.drop_table('category')
    op.drop_table('user')
    # ### end Alembic commands ###
