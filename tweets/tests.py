from rest_framework.test import APITestCase
from users.models import User
from tweets.models import Tweet


class TestTweets(APITestCase):

    USERNAME = "test-username"
    PAYLOAD = "This is test tweet."
    URL = "/api/v1/tweets/"

    def setUp(self):
        self.user = User.objects.create(
            name=self.USERNAME,
        )
        Tweet.objects.create(
            payload=self.PAYLOAD,
            user=self.user,
        )

    def test_all_tweets(self):
        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )
        self.assertIsInstance(
            data,
            list,
            "Data isn't a list.",
        )
        self.assertEqual(
            len(data),
            1,
            "Length isn't 1.",
        )
        self.assertEqual(
            data[0]["user"],
            self.user.pk,
            "User isn't correct.",
        )

        self.assertEqual(
            data[0]["payload"],
            self.PAYLOAD,
            "Payload isn't correct.",
        )
        self.assertEqual(
            data[0]["total_likes_count"],
            0,
            "Like count isn't 0.",
        )

    def test_create_tweet(self):
        new_payload = "New payload for testing"

        self.client.force_login(
            self.user,
        )

        response = self.client.post(
            self.URL,
            data={"payload": new_payload},
        )
        data = response.json()

        self.assertEqual(
            response.status_code,
            201,
            "Not 201 status code",
        )
        self.assertEqual(
            data["user"],
            self.user.pk,
        )
        self.assertEqual(
            data["payload"],
            new_payload,
            "Payload isn't correct.",
        )
        self.assertEqual(
            data["total_likes_count"],
            0,
            "Like count isn't 0.",
        )

    def test_create_tweet_invalid_payload(self):
        self.client.force_login(self.user)
        response = self.client.post(self.URL, data={"payload": ""})

        self.assertEqual(response.status_code, 400, "Not 400 status code")


class TestTweetDetail(APITestCase):

    USERNAME = "test-username"
    PAYLOAD = "This is test tweet."
    TEST_URL = "/api/v1/tweets/1"
    NOT_FOUND_URL = "/api/v1/tweets/999"

    def setUp(self):
        self.user = User.objects.create(
            username=self.USERNAME,
        )
        self.tweet = Tweet.objects.create(
            payload=self.PAYLOAD,
            user=self.user,
        )

    def test_get_tweet(self):
        response = self.client.get(self.TEST_URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )

        data = response.json()

        self.assertEqual(
            data["user"],
            self.user.pk,
            "User isn't correct.",
        )
        self.assertEqual(
            data["payload"],
            self.PAYLOAD,
            "Payload isn't correct.",
        )
        self.assertEqual(
            data["total_likes_count"],
            0,
            "Like count isn't 0.",
        )

    def test_put_tweet(self):
        new_payload = "Update test Payload"

        self.client.force_login(
            self.user,
        )

        response = self.client.put(
            self.TEST_URL,
            data={"payload": new_payload},
        )
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertEqual(
            data["user"],
            self.user.pk,
            "User isn't correct.",
        )
        self.assertEqual(
            data["payload"],
            new_payload,
            "Payload isn't correct.",
        )
        self.assertEqual(
            data["total_likes_count"],
            0,
            "Like count isn't 0.",
        )

    def test_delete_tweet(self):
        self.client.force_login(
            self.user,
        )
        response = self.client.delete(
            self.TEST_URL,
        )

        self.assertEqual(
            response.status_code,
            204,
            "Not 204 status code",
        )

    def test_get_tweet_not_found(self):
        response = self.client.get(
            self.NOT_FOUND_URL,
        )

        self.assertEqual(
            response.status_code,
            404,
            "Not 404 status code",
        )

    def test_update_tweet_not_owner(self):
        other_user = User.objects.create(
            username="other_user",
        )
        self.client.force_login(
            other_user,
        )

        response = self.client.put(
            self.TEST_URL,
            data={"payload": "New payload"},
        )

        self.assertEqual(
            response.status_code,
            403,
            "Not 403 status code",
        )

    def test_delete_tweet_not_owner(self):
        other_user = User.objects.create(
            username="other_user",
        )
        self.client.force_login(
            other_user,
        )

        response = self.client.delete(
            self.TEST_URL,
        )

        self.assertEqual(
            response.status_code,
            403,
            "Not 403 status code",
        )
