from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "6f2d1312d420"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column(
            "id",
            sa.UUID(as_uuid=True),
            primary_key=True,
            index=True,
            nullable=False,
            server_default=sa.text("gen_random_uuid()"),
        ),
        sa.Column("title", sa.String(), index=True, nullable=False),
        sa.Column("content", sa.String(), index=True, nullable=False),
        sa.Column(
            "published", sa.Boolean(), nullable=False, server_default=sa.text("true")
        ),
        sa.Column("rating", sa.Integer(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )


def downgrade() -> None:
    op.drop_table("posts")
