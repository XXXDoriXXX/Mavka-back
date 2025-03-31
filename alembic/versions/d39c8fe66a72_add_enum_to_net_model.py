"""add enum to net model

Revision ID: d39c8fe66a72
Revises: d5873b09a2bc
Create Date: 2025-03-31 10:40:22.936300

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd39c8fe66a72'
down_revision: Union[str, None] = 'd5873b09a2bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    nettype_enum = sa.Enum('RIBBON', 'BOW', name='nettype')
    netstatus_enum = sa.Enum('PLANNED', 'WORKING', 'CONFIRMATION', 'COMPLETED', 'CANCELED', name='netstatus')
    nettype_enum.create(op.get_bind(), checkfirst=True)
    netstatus_enum.create(op.get_bind(), checkfirst=True)

    op.execute("ALTER TABLE nets ALTER COLUMN type TYPE nettype USING type::nettype")
    op.execute("ALTER TABLE nets ALTER COLUMN status TYPE netstatus USING status::netstatus")


def downgrade() -> None:
    """Downgrade schema."""
    nettype_enum = sa.Enum('RIBBON', 'BOW', name='nettype')
    netstatus_enum = sa.Enum('PLANNED', 'WORKING', 'CONFIRMATION', 'COMPLETED', 'CANCELED', name='netstatus')

    op.execute("ALTER TABLE nets ALTER COLUMN status TYPE VARCHAR USING status::VARCHAR")
    op.execute("ALTER TABLE nets ALTER COLUMN type TYPE VARCHAR USING type::VARCHAR")

    netstatus_enum.drop(op.get_bind(), checkfirst=True)
    nettype_enum.drop(op.get_bind(), checkfirst=True)
