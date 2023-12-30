"""empty message

Revision ID: 2b269549ba82
Revises: 57afd5871c1e
Create Date: 2020-06-06 19:06:19.747940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b269549ba82'
down_revision = '57afd5871c1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shift_time',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shift_name', sa.String(length=30), nullable=True),
    sa.Column('shift_time_start', sa.DateTime(), nullable=True),
    sa.Column('shift_time_end', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('address_line1', sa.String(length=50), nullable=True),
    sa.Column('address_line2', sa.String(length=50), nullable=True),
    sa.Column('city', sa.String(length=30), nullable=True),
    sa.Column('state', sa.String(length=30), nullable=True),
    sa.Column('country', sa.String(length=30), nullable=True),
    sa.Column('pin_code', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.employee_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('department_name', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.employee_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('designation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('designation_name', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.employee_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee_personal_detail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('alternate_phone_no', sa.String(length=15), nullable=True),
    sa.Column('father_name', sa.String(length=30), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(), nullable=True),
    sa.Column('pan_number', sa.String(length=20), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.employee_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee_personal_detail')
    op.drop_table('designation')
    op.drop_table('department')
    op.drop_table('address')
    op.drop_table('shift_time')
    # ### end Alembic commands ###