def create_classes(db):
    class News(db.Model):
        __tablename__ = 'news_df'

        id = db.Column(db.Integer, primary_key=True)
        topic = db.Column(db.String)
        news_date = db.Column(db.Date)
        label = db.Column(db.Numeric)
        combined_text = db.Column(db.String)

        def __repr__(self):
            return '<News %r>' % (self.id)
    return News
