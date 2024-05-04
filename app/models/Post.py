from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, select
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from urllib.parse import urlparse

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    user = relationship('User')
    comments = relationship('Comment', cascade='all,delete')
    votes = relationship('Vote', cascade='all,delete')
    
    @hybrid_property
    def vote_count(self):
        return len([vote for vote in self.votes if vote.post_id == self.id])

    @vote_count.expression
    def vote_count(cls):
        return (
            select([func.count()])
            .where(Vote.post_id == cls.id)
            .label('vote_count')
        )

    @property
    def shortened_url(self):
        parsed_url = urlparse(self.post_url)
        return parsed_url.netloc
    
    @property
    def formatted_created_at(self):
        return self.created_at.strftime("%d %b, %Y")  # Format the date as "04 May, 2024"
