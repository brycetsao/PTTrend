module PostsHelper
  def political(p)
    if p.political
      return "政"
    else
      return ""
    end
  end
end
