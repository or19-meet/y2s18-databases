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
		
		
add_article("rainbow","weather",9)

		
	

def query_all_articles():
	pass

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
