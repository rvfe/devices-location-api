"""tabelas iniciais4

Revision ID: 2f4dc7f6c2a4
Revises: eb512be7f473
Create Date: 2023-02-11 18:13:19.378863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f4dc7f6c2a4'
down_revision = 'eb512be7f473'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('position', sa.Column('device_ref_id', sa.Integer(), nullable=False))
    op.drop_constraint('position_device_id_fkey', 'position', type_='foreignkey')
    op.create_foreign_key(None, 'position', 'device', ['device_ref_id'], ['id'], ondelete='CASCADE')
    op.drop_column('position', 'device_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('position', sa.Column('device_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'position', type_='foreignkey')
    op.create_foreign_key('position_device_id_fkey', 'position', 'device', ['device_id'], ['id'], ondelete='CASCADE')
    op.drop_column('position', 'device_ref_id')
    # ### end Alembic commands ###
