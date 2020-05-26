"""empty message

Revision ID: 7bb68cecd174
Revises: 0dc580d98211
Create Date: 2020-05-25 16:49:19.568498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bb68cecd174'
down_revision = '0dc580d98211'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('features__data_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('features__data_type')
    # ### end Alembic commands ###
