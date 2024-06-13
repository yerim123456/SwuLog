import json
import urllib.request
import urllib.parse
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_search(request):
    if request.method == 'GET':
        # 클라이언트 ID와 시크릿을 settings.py에서 로드
        client_id = settings.NAVER_CLIENT_ID
        client_secret = settings.NAVER_CLIENT_SECRET
        query = request.GET.get('q', '검색할 단어')
        encText = urllib.parse.quote(query)
        url = "https://openapi.naver.com/v1/search/blog?query=" + encText  # JSON 결과
        api_request = urllib.request.Request(url)
        api_request.add_header("X-Naver-Client-Id", client_id)
        api_request.add_header("X-Naver-Client-Secret", client_secret)
        try:
            response = urllib.request.urlopen(api_request)
            rescode = response.getcode()
            if rescode == 200:
                response_body = response.read()
                result = json.loads(response_body.decode('utf-8'))

                items = result.get('items', [])
                processed_data = []
                for item in items:
                    processed_data.append({
                        'title': item.get('title', ''),
                        'link': item.get('link', ''),
                        'postdate': item.get('postdate', '')
                    }) #이렇게 설정했는데도 안됨. api를 불러오는 과정에서 수정은 따로 안 되는듯.

                return JsonResponse(result)
            else:
                return JsonResponse({"error": f"Error Code: {rescode}"}, status=rescode)
        except urllib.error.HTTPError as e:
            return JsonResponse({"error": f"HTTP Error: {e.code}"}, status=e.code)
        except urllib.error.URLError as e:
            return JsonResponse({"error": f"URL Error: {e.reason}"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
