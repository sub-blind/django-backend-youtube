from django.test import TestCase
from rest_framework.test import APITestCase
from users.models import User
from .models import Video
from django.urls import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.
class VideoAPITestCasse(TestCase):

    # 테스트 코드 실행 전 동작하는 함수
    # - 데이터를 만들어줘야 함. (1) 유저 생성
    def setUp(self):
        self.user = User.objects.create_user(email="jaeseop@gmail.com", password="1234")
        self.client.login(email="jaeseop@gmail.com", password="1234")

        self.Video = Video.objects.create(
            title="test video",
            link="http://www.test.com",
            user=self.user,
        )

    def test_video_list_get(self):
        url = reverse("video-list")
        res = self.client.get(url)  # 전체 비디오 조회 데이터

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.headers["Content-Type"], "application/json")
        self.assertTrue(len(res.data) > 0)

        for video in res.data:
            self.assertIn("title", video)

    def test_video_list_post(self):
        url = reverse("video-list")  # api/v1/video

        data = {
            "title": "test video2",
            "link": "http://test.com",
            "category": "test category",
            "thumbnail": "http://test.com",
            "video_file": SimpleUploadedFile("file.mp4", b"file_content", "video/mp4"),
            "user": self.user.pk,
        }

        res = self.client.post(url, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data["title"], "test video2")

    def test_video_detail_get(self):
        pass

    def test_video_detail_put(self):
        pass

    def test_video_detail_delete(self):
        pass
