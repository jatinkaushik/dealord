"""empty message

Revision ID: 8bc6d8b6ee45
Revises: 
Create Date: 2020-06-13 14:21:32.011177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bc6d8b6ee45'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('primary_phone_no', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('employee_id')
    )
    op.create_table('features__datatype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('features__datatype__global',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shift_time',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shift_name', sa.String(length=30), nullable=True),
    sa.Column('shift_time_start', sa.DateTime(), nullable=True),
    sa.Column('shift_time_end', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
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
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id1', sa.Integer(), nullable=True),
    sa.Column('address_line1', sa.String(length=50), nullable=True),
    sa.Column('address_line2', sa.String(length=50), nullable=True),
    sa.Column('city', sa.String(length=30), nullable=True),
    sa.Column('state', sa.String(length=30), nullable=True),
    sa.Column('country', sa.String(length=30), nullable=True),
    sa.Column('pin_code', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id1'], ['employee.employee_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('parent', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category__global',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('parent', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id1', sa.Integer(), nullable=True),
    sa.Column('department_name', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['employee_id1'], ['employee.employee_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('designation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id1', sa.Integer(), nullable=True),
    sa.Column('designation_name', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['employee_id1'], ['employee.employee_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee_personal_detail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id1', sa.Integer(), nullable=True),
    sa.Column('alternate_phone_no', sa.String(length=15), nullable=True),
    sa.Column('father_name', sa.String(length=30), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(), nullable=True),
    sa.Column('pan_number', sa.String(length=20), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['employee_id1'], ['employee.employee_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tokens', sa.String(length=1000), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category__feature',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('features_datatype_id', sa.Integer(), nullable=True),
    sa.Column('unit', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['features_datatype_id'], ['features__datatype.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('features__groups__global',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('sub_category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sub_category_id'], ['category__global.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products__global',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category__global.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('boolean__features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.Boolean(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['category__feature.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category__feature__global',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('features_datatype_id', sa.Integer(), nullable=True),
    sa.Column('unit', sa.Integer(), nullable=True),
    sa.Column('features_groups_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category__global.id'], ),
    sa.ForeignKeyConstraint(['features_datatype_id'], ['features__datatype__global.id'], ),
    sa.ForeignKeyConstraint(['features_groups_id'], ['features__groups__global.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('date__features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.DateTime(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['category__feature.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('double__features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.Float(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['category__feature.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('extra__features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('feature_type_id', sa.Integer(), nullable=True),
    sa.Column('units', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('extra__features__global',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('feature_type_id', sa.Integer(), nullable=True),
    sa.Column('units', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products__global.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('integer__features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.Integer(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['category__feature.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('string__features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.String(length=1000), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['category__feature.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('varient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_feature_id'], ['category__feature.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('boolean__features__global',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.Boolean(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['category__feature__global.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products__global.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('date__features__global',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.DateTime(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['category__feature__global.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products__global.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('double__features__global',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.Float(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['category__feature__global.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products__global.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('integer__features__global',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.Integer(), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['category__feature__global.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products__global.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('string__features__global',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_value', sa.String(length=1000), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['category__feature__global.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products__global.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('varient__global',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_feature_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_feature_id'], ['category__feature__global.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products__global.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('varient__global')
    op.drop_table('string__features__global')
    op.drop_table('integer__features__global')
    op.drop_table('double__features__global')
    op.drop_table('date__features__global')
    op.drop_table('boolean__features__global')
    op.drop_table('varient')
    op.drop_table('string__features')
    op.drop_table('integer__features')
    op.drop_table('extra__features__global')
    op.drop_table('extra__features')
    op.drop_table('double__features')
    op.drop_table('date__features')
    op.drop_table('category__feature__global')
    op.drop_table('boolean__features')
    op.drop_table('products__global')
    op.drop_table('products')
    op.drop_table('features__groups__global')
    op.drop_table('category__feature')
    op.drop_table('token')
    op.drop_table('employee_personal_detail')
    op.drop_table('designation')
    op.drop_table('department')
    op.drop_table('category__global')
    op.drop_table('category')
    op.drop_table('address')
    op.drop_table('user')
    op.drop_table('shift_time')
    op.drop_table('features__datatype__global')
    op.drop_table('features__datatype')
    op.drop_table('employee')
    # ### end Alembic commands ###