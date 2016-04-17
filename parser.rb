require 'mechanize'
require 'sqlite3'

def init_db
  db = SQLite3::Database.new 'ptt.db'
  db.execute <<-SQL
    CREATE TABLE IF NOT EXISTS ARTICLE
      (
        TITLE TEXT(256),
        BOARD TEXT(16),
        AUTHOR TEXT(16),
        D DATE,
        CONTENT VARCHAR(65536),
        COMMENT VARCHAR(65536)
      );
    SQL
end

init_db
agent = Mechanize.new
payload = { 'from' => '/bbs/Gossiping/index.html', 'yes' => 'yes' }
agent.post 'https://www.ptt.cc/ask/over18', payload
p = agent.page
links = p.css('.r-list-container a')

# db = SQLite3::Database.open 'ptt.db'

# current_year = 2016
# base_url = 'https://www.ptt.cc'

links.each do |l|
	p = agent.get l['href']
	m = p.at_css('#main-content')

	comments = p.css('.push').map &:text
	# puts comments

	m.search('.//div').remove
	content = m.text[/(.|\n)*--\n/]
	# puts content


	# db.execute <<-SQL
	# 	insert into article values('title', 'board', 'author', 'date', m.text, comment)
	# SQL
end

