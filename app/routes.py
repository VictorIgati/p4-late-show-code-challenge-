from flask import Blueprint, jsonify, request
from app.models import db, Episode, Guest, Appearance

api = Blueprint('api', __name__)

@api.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        'id': episode.id,
        'date': episode.date,
        'number': episode.number
    } for episode in episodes])

@api.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404
    return jsonify(episode.to_dict(rules=('appearances', 'appearances.guest')))

@api.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{
        'id': guest.id,
        'name': guest.name,
        'occupation': guest.occupation
    } for guest in guests])

@api.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        new_appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        db.session.add(new_appearance)
        db.session.commit()
        return jsonify(new_appearance.to_dict(
            rules=('episode', 'guest', '-episode.appearances', '-guest.appearances')
        )), 201
    except (ValueError, KeyError) as e:
        return jsonify({'errors': [str(e)]}), 400