import psycopg2
from reb_main.pg_srv import PGService

class CreateExtn:
	
	def __init__(self):
		
			
		init_query = ("""
				--- create service_reg if not exists		
				create table if not exists service_reg( service_name varchar(16), key_name varchar(16), key text );
				create extension if not exists multicorn;
		""")
		self.pgsrv = PGService()
		self.pgsrv.execute_ddl(init_query)
		

	def init_twitter_extn(self):
		access_token = self.pgsrv.execute_dml("select key from service_reg where service_name = 'twitter_srv' and key_name = 								'access_token'")[0][0] 
		
 		access_token_secret = self.pgsrv.execute_dml("select key from service_reg where service_name = 'twitter_srv' and key_name = 								'access_token_secret'") [0][0]
		
		consumer_key = self.pgsrv.execute_dml("select key from service_reg where service_name = 'twitter_srv' and key_name = 								'consumer_key'")[0][0]
		
		consumer_secret = self.pgsrv.execute_dml("select key from service_reg where service_name = 'twitter_srv' and key_name = 								'consumer_secret'")[0][0]
 
		twitter_sql = ("""	
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
	
			
			""") % (access_token, access_token_secret,consumer_key,consumer_secret)
				
		self.pgsrv.execute_ddl(twitter_sql)

