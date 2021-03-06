process_twitter_sql = """

---:::::::::::::::::::home_timeline::::::::::::::
drop table if exists twitter_home_timeline;
create table twitter_home_timeline(contributors text ,
truncated text ,
text text ,
is_quote_status text ,
in_reply_to_status_id text ,
id text ,
favorite_count int ,
_api text ,
author text ,
_json text ,
coordinates text ,
entities text ,
in_reply_to_screen_name text ,
in_reply_to_user_id text ,
retweet_count int ,
id_str text ,
favorited text ,
source_url text ,
_user text ,
geo text ,
in_reply_to_user_id_str text ,
possibly_sensitive text ,
possibly_sensitive_appealable text ,
lang text ,
created_at text ,
in_reply_to_status_id_str text ,
place text ,
source text ,
retweeted text ,fkid integer);

------------------------------------------------------------
insert into twitter_home_timeline select tweet_data ->> 'contributors' as contributors,
tweet_data ->> 'truncated' as truncated,
tweet_data ->> 'text' as text,
tweet_data ->> 'is_quote_status' as is_quote_status,
tweet_data ->> 'in_reply_to_status_id' as in_reply_to_status_id,
tweet_data ->> 'id' as id,
(tweet_data ->> 'favorite_count')::text::int as favorite_count,
tweet_data ->> '_api' as _api,
tweet_data ->> 'author' as author,
tweet_data ->> '_json' as _json,
tweet_data ->> 'coordinates' as coordinates,
tweet_data ->> 'entities' as entities,
tweet_data ->> 'in_reply_to_screen_name' as in_reply_to_screen_name,
tweet_data ->> 'in_reply_to_user_id' as in_reply_to_user_id,
(tweet_data ->> 'retweet_count')::text::int as retweet_count,
tweet_data ->> 'id_str' as id_str,
tweet_data ->> 'favorited' as favorited,
tweet_data ->> 'source_url' as source_url,
tweet_data ->> '_user' as _user,
tweet_data ->> 'geo' as geo,
tweet_data ->> 'in_reply_to_user_id_str' as in_reply_to_user_id_str,
tweet_data ->> 'possibly_sensitive' as possibly_sensitive,
tweet_data ->> 'possibly_sensitive_appealable' as possibly_sensitive_appealable,
tweet_data ->> 'lang' as lang,
tweet_data ->> 'created_at' as created_at,
tweet_data ->> 'in_reply_to_status_id_str' as in_reply_to_status_id_str,
tweet_data ->> 'place' as place,
tweet_data ->> 'source' as source,
tweet_data ->> 'retweeted' as retweeted,pkid from twitter_srv where fn_name = 'home_timeline';

---::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
---:::::::::::::::::::user_timeline::::::::::::::
drop table if exists twitter_user_timeline;
create table twitter_user_timeline(contributors text ,
truncated text ,
text text ,
is_quote_status text ,
in_reply_to_status_id text ,
id text ,
favorite_count int ,
_api text ,
author text ,
_json text ,
coordinates text ,
entities text ,
in_reply_to_screen_name text ,
in_reply_to_user_id text ,
retweet_count int ,
id_str text ,
favorited text ,
source_url text ,
_user text ,
geo text ,
in_reply_to_user_id_str text ,
lang text ,
created_at text ,
in_reply_to_status_id_str text ,
place text ,
source text ,
retweeted text ,fkid integer);

------------------------------------------------------------
insert into twitter_user_timeline select tweet_data ->> 'contributors' as contributors,
tweet_data ->> 'truncated' as truncated,
tweet_data ->> 'text' as text,
tweet_data ->> 'is_quote_status' as is_quote_status,
tweet_data ->> 'in_reply_to_status_id' as in_reply_to_status_id,
tweet_data ->> 'id' as id,
(tweet_data ->> 'favorite_count')::text::int as favorite_count,
tweet_data ->> '_api' as _api,
tweet_data ->> 'author' as author,
tweet_data ->> '_json' as _json,
tweet_data ->> 'coordinates' as coordinates,
tweet_data ->> 'entities' as entities,
tweet_data ->> 'in_reply_to_screen_name' as in_reply_to_screen_name,
tweet_data ->> 'in_reply_to_user_id' as in_reply_to_user_id,
(tweet_data ->> 'retweet_count')::text::int as retweet_count,
tweet_data ->> 'id_str' as id_str,
tweet_data ->> 'favorited' as favorited,
tweet_data ->> 'source_url' as source_url,
tweet_data ->> '_user' as _user,
tweet_data ->> 'geo' as geo,
tweet_data ->> 'in_reply_to_user_id_str' as in_reply_to_user_id_str,
tweet_data ->> 'lang' as lang,
tweet_data ->> 'created_at' as created_at,
tweet_data ->> 'in_reply_to_status_id_str' as in_reply_to_status_id_str,
tweet_data ->> 'place' as place,
tweet_data ->> 'source' as source,
tweet_data ->> 'retweeted' as retweeted,pkid from twitter_srv where fn_name = 'user_timeline';

---::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
---:::::::::::::::::::retweets_of_me::::::::::::::
drop table if exists twitter_retweets_of_me;
create table twitter_retweets_of_me(contributors text ,
truncated text ,
text text ,
is_quote_status text ,
in_reply_to_status_id text ,
id text ,
favorite_count int ,
_api text ,
author text ,
_json text ,
coordinates text ,
entities text ,
in_reply_to_screen_name text ,
in_reply_to_user_id text ,
retweet_count int ,
id_str text ,
favorited text ,
source_url text ,
_user text ,
geo text ,
in_reply_to_user_id_str text ,
lang text ,
created_at text ,
in_reply_to_status_id_str text ,
place text ,
source text ,
retweeted text ,fkid integer);

------------------------------------------------------------
insert into twitter_retweets_of_me select tweet_data ->> 'contributors' as contributors,
tweet_data ->> 'truncated' as truncated,
tweet_data ->> 'text' as text,
tweet_data ->> 'is_quote_status' as is_quote_status,
tweet_data ->> 'in_reply_to_status_id' as in_reply_to_status_id,
tweet_data ->> 'id' as id,
(tweet_data ->> 'favorite_count')::text::int as favorite_count,
tweet_data ->> '_api' as _api,
tweet_data ->> 'author' as author,
tweet_data ->> '_json' as _json,
tweet_data ->> 'coordinates' as coordinates,
tweet_data ->> 'entities' as entities,
tweet_data ->> 'in_reply_to_screen_name' as in_reply_to_screen_name,
tweet_data ->> 'in_reply_to_user_id' as in_reply_to_user_id,
(tweet_data ->> 'retweet_count')::text::int as retweet_count,
tweet_data ->> 'id_str' as id_str,
tweet_data ->> 'favorited' as favorited,
tweet_data ->> 'source_url' as source_url,
tweet_data ->> '_user' as _user,
tweet_data ->> 'geo' as geo,
tweet_data ->> 'in_reply_to_user_id_str' as in_reply_to_user_id_str,
tweet_data ->> 'lang' as lang,
tweet_data ->> 'created_at' as created_at,
tweet_data ->> 'in_reply_to_status_id_str' as in_reply_to_status_id_str,
tweet_data ->> 'place' as place,
tweet_data ->> 'source' as source,
tweet_data ->> 'retweeted' as retweeted,pkid from twitter_srv where fn_name = 'retweets_of_me';

---::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
---:::::::::::::::::::followers::::::::::::::
drop table if exists twitter_followers;
create table twitter_followers(follow_request_sent text ,
has_extended_profile text ,
profile_use_background_image text ,
_json text ,
time_zone text ,
id text ,
description text ,
_api text ,
verified text ,
blocked_by text ,
profile_text_color text ,
muting text ,
profile_image_url_https text ,
profile_sidebar_fill_color text ,
is_translator text ,
geo_enabled text ,
entities text ,
followers_count int ,
protected text ,
id_str text ,
default_profile_image text ,
listed_count int ,
status text ,
lang text ,
utc_offset text ,
statuses_count int ,
profile_background_color text ,
friends_count int ,
profile_link_color text ,
profile_image_url text ,
notifications text ,
profile_background_image_url_https text ,
blocking text ,
profile_background_image_url text ,
name text ,
is_translation_enabled text ,
profile_background_tile text ,
favourites_count int ,
screen_name text ,
url text ,
created_at text ,
contributors_enabled text ,
location text ,
profile_sidebar_border_color text ,
default_profile text ,
following text ,fkid integer);

------------------------------------------------------------
insert into twitter_followers select tweet_data ->> 'follow_request_sent' as follow_request_sent,
tweet_data ->> 'has_extended_profile' as has_extended_profile,
tweet_data ->> 'profile_use_background_image' as profile_use_background_image,
tweet_data ->> '_json' as _json,
tweet_data ->> 'time_zone' as time_zone,
tweet_data ->> 'id' as id,
tweet_data ->> 'description' as description,
tweet_data ->> '_api' as _api,
tweet_data ->> 'verified' as verified,
tweet_data ->> 'blocked_by' as blocked_by,
tweet_data ->> 'profile_text_color' as profile_text_color,
tweet_data ->> 'muting' as muting,
tweet_data ->> 'profile_image_url_https' as profile_image_url_https,
tweet_data ->> 'profile_sidebar_fill_color' as profile_sidebar_fill_color,
tweet_data ->> 'is_translator' as is_translator,
tweet_data ->> 'geo_enabled' as geo_enabled,
tweet_data ->> 'entities' as entities,
(tweet_data ->> 'followers_count')::text::int as followers_count,
tweet_data ->> 'protected' as protected,
tweet_data ->> 'id_str' as id_str,
tweet_data ->> 'default_profile_image' as default_profile_image,
(tweet_data ->> 'listed_count')::text::int as listed_count,
tweet_data ->> 'status' as status,
tweet_data ->> 'lang' as lang,
tweet_data ->> 'utc_offset' as utc_offset,
(tweet_data ->> 'statuses_count')::text::int as statuses_count,
tweet_data ->> 'profile_background_color' as profile_background_color,
(tweet_data ->> 'friends_count')::text::int as friends_count,
tweet_data ->> 'profile_link_color' as profile_link_color,
tweet_data ->> 'profile_image_url' as profile_image_url,
tweet_data ->> 'notifications' as notifications,
tweet_data ->> 'profile_background_image_url_https' as profile_background_image_url_https,
tweet_data ->> 'blocking' as blocking,
tweet_data ->> 'profile_background_image_url' as profile_background_image_url,
tweet_data ->> 'name' as name,
tweet_data ->> 'is_translation_enabled' as is_translation_enabled,
tweet_data ->> 'profile_background_tile' as profile_background_tile,
(tweet_data ->> 'favourites_count')::text::int as favourites_count,
tweet_data ->> 'screen_name' as screen_name,
tweet_data ->> 'url' as url,
tweet_data ->> 'created_at' as created_at,
tweet_data ->> 'contributors_enabled' as contributors_enabled,
tweet_data ->> 'location' as location,
tweet_data ->> 'profile_sidebar_border_color' as profile_sidebar_border_color,
tweet_data ->> 'default_profile' as default_profile,
tweet_data ->> 'following' as following,pkid from twitter_srv where fn_name = 'followers';

---::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
---:::::::::::::::::::friends::::::::::::::
drop table if exists twitter_friends;
create table twitter_friends(follow_request_sent text ,
has_extended_profile text ,
profile_use_background_image text ,
_json text ,
time_zone text ,
id text ,
description text ,
_api text ,
verified text ,
blocked_by text ,
profile_text_color text ,
muting text ,
profile_image_url_https text ,
profile_sidebar_fill_color text ,
is_translator text ,
geo_enabled text ,
entities text ,
followers_count int ,
protected text ,
id_str text ,
default_profile_image text ,
listed_count int ,
status text ,
lang text ,
utc_offset text ,
statuses_count int ,
profile_background_color text ,
friends_count int ,
profile_link_color text ,
profile_image_url text ,
notifications text ,
profile_background_image_url_https text ,
blocking text ,
profile_background_image_url text ,
name text ,
is_translation_enabled text ,
profile_background_tile text ,
favourites_count int ,
screen_name text ,
url text ,
created_at text ,
contributors_enabled text ,
location text ,
profile_sidebar_border_color text ,
default_profile text ,
following text ,fkid integer);

------------------------------------------------------------
insert into twitter_friends select tweet_data ->> 'follow_request_sent' as follow_request_sent,
tweet_data ->> 'has_extended_profile' as has_extended_profile,
tweet_data ->> 'profile_use_background_image' as profile_use_background_image,
tweet_data ->> '_json' as _json,
tweet_data ->> 'time_zone' as time_zone,
tweet_data ->> 'id' as id,
tweet_data ->> 'description' as description,
tweet_data ->> '_api' as _api,
tweet_data ->> 'verified' as verified,
tweet_data ->> 'blocked_by' as blocked_by,
tweet_data ->> 'profile_text_color' as profile_text_color,
tweet_data ->> 'muting' as muting,
tweet_data ->> 'profile_image_url_https' as profile_image_url_https,
tweet_data ->> 'profile_sidebar_fill_color' as profile_sidebar_fill_color,
tweet_data ->> 'is_translator' as is_translator,
tweet_data ->> 'geo_enabled' as geo_enabled,
tweet_data ->> 'entities' as entities,
(tweet_data ->> 'followers_count')::text::int as followers_count,
tweet_data ->> 'protected' as protected,
tweet_data ->> 'id_str' as id_str,
tweet_data ->> 'default_profile_image' as default_profile_image,
(tweet_data ->> 'listed_count')::text::int as listed_count,
tweet_data ->> 'status' as status,
tweet_data ->> 'lang' as lang,
tweet_data ->> 'utc_offset' as utc_offset,
(tweet_data ->> 'statuses_count')::text::int as statuses_count,
tweet_data ->> 'profile_background_color' as profile_background_color,
(tweet_data ->> 'friends_count')::text::int as friends_count,
tweet_data ->> 'profile_link_color' as profile_link_color,
tweet_data ->> 'profile_image_url' as profile_image_url,
tweet_data ->> 'notifications' as notifications,
tweet_data ->> 'profile_background_image_url_https' as profile_background_image_url_https,
tweet_data ->> 'blocking' as blocking,
tweet_data ->> 'profile_background_image_url' as profile_background_image_url,
tweet_data ->> 'name' as name,
tweet_data ->> 'is_translation_enabled' as is_translation_enabled,
tweet_data ->> 'profile_background_tile' as profile_background_tile,
(tweet_data ->> 'favourites_count')::text::int as favourites_count,
tweet_data ->> 'screen_name' as screen_name,
tweet_data ->> 'url' as url,
tweet_data ->> 'created_at' as created_at,
tweet_data ->> 'contributors_enabled' as contributors_enabled,
tweet_data ->> 'location' as location,
tweet_data ->> 'profile_sidebar_border_color' as profile_sidebar_border_color,
tweet_data ->> 'default_profile' as default_profile,
tweet_data ->> 'following' as following,pkid from twitter_srv where fn_name = 'friends';

---::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
---:::::::::::::::::::search::::::::::::::
drop table if exists twitter_search;
create table twitter_search(contributors text ,
truncated text ,
text text ,
is_quote_status text ,
in_reply_to_status_id text ,
id text ,
favorite_count int ,
_api text ,
author text ,
_json text ,
coordinates text ,
entities text ,
in_reply_to_screen_name text ,
id_str text ,
retweet_count int ,
in_reply_to_user_id text ,
favorited text ,
source_url text ,
_user text ,
geo text ,
in_reply_to_user_id_str text ,
possibly_sensitive text ,
lang text ,
created_at text ,
in_reply_to_status_id_str text ,
place text ,
source text ,
retweeted text ,
metadata text ,fkid integer);

------------------------------------------------------------
insert into twitter_search select tweet_data ->> 'contributors' as contributors,
tweet_data ->> 'truncated' as truncated,
tweet_data ->> 'text' as text,
tweet_data ->> 'is_quote_status' as is_quote_status,
tweet_data ->> 'in_reply_to_status_id' as in_reply_to_status_id,
tweet_data ->> 'id' as id,
(tweet_data ->> 'favorite_count')::text::int as favorite_count,
tweet_data ->> '_api' as _api,
tweet_data ->> 'author' as author,
tweet_data ->> '_json' as _json,
tweet_data ->> 'coordinates' as coordinates,
tweet_data ->> 'entities' as entities,
tweet_data ->> 'in_reply_to_screen_name' as in_reply_to_screen_name,
tweet_data ->> 'id_str' as id_str,
(tweet_data ->> 'retweet_count')::text::int as retweet_count,
tweet_data ->> 'in_reply_to_user_id' as in_reply_to_user_id,
tweet_data ->> 'favorited' as favorited,
tweet_data ->> 'source_url' as source_url,
tweet_data ->> '_user' as _user,
tweet_data ->> 'geo' as geo,
tweet_data ->> 'in_reply_to_user_id_str' as in_reply_to_user_id_str,
tweet_data ->> 'possibly_sensitive' as possibly_sensitive,
tweet_data ->> 'lang' as lang,
tweet_data ->> 'created_at' as created_at,
tweet_data ->> 'in_reply_to_status_id_str' as in_reply_to_status_id_str,
tweet_data ->> 'place' as place,
tweet_data ->> 'source' as source,
tweet_data ->> 'retweeted' as retweeted,
tweet_data ->> 'metadata' as metadata,pkid from twitter_srv where fn_name = 'search';

---::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
---:::::::: USERS QUERY :::::::::::::::::::::
DROP TABLE IF EXISTS TWITTER_USER;
create table twitter_user(
follow_request_sent text ,
has_extended_profile text ,
profile_use_background_image text ,
_json text ,
time_zone text ,
id text ,
_api text ,
verified text ,
profile_text_color text ,
profile_image_url_https text ,
profile_sidebar_fill_color text ,
is_translator text ,
geo_enabled text ,
entities text ,
followers_count int ,
protected text ,
id_str text ,
default_profile_image text ,
listed_count int ,
lang text ,
utc_offset text ,
statuses_count int ,
description text ,
friends_count int ,
profile_link_color text ,
profile_image_url text ,
notifications text ,
profile_background_image_url_https text ,
profile_background_color text ,
profile_banner_url text ,
profile_background_image_url text ,
name text ,
is_translation_enabled text ,
profile_background_tile text ,
favourites_count int ,
screen_name text ,
url text ,
created_at text ,
contributors_enabled text ,
location text ,
profile_sidebar_border_color text ,
default_profile text ,
following text, 

fkid integer
);


insert into twitter_user select tweet_data ->> 'follow_request_sent' as follow_request_sent,
tweet_data ->> 'has_extended_profile' as has_extended_profile,
tweet_data ->> 'profile_use_background_image' as profile_use_background_image,
tweet_data ->> '_json' as _json,
tweet_data ->> 'time_zone' as time_zone,
tweet_data ->> 'id' as id,
tweet_data ->> '_api' as _api,
tweet_data ->> 'verified' as verified,
tweet_data ->> 'profile_text_color' as profile_text_color,
tweet_data ->> 'profile_image_url_https' as profile_image_url_https,
tweet_data ->> 'profile_sidebar_fill_color' as profile_sidebar_fill_color,
tweet_data ->> 'is_translator' as is_translator,
tweet_data ->> 'geo_enabled' as geo_enabled,
tweet_data ->> 'entities' as entities,
(tweet_data ->> 'followers_count')::text::int as followers_count,
tweet_data ->> 'protected' as protected,
tweet_data ->> 'id_str' as id_str,
tweet_data ->> 'default_profile_image' as default_profile_image,
(tweet_data ->> 'listed_count')::text::int as listed_count,
tweet_data ->> 'lang' as lang,
tweet_data ->> 'utc_offset' as utc_offset,
(tweet_data ->> 'statuses_count')::text::int as statuses_count,
tweet_data ->> 'description' as description,
(tweet_data ->> 'friends_count')::text::int as friends_count,
tweet_data ->> 'profile_link_color' as profile_link_color,
tweet_data ->> 'profile_image_url' as profile_image_url,
tweet_data ->> 'notifications' as notifications,
tweet_data ->> 'profile_background_image_url_https' as profile_background_image_url_https,
tweet_data ->> 'profile_background_color' as profile_background_color,
tweet_data ->> 'profile_banner_url' as profile_banner_url,
tweet_data ->> 'profile_background_image_url' as profile_background_image_url,
tweet_data ->> 'name' as name,
tweet_data ->> 'is_translation_enabled' as is_translation_enabled,
tweet_data ->> 'profile_background_tile' as profile_background_tile,
(tweet_data ->> 'favourites_count')::text::int as favourites_count,
tweet_data ->> 'screen_name' as screen_name,
tweet_data ->> 'url' as url,
tweet_data ->> 'created_at' as created_at,
tweet_data ->> 'contributors_enabled' as contributors_enabled,
tweet_data ->> 'location' as location,
tweet_data ->> 'profile_sidebar_border_color' as profile_sidebar_border_color,
tweet_data ->> 'default_profile' as default_profile,
tweet_data ->> 'following' as following,
pkid
from twitter_srv ;

"""


