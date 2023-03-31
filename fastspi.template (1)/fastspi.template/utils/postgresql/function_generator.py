"""This file generates the functions required for database"""
import sqlalchemy
from sqlalchemy import DDL
from sqlalchemy.orm import declarative_base
from config.database_connection import connection
Base = declarative_base()


create_refresh_modified_on_at_func = """
        CREATE FUNCTION refresh_modified_on_at()
        RETURNS TRIGGER AS $$
        BEGIN
        NEW.modified_on = (now() at time zone 'utc');
        RETURN NEW;
        END;
        $$ language 'plpgsql';
        """
connection.execute(create_refresh_modified_on_at_func)


def create_time_trigger_for_modified_on(table_name: str,table_base_class):
    """ Create a trigger based on table name """
    create_trigger = f"""
        CREATE TRIGGER trig_category_updated BEFORE INSERT OR UPDATE ON {table_name}
        FOR EACH ROW EXECUTE PROCEDURE refresh_modified_on_at();
        """
    metadata = {table_base_class}.metadata
    sqlalchemy.event.listen(
        metadata,
        'after_create',
        DDL(create_trigger)
    )



