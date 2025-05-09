# youtube-scraping


유튜브 동영상을 다운로드하기 위한 파이썬 기반 스크래퍼입니다.

## 설치 방법

1. 저장소 복제:

```bash
git clone https://github.com/allenkang92/youtube-scraping.git
cd youtube-scraping
```

2. 필요한 패키지 설치:

```bash
pip install -r requirements.txt
```

## 사용 방법

### 기본 사용법

```bash
python youtube_scraping.py -u "유튜브_URL"
```

### 예시

```bash
# 기본 경로(./downloads)에 저장
python youtube_scraping.py -u "https://youtu.be/xoS8WZOKk6w"

# 지정된 경로에 저장
python youtube_scraping.py -u "https://youtu.be/xoS8WZOKk6w" -o "./my_videos"
```

### 명령어 옵션

| 옵션 | 설명 |
|------|------|
| `-u, --url` | 다운로드할 유튜브 동영상 URL |
| `-o, --output` | 다운로드한 파일을 저장할 경로 (기본값: ./downloads) |

## 요구 사항

- Python 3.6 이상
- yt-dlp 라이브러리