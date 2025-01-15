import pytest
from api.models import Post


@pytest.mark.django_db
def test_post_str():
    post=Post.objects.create(
        title="Sample post",
        author="Safuan Alam Saifee",
        slug="sample-post"
    )

    print(str(post)) 
    assert str(post) == "Sample post"