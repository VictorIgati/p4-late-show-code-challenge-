# Late Show API

A Flask API for tracking guests and their appearances on the Late Show.

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pipenv install
```

3. Setup the database:
```bash
export FLASK_APP=app
flask db upgrade
python seed.py
```

4. Start the server:
```bash
python run.py
```

## API Endpoints

### GET /episodes
Returns a list of all episodes with their dates and numbers.

### GET /episodes/:id
Returns a specific episode with its guest appearances.

### GET /guests
Returns a list of all guests with their occupations.

### POST /appearances
Creates a new appearance with the following required fields:
- rating (1-5)
- episode_id
- guest_id

## Models

### Episode
- date: string
- number: integer
- has many guests through appearances

### Guest
- name: string
- occupation: string
- has many episodes through appearances

### Appearance
- rating: integer (1-5)
- belongs to episode
- belongs to guest

## Validation
- Appearance ratings must be between 1 and 5 inclusive