# Django Publication API

This project implements a Django API for managing publications. The API includes features such as adding publications, viewing the latest and top-rated publications, and voting for publications. Below are the instructions for setting up the virtual environment and installing the dependencies.

## Setup

1.  **Clone the Repository:**    
    `git clone <repository_url>
    cd django-publication-api` 
    
2.  **Create and Activate Virtual Environment:**
 `python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate` 
    
3.  **Install Dependencies:**
 `pip install -r requirements.txt` 
    

## Database Migration
`python manage.py migrate` 

## Run the Development Server
`python manage.py runserver` 

The API will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## API Endpoints

-   **Add Publication:**
    
    `POST /api/publication/create/`
    
-   **Get Latest Publications:**
    
    `GET /api/publication?order_by=latest`
    
-   **Get Top-Rated Publications:**
    
    `GET /api/publication?order_by=top_rated`
    
-   **Vote for a Publication:**
    
    `POST /api/publication/vote/`
    
    Send JSON data with `publication` (publication ID), `value` ('like', 'dislike', 'revoke').
    

## Rules and Restrictions

-   Only authenticated users can create publications and vote.
-   Users cannot vote for the same publication twice. They can change their vote or revoke it.
-   The publication data includes text, publication date, author, number of votes, and rating.
