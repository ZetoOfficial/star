"""add triggers

Revision ID: 4d937cbf9e4b
Revises: 68bd91677569
Create Date: 2023-12-01 14:12:58.430725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4d937cbf9e4b"
down_revision = "68bd91677569"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create audit trigger function
    op.execute(
        """
    CREATE OR REPLACE FUNCTION audit_trigger_function()
    RETURNS TRIGGER AS $$
    BEGIN
        IF (TG_OP = 'DELETE') THEN
            INSERT INTO audit (table_name, row_id, old_value, operation_type, timestamp)
            VALUES (TG_TABLE_NAME, OLD.id, row_to_json(OLD), TG_OP, now());
            RETURN OLD;
        ELSIF (TG_OP = 'UPDATE') THEN
            INSERT INTO audit (table_name, row_id, old_value, new_value, operation_type, timestamp)
            VALUES (TG_TABLE_NAME, NEW.id, row_to_json(OLD), row_to_json(NEW), TG_OP, now());
            RETURN NEW;
        ELSIF (TG_OP = 'INSERT') THEN
            INSERT INTO audit (table_name, row_id, new_value, operation_type, timestamp)
            VALUES (TG_TABLE_NAME, NEW.id, row_to_json(NEW), TG_OP, now());
            RETURN NEW;
        END IF;
        RETURN NULL; -- result is ignored since this is an AFTER trigger
    END;
    $$ LANGUAGE plpgsql;
    """
    )

    # Create triggers for each table
    tables = [
        "universe",
        "star_constellation",
        "star",
        "planet",
        "galaxy",
        "constellation",
    ]
    for table in tables:
        op.execute(
            f"""
        CREATE TRIGGER {table}_audit_trigger
        AFTER INSERT OR UPDATE OR DELETE ON {table}
            FOR EACH ROW EXECUTE FUNCTION audit_trigger_function();
        """
        )


def downgrade() -> None:
    # Remove triggers and the function
    tables = [
        "universe",
        "star_constellation",
        "star",
        "planet",
        "galaxy",
        "constellation",
    ]
    for table in tables:
        op.execute(f"DROP TRIGGER IF EXISTS {table}_audit_trigger ON {table};")

    op.execute("DROP FUNCTION IF EXISTS audit_trigger_function;")
