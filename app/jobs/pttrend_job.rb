class PttrendJob < ActiveJob::Base
  queue_as :default

  def perform(post_id)
    # Do something later
    #include Sidekiq::Worker
    post = Post.find(post_id)
    result = `cd lib/assets/python/ && echo #{post.content} | python3 pttrend.py -i -l`.split("\n")
    if result[1] == "[1]"
      post.political = true
    end
    post.proba_of_political = (result[2].split[2][0..-3].to_f * 100).to_i
    post.comment = result[3].to_i
    post.save
  end
end
