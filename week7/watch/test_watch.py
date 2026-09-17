import pytest
from watch import parse

# 合法案例
@pytest.mark.parametrize("html, expected", [
    # 1. 傳統 Embed (HTTP + www)
    ('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>', 'https://youtu.be/xvFZjo5PgG0'),
    # 2. 傳統 Embed (HTTPS + 無 www)
    ('<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>', 'https://youtu.be/xvFZjo5PgG0'),
    # 3. 傳統 Embed (HTTPS + www + 包含一堆額外屬性)
    ('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allowfullscreen></iframe>', 'https://youtu.be/xvFZjo5PgG0'),
    # 4. 短網址 (youtu.be)
    ('<iframe src="https://youtu.be/xvFZjo5PgG0"></iframe>', 'https://youtu.be/xvFZjo5PgG0'),
    # 5. 短片型 (Shorts)
    ('<iframe src="https://www.youtube.com/shorts/abc123XYZ-_"></iframe>', 'https://youtu.be/abc123XYZ-_'),
    # 6. 標準觀看頁 (Watch Page)
    ('<iframe src="https://www.youtube.com/watch?v=xvFZjo5PgG0"></iframe>', 'https://youtu.be/xvFZjo5PgG0'),
])
def test_success(html, expected):
    assert parse(html) == expected

# 非法案例
@pytest.mark.parametrize("html, expected", [
    # 1. 非 YouTube 網址 (如 CS50 官網)
    ('<iframe src="https://cs50.harvard.edu/python"></iframe>', None),
    # 2. 完全不相干的網站
    ('<iframe src="https://www.google.com"></iframe>', None),
    # 3. 雖然是 youtube 網址，但路徑不合法 (invalid)
    ('<iframe src="https://www.youtube.com/invalid/xvFZjo5PgG0"></iframe>', None),
    # 4. 不是 iframe 標籤 (例如用 img 標籤包裝)
    ('<img src="https://www.youtube.com/embed/xvFZjo5PgG0">', None),
    # 5. 只是純文字，沒有 HTML 標籤
    ('just a random string without html', None),
    # 6. 空字串
    ('', None),
    # 7. 缺少網址雙引號包覆的異常情況
    ('<iframe src=https://www.youtube.com/embed/xvFZjo5PgG0></iframe>', None),
])
def test_fail(html, expected):
    assert parse(html) == expected