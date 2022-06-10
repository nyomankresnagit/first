"""Initial migration.

Revision ID: 4b6ac959cd49
Revises: 
Create Date: 2022-06-08 15:56:08.039653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b6ac959cd49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('no_buku', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nama_buku', sa.String(length=80), nullable=False),
    sa.Column('penulis_buku', sa.String(length=80), nullable=False),
    sa.Column('status_peminjaman', sa.String(length=2), nullable=False),
    sa.Column('flag', sa.String(length=2), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('updated_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('no_buku')
    )
    op.create_table('user',
    sa.Column('id_user', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nama_user', sa.String(length=99), nullable=False),
    sa.Column('kontak', sa.String(length=99), nullable=False),
    sa.Column('flag', sa.String(length=2), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('updated_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id_user')
    )
    op.create_table('bookhistory',
    sa.Column('no_buku_history', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('no_buku', sa.Integer(), nullable=False),
    sa.Column('nama_buku', sa.String(length=80), nullable=False),
    sa.Column('penulis_buku', sa.String(length=80), nullable=False),
    sa.Column('status_peminjaman', sa.String(length=2), nullable=False),
    sa.Column('flag', sa.String(length=2), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['no_buku'], ['book.no_buku'], ),
    sa.PrimaryKeyConstraint('no_buku_history')
    )
    op.create_table('trans',
    sa.Column('id_trans', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('no_buku', sa.Integer(), nullable=False),
    sa.Column('lama', sa.Integer(), nullable=False),
    sa.Column('tanggal_pengembalian', sa.DateTime(), nullable=False),
    sa.Column('flag', sa.String(length=2), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('updated_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['user.id_user'], ),
    sa.ForeignKeyConstraint(['no_buku'], ['book.no_buku'], ),
    sa.PrimaryKeyConstraint('id_trans')
    )
    op.create_table('userhistory',
    sa.Column('id_user_history', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('nama_user', sa.String(length=99), nullable=False),
    sa.Column('kontak', sa.String(length=99), nullable=False),
    sa.Column('flag', sa.String(length=2), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['user.id_user'], ),
    sa.PrimaryKeyConstraint('id_user_history')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userhistory')
    op.drop_table('trans')
    op.drop_table('bookhistory')
    op.drop_table('user')
    op.drop_table('book')
    # ### end Alembic commands ###