"""empty message

Revision ID: 5ae41e98f5c4
Revises: 9fcfb7748037
Create Date: 2020-09-21 02:09:25.386208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ae41e98f5c4'
down_revision = '9fcfb7748037'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers_customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company_company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vendors_vendor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company_company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customers_address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('address_line_1', sa.String(length=100), nullable=True),
    sa.Column('address_line_2', sa.String(length=100), nullable=True),
    sa.Column('district', sa.String(length=30), nullable=True),
    sa.Column('city_town', sa.String(length=30), nullable=True),
    sa.Column('landmark', sa.String(length=50), nullable=True),
    sa.Column('state', sa.String(length=30), nullable=True),
    sa.Column('country', sa.String(length=30), nullable=True),
    sa.Column('pin_code', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers_customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customers_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('legal_name', sa.String(length=100), nullable=True),
    sa.Column('gstin_no', sa.String(length=100), nullable=True),
    sa.Column('cin_no', sa.String(length=100), nullable=True),
    sa.Column('website', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('phone_no', sa.String(length=20), nullable=True),
    sa.Column('fax', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers_customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vendors_address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vendor_id', sa.Integer(), nullable=True),
    sa.Column('address_line_1', sa.String(length=100), nullable=True),
    sa.Column('address_line_2', sa.String(length=100), nullable=True),
    sa.Column('district', sa.String(length=30), nullable=True),
    sa.Column('city_town', sa.String(length=30), nullable=True),
    sa.Column('landmark', sa.String(length=50), nullable=True),
    sa.Column('state', sa.String(length=30), nullable=True),
    sa.Column('country', sa.String(length=30), nullable=True),
    sa.Column('pin_code', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['vendor_id'], ['vendors_vendor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vendors_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vendor_id', sa.Integer(), nullable=True),
    sa.Column('legal_name', sa.String(length=100), nullable=True),
    sa.Column('gstin_no', sa.String(length=100), nullable=True),
    sa.Column('cin_no', sa.String(length=100), nullable=True),
    sa.Column('website', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('phone_no', sa.String(length=20), nullable=True),
    sa.Column('fax', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['vendor_id'], ['vendors_vendor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vendors_info')
    op.drop_table('vendors_address')
    op.drop_table('customers_info')
    op.drop_table('customers_address')
    op.drop_table('vendors_vendor')
    op.drop_table('customers_customer')
    # ### end Alembic commands ###