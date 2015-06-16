Final Project for Intro to Hadoop and MapReduce from Udacity
==========================================
This repository hosts the required Mapper and Reducer codes for the final project of this course.

#Intro to Hadoop and Mapreduce Project Explanation
In this project you will work with discussion forum (also sometimes called discussion board) data. It is one type of user generated content that you can find all around the web. Most popular websites have some kind of a forum, and the things you will do in this project can transfer to other similar projects.

This particular dataset is taken from Udacity forums the first months after launch. Udacity forums are run on free, opensource software called OSQA, which was designed to be similar to the popular StackOverflow forums. The basic structure is - the forum has nodes. All nodes have a body and author_id. Top level nodes are called questions, and will also have a title and tags. Questions can have answers. Both questions and answers can have comments. If you are not sure how that all looks, please go to the class discussion forum and look around!

You will have to run the code mostly on your VMs, or on your real Hadoop cluster, if you have set up one. You can download the additional dataset here. To unarchive it, download it to your VM, put in the data directory and run:

tar zxvf forum_data.tar.gz
There are 2 files in the dataset. The first is "forum_nodes.tsv", and that contains all forum questions and answers in one table. It was exported from the RDBMS by using tab as a separator, and enclosing all fields in doublequotes. If you finished Lesson 4, you already know how to deal with such files. You can find the field names in the first line of the file "forum_node.tsv". The ones that are the most relevant to the task are:

- "id": id of the node
- "title": title of the node. in case "node_type" is "answer" or "comment", this field will be empty
- "tagnames": space separated list of tags
- "author_id": id of the author
- "body": content of the post
- "node_type": type of the node, either "question", "answer" or "comment"
- "parent_id": node under which the post is located, will be empty for "questions"
- "abs_parent_id": top node where the post is located
- "added_at": date added


The second table is "forum_users.tsv". It contains fields for "user_ptr_id" - the id of the user. "reputation" - the reputation, or karma of the user, earned when other users upvote their posts, and the number of "gold", "silver" and "bronze" badges earned. The actual database has more fields in this table, like user name nickname, bio (if set) etc, but we have removed this information here.
 
## Files
The following files are the Mappers and Reducers required for each part of the project:
- study_groups_mapper.py       [Study Groups Exercise]
- study_groups_reducer.py       [Study Groups Exercise]
- student_times_mapper.py      [Student Times Exercise]
- student_times_reducer.py      [Student Times Exercise]
- average_length_mapper.py      [Post and Answer Length Exercise]
- average_length_reducer.py      [Post and Answer Length Exercise]
- popular_tags_mapper.py        [Top Tags Exercise]
- popular_tags_reducer.py        [Top Tags Exercise]