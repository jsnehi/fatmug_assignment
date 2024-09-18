### Video Upload and Processing Web Application
This is a Django-based web application that allows users to upload videos, extract subtitles using ffmpeg, search for phrases within the subtitles, and play the video from the point where the searched phrase occurs. The project aims to provide seamless video processing and subtitle management functionality.

## Table of Contents
  * Features
  * Tech Stack
  * Installation
  * Usage

## Features
  * Video Upload: Users can upload video files through the web interface.
  * Subtitle Extraction: Subtitles are extracted from uploaded videos using ffmpeg and stored in the database.
  * Search Functionality: Users can search for specific phrases within the subtitles and see the corresponding timestamps.
  * Play from Timestamp: Users can click on the timestamp and play the video from that point.
  * Video List View: A list of all uploaded videos is displayed, allowing users to select and interact with any video.
  * Closed Captions: The subtitles are displayed as closed captions during video playback.

## Tech Stack
  * Backend: Django (Python)
  * Frontend: HTML, CSS, JavaScript
  * Database: PostgreSQL
  * Subtitle Extraction: ffmpeg
  * Storage: Django Media Files

## Installation
To get this project running locally, follow these steps:

# Prerequisites
  * Python 3.8+
  * PostgreSQL
  * ffmpeg (for subtitle extraction)
  * Git

# Steps
  1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
  
  2. Create a virtual environment:

  ```bash
  python -m venv venv
  ```
    
  3. Activate the virtual environment:
  On Windows:

   ```bash
   venv\Scripts\activate
   ```
      
  On macOS/Linux:
    
   ```bash
   source venv/bin/activate
   ```
      
  4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

  5. Install ffmpeg
  Download and install ffmpeg from here. Make sure it's accessible from your system's PATH.

  6. Set up PostgreSQL database:

  * Create a PostgreSQL database named video_db.
  * Configure database settings in settings.py:
  ```bash
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'video_db',
          'USER': 'your_db_user',
          'PASSWORD': 'your_db_password',
          'HOST': 'localhost',
          'PORT': '5432',
      }
  }
  ```

  7. Run database migrations
  ```bash
  python manage.py migrate
  ```

  8. Create a superuser
  ```bash
  python manage.py createsuperuser
  ```

  9. Run the development server
  ```bash
  python manage.py runserver
  ```

  10. Access the application
  Open http://127.0.0.1:8000/ in your browser to access the app.

## Usage

* Video Upload
  * Go to the "Upload Video" page.
  * Select and upload a video file.
  * The system will process the video and extract subtitles.
* Search in Subtitles
  * Go to the "Uploaded Videos" page and select a video.
  * Use the search bar to search for specific phrases within the video’s subtitles.
  * Results will display the timestamps where the phrase occurs. Clicking on the timestamp will play the video from that point.
* List of Videos
  * Navigate to the "Uploaded Videos" page to see a list of all the uploaded videos.
