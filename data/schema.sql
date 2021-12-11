-- Drop tables if exists
DROP TABLE IF EXISTS clean_data_df

-- Create data_clean table for raw dataset
CREATE TABLE clean_data_df (
	id SERIAL PRIMARY KEY,
	title VARCHAR,
	author VARCHAR,
	content VARCHAR,
	label NUMERIC
)