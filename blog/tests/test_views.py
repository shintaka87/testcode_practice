from django.test import TestCase
from django.urls import reverse

from ..models import Post

class IndexTests(TestCase):
  """IndexViewのテストクラス"""

  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('blog:index'))
    self.assertEqual(response.status_code, 200)