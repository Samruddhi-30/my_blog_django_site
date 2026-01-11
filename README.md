** Sam's Blog - Django Web Application

A feature-rich blog application built with Django, utilizing class-based views for clean and maintainable code architecture.

** Features

- **Home Page**: Displays the latest 3 blog posts
- **All Posts**: Browse through all published blog posts
- **Post Details**: View individual posts with full content
- **Commenting System**: Users can leave comments on blog posts
- **Read Later**: Save posts to read later using session-based storage
- **Author Information**: Display author details and post metadata
- **Responsive Design**: Clean UI with purple-themed styling

** Technology Stack

- **Framework**: Django (Python)
- **Architecture**: Class-Based Views (CBV)
- **Database**: SQLite (default, can be changed)
- **Session Management**: Django sessions for "Read Later" functionality

** Application Structure

**# Views (Class-Based)

** `home_page` (TemplateView)
- Displays the 3 most recent blog posts ordered by date
- Template: `blog/index.html`

** `AllPostsList` (ListView)
- Shows all blog posts in descending order by date
- Template: `blog/all-posts.html`
- Context object: `all_posts`

** `PostDetailed` (View)
- Handles both GET and POST requests for individual posts
- **GET**: Displays post details, comments, and comment form
- **POST**: Processes and saves new comments
- Implements "Read Later" functionality using sessions
- Template: `blog/post-detail.html`

** `ReadLaterView` (View)
- **GET**: Displays all saved posts from session storage
- **POST**: Adds or removes posts from "Read Later" list
- Template: `blog/stored-posts.html`

** Key Functionality

**# Session-Based "Read Later"
Posts are stored in the user's session using their post IDs. Users can:
- Add posts to their reading list
- Remove posts from the list
- View all saved posts on a dedicated page

**# Comment System
- Users can submit comments with username, email, and comment text
- Comments are associated with specific posts
- Comments are displayed in reverse chronological order (newest first)

** Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-blog.git
   cd django-blog
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

** Models

**# Post Model
- Title
- Slug (URL-friendly)
- Author (ForeignKey)
- Date
- Image
- Excerpt
- Content
- Tags (ManyToMany)

**# Comment Model
- User name
- Email
- Comment text
- Post (ForeignKey)
- Timestamp

** URL Structure

```
/                           # Home page with latest posts
/posts                      # All posts listing
/posts/<slug>              # Individual post detail
/read-later                # Saved posts
```

** Screenshots

**# Home Page
Landing page featuring the latest blog posts and author introduction.

**# Post Detail
Individual post view with full content, comments section, and "Read Later" functionality.

**# Comment Form
Interactive form for users to submit comments on posts.

**# Stored Posts
Personalized reading list with saved posts.

**# All Posts
Grid view of all published blog posts.

** Features in Detail

**# Read Later Functionality
- Session-based storage (no authentication required)
- Toggle posts in/out of reading list
- Persistent across browsing session
- Button changes text based on save status

**# Comments
- Simple form validation
- Auto-redirect after successful submission
- Display comment count
- Chronological ordering (newest first)

** Future Enhancements

- User authentication and profiles
- Categories and advanced filtering
- Search functionality
- Rich text editor for post creation
- Social sharing buttons
- Email notifications for new comments
- Pagination for posts and comments

** Contact

Sam - https://github.com/Samruddhi-30

** Acknowledgments

- Django Documentation
- Django Class-Based Views
- Bootstrap/CSS Framework (if used)
- Lorem Ipsum content for testing