# LibraryProject

## Introduction
This project is part of the *Introduction to Django* learning task. It sets up a basic Django development environment and creates a new project named *LibraryProject*.

## Setup Instructions

### 1. Install Django
```bash
pip install django

# Django Permissions and Groups Setup

## Custom Permissions
The Book model defines four custom permissions:
- can_view → view book list/details
- can_create → create new books
- can_edit → edit existing books
- can_delete → delete books

## Groups
Three groups are created via setup_groups command:
- *Viewers* → can_view
- *Editors* → can_view, can_create, can_edit
- *Admins* → all permissions

## Usage
Run:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py setup_groups