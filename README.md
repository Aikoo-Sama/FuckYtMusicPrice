# FuckYtMusicPrice

Or how to fuck the excessive prices of Youtube subscriptions

## 🌞 Preview

![Preview](screen.png)

## 🍀 Installation

### Requirements

- Python 3.0 or higher
- pip

### Install

```bash
git clone
cd YTMusic-Tracker
pip3 install ytmusicapi
ytmusicapi oauth ## From https://ytmusicapi.readthedocs.io
```

If you can't run ytmusicapi, try to run this python script in the project folder:
```py
import ytmusicapi
ytmusicapi.setup_oauth("oauth.json")
```

## ❤️ Usage

```bash
python3 main.py
```

## 📝 Todo

- [ ] Add a GUI
- [ ] Add a way to export data
- [ ] Add a way to import data
- [ ] Add a way to see the data in a web browser
- [ ] Add a way to see the data in a mobile app
- [ ] Fix issue: After 7 days, data is not saved anymore, so we need to store the data in a file

## License

[MIT](https://choosealicense.com/licenses/mit/)
