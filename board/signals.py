from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from board.models import ContactItem, TaskItem
from datetime import date, timedelta

@receiver(post_save, sender=User)
def create_default_contacts(sender, instance, created, **kwargs):
    if created:
        # Predefined Contacts
        ContactItem.objects.create(user=instance, name="Anna Müller", mail="anna.mueller@example.com", phone="015123456789", isChoosen = False)
        ContactItem.objects.create(user=instance, name="Peter Schmidt", mail="peter.schmidt@example.com", phone="017234567890", isChoosen = False)
        ContactItem.objects.create(user=instance, name="Laura Fischer", mail="laura.fischer@example.com", phone="016345678901", isChoosen = False)
        ContactItem.objects.create(user=instance, name="Markus Weber", mail="markus.weber@example.com", phone="017987654321", isChoosen = False)
        ContactItem.objects.create(user=instance, name="Sabine Becker", mail="sabine.becker@example.com", phone="015678901234", isChoosen = False)
        ContactItem.objects.create(user=instance, name="Thomas Wagner", mail="thomas.wagner@example.com", phone="016789012345", isChoosen = False)

        # Predefined Tasks
        TaskItem.objects.create(
            user=instance,
            taskTitle="Design Homepage Layout",
            taskDescription="Create an initial layout design for the homepage, focusing on user experience.",
            taskDueDate=date.today() + timedelta(days=5),
            selectedCategory="User Story",
            prio="urgent",
            subtasks=[
                {"subTaskInput": "Sketch wireframes", "id": 0, "isActive": True},
                {"subTaskInput": "Review with team", "id": 1, "isActive": False},
                {"subTaskInput": "Finalize design", "id": 2, "isActive": True}
            ],
            selectedContacts=[
                {"name": "Anna Müller", "color": "", "selectedContactsId": 0},
                {"name": "Peter Schmidt", "color": "", "selectedContactsId": 1}
            ],
            currentState="inProgress"
        )
        TaskItem.objects.create(
            user=instance,
            taskTitle="Develop Contact Form Functionality",
            taskDescription="Implement the backend logic for the website’s contact form.",
            taskDueDate=date.today() + timedelta(days=10),
            selectedCategory="Technical Task",
            prio="medium",
            subtasks=[
                {"subTaskInput": "Set up form validation", "id": 0, "isActive": True},
                {"subTaskInput": "Implement form submission", "id": 1, "isActive": False}
            ],
            selectedContacts=[
                {"name": "Laura Fischer", "color": "", "selectedContactsId": 0},
                {"name": "Markus Weber", "color": "", "selectedContactsId": 1}
            ],
            currentState="toDo"
        )
        TaskItem.objects.create(
            user=instance,
            taskTitle="Optimize Images for Web",
            taskDescription="Optimize all images on the website to improve loading times.",
            taskDueDate=date.today() + timedelta(days=7),
            selectedCategory="Technical Task",
            prio="low",
            subtasks=[
                {"subTaskInput": "Compress images", "id": 0, "isActive": True},
                {"subTaskInput": "Replace existing images", "id": 1, "isActive": True},
                {"subTaskInput": "Test loading times", "id": 2, "isActive": True}
            ],
            selectedContacts=[
                {"name": "Markus Weber", "color": "", "selectedContactsId": 0},
                {"name": "Sabine Becker", "color": "", "selectedContactsId": 1}
            ],
            currentState="awaitFeedback"
        )
        TaskItem.objects.create(
            user=instance,
            taskTitle="Create User Personas",
            taskDescription="Develop detailed user personas to guide the design process.",
            taskDueDate=date.today() + timedelta(days=14),
            selectedCategory="User Story",
            prio="medium",
            subtasks=[
                {"subTaskInput": "Research target audience", "id": 0, "isActive": True},
                {"subTaskInput": "Draft personas", "id": 1, "isActive": False},
                {"subTaskInput": "Review personas with team", "id": 2, "isActive": False},
                {"subTaskInput": "Finalize personas", "id": 3, "isActive": True}
            ],
            selectedContacts=[
                {"name": "Sabine Becker", "color": "", "selectedContactsId": 0},
                {"name": "Thomas Wagner", "color": "", "selectedContactsId": 1}
            ],
            currentState="toDo"
        )
        TaskItem.objects.create(
            user=instance,
            taskTitle="Setup Hosting Environment",
            taskDescription="Configure the hosting environment for the new website, including SSL and security settings.",
            taskDueDate=date.today() + timedelta(days=12),
            selectedCategory="Technical Task",
            prio="urgent",
            subtasks=[
                {"subTaskInput": "Set up server", "id": 0, "isActive": False},
                {"subTaskInput": "Install SSL certificate", "id": 1, "isActive": True},
                {"subTaskInput": "Configure firewall", "id": 2, "isActive": False}
            ],
            selectedContacts=[
                {"name": "Thomas Wagner", "color": "", "selectedContactsId": 0},
                {"name": "Anna Müller", "color": "", "selectedContactsId": 1}
            ],
            currentState="inProgress"
        )
        TaskItem.objects.create(
            user=instance,
            taskTitle="Test User Flow on Mobile Devices",
            taskDescription="Test the entire user flow on various mobile devices to ensure responsiveness.",
            taskDueDate=date.today() + timedelta(days=9),
            selectedCategory="User Story",
            prio="urgent",
            subtasks=[
                {"subTaskInput": "Test on iOS", "id": 0, "isActive": True},
                {"subTaskInput": "Test on Android", "id": 1, "isActive": True},
                {"subTaskInput": "Test on Windows Phone", "id": 2, "isActive": True}
            ],
            selectedContacts=[
                {"name": "Anna Müller", "color": "", "selectedContactsId": 0},
                {"name": "Peter Schmidt", "color": "", "selectedContactsId": 1},
                {"name": "Laura Fischer", "color": "", "selectedContactsId": 2},
                {"name": "Markus Weber", "color": "", "selectedContactsId": 3},
                {"name": "Sabine Becker", "color": "", "selectedContactsId": 4}
            ],
            currentState="done"
        )

        
