"""create many tables

Revision ID: 2c2523c51890
Revises: 6c0d7fb2a6a8
Create Date: 2025-03-31 11:34:47.165587

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c2523c51890'
down_revision: Union[str, None] = '6c0d7fb2a6a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    orderstatus_enum = sa.Enum('PENDING', 'CONFIRMATION', 'COMPLETED', 'CANCELED', name='orderstatus')
    orderstatus_enum.create(op.get_bind(), checkfirst=True)

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedule_templates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('start_time', sa.Time(), nullable=False),
    sa.Column('end_time', sa.Time(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('schedule_weeks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('specialty_id', sa.Integer(), nullable=False),
    sa.Column('notes', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['specialty_id'], ['specialities.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('start_date')
    )
    op.create_table('schedules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('template_id', sa.Integer(), nullable=False),
    sa.Column('week_id', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('is_cleaning', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['teacher_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['template_id'], ['schedule_templates.id'], ),
    sa.ForeignKeyConstraint(['week_id'], ['schedule_weeks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('attendances',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('schedule_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('PRESENT', 'ABSENT', 'EXCUSED', name='attendancestatus'), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['schedule_id'], ['schedules.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('schedule_group',
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('schedule_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['schedule_id'], ['schedules.id'], ),
    sa.PrimaryKeyConstraint('group_id', 'schedule_id')
    )
    op.add_column('orders', sa.Column('status', orderstatus_enum, nullable=False))
    op.add_column('orders', sa.Column('deadline', sa.TIMESTAMP(), nullable=True))
    op.add_column('orders', sa.Column('started_at', sa.TIMESTAMP(), nullable=True))
    op.add_column('orders', sa.Column('completed_at', sa.TIMESTAMP(), nullable=True))
    op.add_column('orders', sa.Column('created_at', sa.TIMESTAMP(), nullable=False))
    op.drop_constraint('orders_name_key', 'orders', type_='unique')
    op.drop_column('orders', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_unique_constraint('orders_name_key', 'orders', ['name'])
    op.drop_column('orders', 'created_at')
    op.drop_column('orders', 'completed_at')
    op.drop_column('orders', 'started_at')
    op.drop_column('orders', 'deadline')
    op.drop_column('orders', 'status')
    op.drop_table('schedule_group')
    op.drop_table('attendances')
    op.drop_table('schedules')
    op.drop_table('schedule_weeks')
    op.drop_table('schedule_templates')
    # ### end Alembic commands ###

    op.execute('DROP TYPE orderstatus')
