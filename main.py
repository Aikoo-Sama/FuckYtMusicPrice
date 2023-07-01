from ytmusicapi import YTMusic
import datetime

yt = YTMusic("oauth.json")
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
this_month = ["Today", "Yesterday", "This week", "This month", "Last week", "Last month"]

def parse_date(strr):
    if strr in this_month:
        today = datetime.date.today()
        if strr == "Last week":
            last_week = today - datetime.timedelta(days=7)
            return (last_week.month, last_week.year)
        elif strr == "Last month":
            last_month = today - datetime.timedelta(days=30)
            return (last_month.month, last_month.year)
        elif strr == "This week":
            return (today.month, today.year)
        elif strr == "This month":
            return (today.month, today.year)
        elif strr == "Today":
            return (today.month, today.year)
        elif strr == "Yesterday":
            yesterday = today - datetime.timedelta(days=1)
            return (yesterday.month, yesterday.year)
    elif strr.split(' ')[0] in month:
        month_str, year_str = strr.split(' ')
        month_int = month.index(month_str) + 1
        year_int = int(year_str)

        return (month_int, year_int)
    elif strr == "This Year":
        today = datetime.date.today()
        return (today.month, today.year)
    elif strr == "Last Year":
        today = datetime.date.today()
        last_year = today - datetime.timedelta(days=365)
        return (last_year.month, last_year.year)

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

def print_info(parsed_history):
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

def format_dhms(seconds):
    days = seconds // (24 * 3600)
    hours = (seconds % (24 * 3600)) // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    result = ""
    if days > 0:
        result += f"{days} jour(s), "
    if hours > 0:
        result += f"{hours} heure(s), "
    if minutes > 0:
        result += f"{minutes} minute(s), "
    result += f"{remaining_seconds} seconde(s)"

    return result

def get_stats(parsed_history, history_json = {}):
    for item in parsed_history:
        date = item['played']
        date_tuple = parse_date(date)
        duration_seconds = item['duration_seconds']

        if date_tuple[1] not in history_json:
            history_json[date_tuple[1]] = {}

        if date_tuple[0] not in history_json[date_tuple[1]]:
            history_json[date_tuple[1]][date_tuple[0]] = 0

        history_json[date_tuple[1]][date_tuple[0]] += duration_seconds

    return history_json

def print_stats(history_json):
    print("History stats:")
    for year in history_json:
        print(f"Year {year}:")
        seconds = 0
        for month_val in history_json[year]:
            month_name = month[month_val - 1]
            seconds += history_json[year][month_val]
            print(f"\tMonth {month_name}: {format_dhms(history_json[year][month_val])}")
        print(f"\tTotal: {format_dhms(seconds)}")
        print()

if __name__ == "__main__":
    history = yt.get_history()
    parsed_history = parse_history(history)
    print_info(parsed_history)
    print_stats(get_stats(parsed_history))
