twitter_fdw_sql = """	
			--- drop and create teh server			
			drop server if exists fdw_twitter_srv cascade;
			create server fdw_twitter_srv  FOREIGN DATA WRAPPER multicorn
			options (
 				 wrapper 'reb_main.TwitterFDW'
			);

			--- drop and create the foreign table

			DROP FOREIGN TABLE IF EXISTS fdw_twitter cascade;
			CREATE FOREIGN TABLE fdw_twitter (
			    tweet_data jsonb,
			    fn_name text,
			    search_text text			   
			)server fdw_twitter_srv options(
				access_token  '%s',
				access_token_secret  '%s',
				consumer_key '%s',
				consumer_secret  '%s');		


			CREATE TABLE IF NOT EXISTS twitter_srv (
			    tweet_data jsonb,
			    fn_name text,    
			    search_text text,
			    processed bool default false,
			    entry_time timestamp default now(),
			    pkid bigserial
			);
	
			
			"""
aws_pg_fdw_sql = """
drop server if exists fdw_aws_pg_srv cascade;
CREATE EXTENSION if not exists postgres_fdw;
CREATE SERVER fdw_aws_pg_srv FOREIGN DATA WRAPPER postgres_fdw OPTIONS (host '%s', dbname '%s', port '%s');
CREATE USER MAPPING FOR postgres SERVER fdw_aws_pg_srv OPTIONS (user '%s', password '%s' );

CREATE FOREIGN TABLE fdw_webanalytics_aws
(
  dtype character varying(10),
  event jsonb,
  header jsonb,
  createdat timestamp without time zone DEFAULT now()
) SERVER fdw_aws_pg_srv OPTIONS (schema_name 'public', table_name 'webanalytics_aws'); 
"""


owm_fdw_sql = """	
--- drop and create teh server			
drop server if exists fdw_openweathermap_srv cascade;
create server fdw_openweathermap_srv  FOREIGN DATA WRAPPER multicorn
options (
	 wrapper 'reb_main.OWMFDW'
);

--- drop and create the foreign table

DROP FOREIGN TABLE IF EXISTS fdw_openweathermap cascade;
CREATE FOREIGN TABLE fdw_openweathermap (
    weather_data text,
    fn_name text,
    city_name text,
    country_name text 	   
)server fdw_openweathermap_srv options( key  '%s');		

"""
