require 'mechanize'
require 'sqlite3'

def init_db
  db = SQLite3::Database.new 'ptt.db'
  db.execute <<-SQL
    CREATE TABLE IF NOT EXISTS ARTICLES
      (
        id INTEGER PRIMARY KEY,
        TITLE TEXT(256),
        BOARD TEXT(16),
        AUTHOR TEXT(16),
        D DATE,
        CONTENT NVARCHAR(4096),
        COMMENT NVARCHAR(4096),
        PUSH INTEGER,
        BOO INTEGER,
        COM INTEGER,
        POLITICAL BOOLEAN,
        LABELED BOOLEAN
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

db = init_db #初始化資料庫
agent = Mechanize.new #HTML Parser，底層使用Nokogiri
last_page = init_parser agent #爬取PTT Gossiping文章的最後一頁頁碼
cnt = 0
(1..last_page).to_a.reverse.each do |i| #爬取從第一頁到最後一頁的連結
  agent.get "https://www.ptt.cc/bbs/Gossiping/index#{i}.html"
  links = agent.page.css('.r-list-container a')#抓取連結網址
  links.each do |l|

    p = agent.get l['href']#抓取網頁

    comments = p.css('.push').map(&:text)#抓取推噓文

    push = boo = com = 0
    comments.each do |c|
      case c[0]
        when "推"
          push += 1
        when "噓"
          boo += 1
        else
          com += 1
      end
    end

    article_info = p.css('.article-meta-value').map(&:text)#抓取作者、版面、標題、時間等資訊
    author, board, title, date = article_info

    m = p.at_css('#main-content')
    m.search('.//div').remove
    content = m.text[/(.|\n)*--\n/]#抓取文章內文
    comment = comments.join(',')

    db.execute("INSERT INTO ARTICLES ('title', 'board', 'author', 'd', 'content', 'comment', 'push', 'boo', 'com', 'political', 'labeled')
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                [title, board, author, date, content, comment, push, boo, com, 0, 0])#寫入資料庫
    sleep(0.1) #avoid http 503
  end
  cnt += 1
  puts cnt
  break if cnt == 100
end