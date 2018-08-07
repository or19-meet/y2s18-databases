from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = "knowledge"
	knowledge = Column(Integer, primary_key=True)
	wikiArticle = Column(String)
	topic = Column(String)
	rating = Column(Integer)

	def __repr__(self):
		return("knowledge topic: {}\n"
				"Knowledge wikiArticle: {}\n"
				"Knowledge rating: {}").format(
				self.topic,
				self.wikiArticle,
				self.rating)
		print(repr(Knowledge.__tablename__))
		

x= Knowledge(topic="Britain", wikiArticle="royal family", rating=10)
print(x)