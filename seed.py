from app import create_app
from app.models import db, Episode, Guest, Appearance

app = create_app()

def seed_database():
    with app.app_context():
        print("🌱 Seeding database...")
        
        # Clear existing data
        print("Clearing existing data...")
        Appearance.query.delete()
        Episode.query.delete()
        Guest.query.delete()
        
        # Create episodes
        print("Creating episodes...")
        e1 = Episode(date="1/11/99", number=1)
        e2 = Episode(date="1/12/99", number=2)
        
        # Create guests
        print("Creating guests...")
        g1 = Guest(name="Michael J. Fox", occupation="actor")
        g2 = Guest(name="Sandra Bernhard", occupation="Comedian")
        g3 = Guest(name="Tracey Ullman", occupation="television actress")
        
        # Add to session
        db.session.add_all([e1, e2, g1, g2, g3])
        db.session.commit()
        
        # Create appearances
        print("Creating appearances...")
        a1 = Appearance(rating=4, episode=e1, guest=g1)
        a2 = Appearance(rating=5, episode=e2, guest=g3)
        
        db.session.add_all([a1, a2])
        db.session.commit()
        
        print("✅ Done seeding!")

if __name__ == "__main__":
    seed_database()