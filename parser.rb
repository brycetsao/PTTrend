require 'mechanize'
require 'rmmseg'

agent = Mechanize.new
payload = { 'from' => '/bbs/Gossiping/index.html', 'yes' => 'yes' }
agent.post 'https://www.ptt.cc/ask/over18', payload
p = agent.page
links = p.css('.r-list-container a')[1, 0]


links.each do |l|
	p = agent.get l['href']
	m = p.at_css('#main-content')
	m.search('.//div').remove
	# puts m.text
	puts 'a'
end