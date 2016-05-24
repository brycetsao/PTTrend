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
  return db
end

def init_parser agent
  payload = { 'from' => '/bbs/Gossiping/index.html', 'yes' => 'yes' }
  agent.post 'https://www.ptt.cc/ask/over18', payload
  p = agent.page
  p.links[7].uri.path[/[0-9]+/].to_i.next
end

db = init_db
agent = Mechanize.new
last_page = init_parser agent
(1..last_page).to_a.reverse.each do |i|
  puts i
  agent.get "https://www.ptt.cc/bbs/Gossiping/index#{i}.html"
  links = agent.page.css('.r-list-container a')
  links.each do |l|

    p = agent.get l['href']

    comments = p.css('.push').map &:text

    article_info = p.css('.article-meta-value').map &:text
    author, board, title, date = article_info

    m = p.at_css('#main-content')
    m.search('.//div').remove
    content = m.text[/(.|\n)*--\n/]
    db.execute <<-SQL
      insert into article values(title, 'board', 'author', 'date', 'content', 'comment')
    SQL
    sleep(0.1) #avoid http 503
    #puts title, content, comments
  end
end

# db = SQLite3::Database.open 'ptt.db'

# current_year = 2016
# base_url = 'https://www.ptt.cc'



