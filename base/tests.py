from django.test import TestCase
from .models import User, Topic, Room, Message


class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@example.com', username='testuser')

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.username, 'testuser')


class TopicModelTestCase(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name='Test Topic')

    def test_topic_creation(self):
        self.assertEqual(Topic.objects.count(), 1)
        self.assertEqual(self.topic.name, 'Test Topic')


class RoomModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@example.com', username='testuser')
        self.topic = Topic.objects.create(name='Test Topic')
        self.room = Room.objects.create(host=self.user, topic=self.topic, name='Test Room')

    def test_room_creation(self):
        self.assertEqual(Room.objects.count(), 1)
        self.assertEqual(self.room.host, self.user)
        self.assertEqual(self.room.topic, self.topic)
        self.assertEqual(self.room.name, 'Test Room')


class MessageModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@example.com', username='testuser')
        self.topic = Topic.objects.create(name='Test Topic')
        self.room = Room.objects.create(host=self.user, topic=self.topic, name='Test Room')
        self.message = Message.objects.create(user=self.user, room=self.room, body='Test Message')

    def test_message_creation(self):
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(self.message.user, self.user)
        self.assertEqual(self.message.room, self.room)
        self.assertEqual(self.message.body, 'Test Message')