init_pg_db = """

create table if not exists column_meta(
	id bigserial primary key,
	column_name text,
	table_name text,
	data_type text,
	related_to_columns text[],
	relation_types text[],
	aliases text[]
	
	
);
create table  if not exists service_meta(
	id bigserial primary key,
	service_name text,
	service_type text,
	related_to_columns text[],
	refresh_interval_sec int,
	represented_by_tables text[]  
	
);

insert into service_meta(
	service_name,
	service_type,	
	refresh_interval_sec,
	represented_by_tables
)values(
	'twitter_srv',
	'social',
	3600,
	ARRAY['twitter_srv','twitter_search','twitter_home_timeline','twitter_friends','twitter_user_timeline','twitter_retweets_of_me','twitter_followers']	
);
insert into service_meta(
	service_name,
	service_type,	
	refresh_interval_sec,
	represented_by_tables
)values(
	'aws_pg_srv',
	'aws',
	0,
	ARRAY['webanalytics_aws']	
);
insert into service_meta(
	service_name,
	service_type,	
	refresh_interval_sec,
	represented_by_tables
)values(
	'fdw_openweathermap',
	'weather',
	3600*12,
	ARRAY['fdw_openweathermap']	
);


create table if not exists facts_table(
	id bigserial primary key,
	fact_table_name text,
	table_name text,		
	key_type text, 
	key_val text,
	dt_type text
);
"""

