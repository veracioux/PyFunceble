"""Allow whois record to be empty/NULL

Revision ID: d8893cd406db
Revises: 35c79626ecb9
Create Date: 2020-08-22 17:27:52.087506

"""
from alembic import op
from sqlalchemy.dialects import mysql

# pylint: skip-file

# revision identifiers, used by Alembic.
revision = "d8893cd406db"
down_revision = "35c79626ecb9"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "pyfunceble_whois_record",
        "record",
        existing_type=mysql.TEXT(collation="utf8mb4_unicode_ci"),
        nullable=True,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "pyfunceble_whois_record",
        "record",
        existing_type=mysql.TEXT(collation="utf8mb4_unicode_ci"),
        nullable=False,
    )
    # ### end Alembic commands ###