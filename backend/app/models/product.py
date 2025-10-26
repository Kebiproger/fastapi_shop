from sqlalchemy import Column, Integer,String, Float, ForeignKey,DateTime, Text
from sqlalchemy.orm import relationship
from ..database import Base
from datetime import datetime

class Product(Base):
    __tablename__= "products"
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String, nullable=False, index=True)
    descriptin = Column(Text)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"),nullable=False)
    image_url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    category = relationship("Category", back_populates="products")
    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price}, category_id={self.category_id})>"