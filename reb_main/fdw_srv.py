from pg_srv import PGService

class FDWService:
	def __init__(self):
		self.pgsrv = PGService()
	
	def call_twitter_srv(self,fn_name,search_text,limit):
		twitter_query = ("insert into twitter_srv ( select * from fdw_twitter where fn_name = '%s' and search_text='%s' limit %s);") 						% (fn_name,search_text,limit)
		self.pgsrv.execute_ddl(twitter_query)
	def process_twitter_srv(self):
		pass
		