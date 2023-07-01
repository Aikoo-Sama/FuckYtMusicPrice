from ytmusicapi import YTMusic

yt = YTMusic("oauth.json")

def parse_history(history):
    parsed_results = []
    for item in history:
        if item is Ellipsis:
            continue

        video_id = item['videoId']
        title = item['title']
        artists = [artist['name'] for artist in item['artists']]
        album = item['album']['name'] if item['album'] else None
        like_status = item['likeStatus']
        thumbnails = [thumbnail['url'] for thumbnail in item['thumbnails']]
        duration = item['duration']
        duration_seconds = item['duration_seconds']
        played = item['played']

        parsed_item = {
            'video_id': video_id,
            'title': title,
            'artists': artists,
            'album': album,
            'like_status': like_status,
            'thumbnails': thumbnails,
            'duration': duration,
            'duration_seconds': duration_seconds,
            'played': played
        }

        parsed_results.append(parsed_item)

    return parsed_results

parsed_history = parse_history(yt.get_history())

# Afficher les résultats
for item in parsed_history:
    print('Video ID:', item['video_id'])
    print('Title:', item['title'])
    print('Artists:', ', '.join(item['artists']))
    print('Album:', item['album'])
    print('Like Status:', item['like_status'])
    print('Thumbnails:', ', '.join(item['thumbnails']))
    print('Duration:', item['duration'])
    print('Duration (seconds):', item['duration_seconds'])
    print('Played:', item['played'])
    print('---')
