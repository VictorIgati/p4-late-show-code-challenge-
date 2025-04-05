# Late Show API

A Flask API for tracking guests and their appearances on the Late Show. This API allows you to manage episodes, guests, and their appearances with ratings.

## Table of Contents
- [Late Show API](#late-show-api)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Database Setup](#database-setup)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
    - [GET /episodes](#get-episodes)
    - [GET /episodes/:id](#get-episodesid)
    - [GET /guests](#get-guests)
    - [POST /appearances](#post-appearances)
  - [Models](#models)
    - [Episode](#episode)
    - [Guest](#guest)
    - [Appearance](#appearance)
  - [Validation Rules](#validation-rules)
  - [Testing](#testing)
  - [Error Handling](#error-handling)
  - [Author](#author)

## Requirements
- Python 3.8+
- Pipenv
- SQLite3

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd lateshow-your-name
```

2. Install dependencies using Pipenv:
```bash
pipenv install
```

3. Activate the virtual environment:
```bash
pipenv shell
```

## Database Setup

1. Set the Flask application environment:
```bash
export FLASK_APP=app
export FLASK_ENV=development
```

2. Initialize the database:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

3. Seed the database with sample data:
```bash
python seed.py
```

## Running the Application

1. Start the Flask server:
```bash
python run.py
```

2. The server will start at `http://localhost:5555`

## API Endpoints

### GET /episodes
Returns all episodes in the format:
```json
[
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  }
]
```

### GET /episodes/:id
Returns a specific episode with its appearances:
```json
{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "episode_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      },
      "guest_id": 1,
      "id": 1,
      "rating": 4
    }
  ]
}
```

### GET /guests
Returns all guests:
```json
[
  {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  }
]
```

### POST /appearances
Create a new appearance:

Request body:
```json
{
  "rating": 5,
  "episode_id": 1,
  "guest_id": 1
}
```

## Models

### Episode
- `id`: Integer, primary key
- `date`: String
- `number`: Integer
- Relationship: Has many guests through appearances

### Guest
- `id`: Integer, primary key
- `name`: String
- `occupation`: String
- Relationship: Has many episodes through appearances

### Appearance
- `id`: Integer, primary key
- `rating`: Integer (1-5)
- `episode_id`: Integer, foreign key
- `guest_id`: Integer, foreign key
- Relationships: 
  - Belongs to episode
  - Belongs to guest

## Validation Rules
- Appearance ratings must be between 1 and 5 inclusive

## Testing

1. Import the provided Postman collection:
   - Open Postman
   - Click "Import"
   - Select the `challenge-4-lateshow.postman_collection.json` file

2. Test endpoints:
   - Ensure the server is running
   - Execute the requests in the collection
   - Verify responses match the expected formats

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Successful GET request
- 201: Successful POST request
- 404: Resource not found
- 400: Invalid request data

## Author
Victor Igati