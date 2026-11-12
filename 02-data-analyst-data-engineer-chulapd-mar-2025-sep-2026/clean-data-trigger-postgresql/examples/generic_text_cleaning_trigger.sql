-- Independent portfolio demo with a fictional table and non-clinical text.
-- This is not the production Supabase schema or cleaning logic.

CREATE TABLE IF NOT EXISTS demo_intake (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    free_text TEXT
);

CREATE OR REPLACE FUNCTION demo_clean_before_write()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.free_text := NULLIF(
        regexp_replace(btrim(COALESCE(NEW.free_text, '')), '\s+', ' ', 'g'),
        ''
    );
    RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS demo_clean_before_write_trigger ON demo_intake;

CREATE TRIGGER demo_clean_before_write_trigger
BEFORE INSERT OR UPDATE OF free_text ON demo_intake
FOR EACH ROW
EXECUTE FUNCTION demo_clean_before_write();

-- Fictional demonstration value only.
INSERT INTO demo_intake (free_text) VALUES ('  sample    response  ');
SELECT id, free_text FROM demo_intake;
