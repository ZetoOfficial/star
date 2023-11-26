"""jajaj

Revision ID: 7b3196d8fc41
Revises: 295783a6c87c
Create Date: 2023-11-26 20:53:37.975361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b3196d8fc41'
down_revision = '295783a6c87c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('star_constellation_star_id_fkey', 'star_constellation', type_='foreignkey')
    op.drop_constraint('star_constellation_constellation_id_fkey', 'star_constellation', type_='foreignkey')
    op.create_foreign_key(None, 'star_constellation', 'star', ['star_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'star_constellation', 'constellation', ['constellation_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'star_constellation', type_='foreignkey')
    op.drop_constraint(None, 'star_constellation', type_='foreignkey')
    op.create_foreign_key('star_constellation_constellation_id_fkey', 'star_constellation', 'constellation', ['constellation_id'], ['id'])
    op.create_foreign_key('star_constellation_star_id_fkey', 'star_constellation', 'star', ['star_id'], ['id'])
    # ### end Alembic commands ###
