from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic, wikiArticle, rating):
	knowledge_object=Knowledge(
		topic=topic,
		wikiArticle = wikiArticle,
		rating= rating)
	session.add(knowledge_object)
	session.commit()
		
add_article("Britain","weather",9)
add_article("rainbow","weather",9)
add_article("rainbow","weather",9)
add_article("rainbow","weather",9)

		
	

def query_all_articles():
	article1=session.query(
		Knowledge).first()
	return article1
print(query_all_articles())
	

def query_article_by_topic(topic):
	topic1=session.query(
		Knowledge).filter_by(topic=topic).first()
	return topic1
print(query_article_by_topic("Britain"))
	

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(
		topic=topic).delete()
	session.commit()

	

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()
# delete_all_articles()


def edit_article_rating(update_rating,article_title):
	article_object=session.query(
		Knowledge).filter_by(
		topic=article_title).first()
	print(article_object)
	article_object.rating=update_rating
	session.commit()
edit_article_rating(11, "Britain")


