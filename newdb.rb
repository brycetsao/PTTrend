require 'sqlite3'

db = SQLite3::Database.new 'ptt.db'
db.execute
	<<-SQL
	create table article
		(
			title varchar(256),
			board varchar(16)
			author varchar(16),
			d date(),
			content varchar(65536),
			comment varray(1000) of varchar(256)
		);
	SQL