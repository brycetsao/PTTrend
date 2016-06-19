class Post < ActiveRecord::Base
  validates_presence_of :content, :author, :title
  before_save :python

  def python
    #PttrendJob.perform_later(self.id)
    result = `cd lib/assets/python/ && echo "#{self.content}" | python3 pttrend.py -i -l`.split("\n")
    if result[1] == "[1]"
      self.political = true
    end
    self.proba_of_political = (result[2].split[2][0..-3].to_f * 100).to_i
    self.comment = result[3].to_i
  end
end
