require 'sqlite3'

db = SQLite3::Database.new 'ptt.db'
db.execute("SELECT * FROM ARTICLES") do |row|
  puts row
end
