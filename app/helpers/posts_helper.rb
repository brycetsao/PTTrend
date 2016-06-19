module PostsHelper
  def political(p)
    if p.political
      return "政"
    else
      return ""
    end
  end

  def comment(c)
    if c.nil?
      return
    elsif c < -99
      return content_tag(:span, "XX", :class => "hl f0")
    elsif c <= -10
      return content_tag(:span, "X#{c.abs / 10}", :class => "hl f0")
    elsif c <= 0
      return content_tag(:span, "")
    elsif c > 99
      return content_tag(:span, "爆", :class => "hl f1")
    elsif c < 10
      return content_tag(:span, c, :class => "hl f2")
    else
      return content_tag(:span, c, :class => "hl f3")
    end
  end

  def comment_details(c)
    if c.nil?
      return
    elsif c >= 0
      return "#{c}推"
    else
      return "#{c.abs}噓"
    end
  end

end
