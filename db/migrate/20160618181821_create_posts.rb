class CreatePosts < ActiveRecord::Migration
  def change
    create_table :posts do |t|

      t.string :content
      t.boolean :political
      t.integer :proba_of_political
      t.integer :comment
      t.timestamps null: false
    end
  end
end
