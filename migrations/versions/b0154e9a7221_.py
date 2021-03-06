"""empty message

Revision ID: b0154e9a7221
Revises: 1477509bfc76
Create Date: 2021-05-23 20:34:39.274886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0154e9a7221'
down_revision = '1477509bfc76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile__student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.String(length=7), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('telp', sa.String(length=15), nullable=False),
    sa.Column('student_class', sa.String(length=7), nullable=True),
    sa.ForeignKeyConstraint(['student_class'], ['class.class_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['user.user_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('telp'),
    sa.UniqueConstraint('telp')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile__student')
    # ### end Alembic commands ###
