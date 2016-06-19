class PostsController < ApplicationController
  before_action :find_post, :only => [ :show, :edit, :update, :destroy ]

  def index
    @posts = Post.all
  end

  def show
  end

  def new
    @post = Post.new
  end

  def create
    @post = Post.create(post_params)
    if @post.save
      redirect_to posts_path
    else
      render new_post_path
    end
  end

  def edit
  end

  def update
    @post.update(post_params)
  end

  def destroy
    @post.destroy
    redirect_to posts_path
  end

  private
  def post_params
    params.require(:post).permit(:content, :political, :proba_of_political, :comment)
  end

  def find_post
    @post = Post.find(params[:id])
  end
end
