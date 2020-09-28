"""empty message

Revision ID: 7548e50e48bc
Revises: c40d1d567e50
Create Date: 2020-09-29 02:08:31.617906

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7548e50e48bc'
down_revision = 'c40d1d567e50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company_address', sa.Column('address_line', sa.String(length=100), nullable=True))
    op.drop_column('company_address', 'address_line_1')
    op.drop_column('company_address', 'address_line_2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company_address', sa.Column('address_line_2', mysql.VARCHAR(length=100), nullable=True))
    op.add_column('company_address', sa.Column('address_line_1', mysql.VARCHAR(length=100), nullable=True))
    op.drop_column('company_address', 'address_line')
    # ### end Alembic commands ###