import os
import argparse
import yt_dlp

def download_with_ytdlp(url, output_path):
    """유튜브 동영상을 yt-dlp를 사용하여 다운로드합니다.
    
    Args:
        url (str): 다운로드할 유튜브 동영상 URL
        output_path (str): 동영상을 저장할 디렉토리 경로
        
    Returns:
        bool: 다운로드 성공 여부
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # yt-dlp 옵션 설정
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'no_check_certificate': True,
        'force_ipv4': True
    }
    
    try:
        print("yt_dlp 라이브러리를 사용하여 다운로드 시도 중...")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("yt_dlp를 통한 다운로드 성공!")
        return True
    except Exception as e:
        print(f"yt_dlp 실행 중 오류 발생: {e}")
        return False

def main():
    """메인 함수: 커맨드 라인 인터페이스를 제공합니다."""
    parser = argparse.ArgumentParser(description="유튜브 동영상 다운로드 도구")
    parser.add_argument("-u", "--url", type=str, help="다운로드할 유튜브 URL")
    parser.add_argument("-o", "--output", type=str, default="./downloads", 
                        help="다운로드 저장 경로 (기본값: ./downloads)")
    
    args = parser.parse_args()
    
    # URL이 입력되지 않으면 기본 URL 사용
    if not args.url:
        print("URL이 제공되지 않았습니다. 기본 예제 URL을 사용합니다.")
        args.url = 'https://youtu.be/jNQXAC9IVRw?feature=shared'
    
    success = download_with_ytdlp(args.url, args.output)
    return 0 if success else 1

if __name__ == "__main__":
    main()