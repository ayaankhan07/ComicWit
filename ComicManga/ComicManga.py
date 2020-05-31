import urllib.request
import re

class Manga():
    def __init__(self, *manga_data):
        self.manga_data = manga_data
        self.show_name = ""
    @staticmethod
    def latest_manga():
        html_data = urllib.request.urlopen(urllib.request.Request("https://manganelo.com", headers={'User-Agent': 'Mozilla/5.0'})).read().decode("utf8")
        latest_links_show = re.findall('class="tooltip item-img" rel="nofollow" href="(.*?)"', html_data)
        latest_show_links = []
        for row in latest_links_show:
            row += "6969"
            link = re.findall("/manga/(.*?)6969", row)
            latest_show_links.append(link[0])
        latest_show_names = re.findall('onerror="javascript:this.src=\'https://manganelo.com/themes/hm/images/404_not_found.png\';" alt="(.*?)" />', html_data)[25:81]
        latest_show_photos = re.findall('<img class="img-loading" src="(.*?)"', html_data)[26:82]
        manga = []
        for row in range(len(latest_show_photos)):
            manga_data = {}
            manga_data["link"] = latest_show_links[row]
            manga_data["name"] = latest_show_names[row]
            manga_data["photo"] = latest_show_photos[row]
            manga.append(manga_data)
        return manga
    def search_manga(self):
        manga_data = self.manga_data
        if len(manga_data) == 2:
            manga_data = manga_data[1]
        elif len(manga_data) == 1:
            manga_data = manga_data[0]
        manga_data = manga_data.lower()
        if len(manga_data.split()) == 2:
            manga_data = manga_data.split()[0] + "_" + manga_data.split()[1]
        if len(manga_data.split()) == 3:
            manga_data = manga_data.split()[0] + "_" + manga_data.split()[1] + "_" + manga_data.split()[2]
        if len(manga_data.split()) == 4:
            manga_data = manga_data.split()[0] + "_" + manga_data.split()[1] + "_" + manga_data.split()[2] + "_" + \
                         manga_data.split()[3]
        html_data = urllib.request.urlopen(
            urllib.request.Request("https://manganelo.com/search/"+ manga_data, headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
            "utf8")
        links_show = re.findall('<a class="item-img" rel="nofollow" href="(.*?)"', html_data)
        show_links = []
        for row in links_show:
            row += "6969"
            link = re.findall("/manga/(.*?)6969", row)
            show_links.append(link[0])
        show_images = re.findall('<img class="img-loading" src="(.*?)"',html_data)[25:]
        show_names = re.findall('onerror="javascript:this.src=\'https://manganelo.com/themes/hm/images/404_not_found.png\';" alt="(.*?)"', html_data)[25:]
        manga = []
        for row in range(len(show_images)):
            manga_data = {}
            manga_data["name"] = show_names[row]
            manga_data["link"] = show_links[row]
            manga_data["photo"] = show_images[row]
            manga.append(manga_data)
        return manga
    def get_manga(self):
        manga_data = self.manga_data[0]
        if "https://manganelo.com/manga/" in manga_data:
            html_data = urllib.request.urlopen(
                urllib.request.Request(manga_data,
                                       headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
                "utf8")
        else:
            html_data = urllib.request.urlopen(
                urllib.request.Request("https://manganelo.com/manga/"+ manga_data,
                                       headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
                "utf8")
        show_name = re.findall("<h1>(.*?)</h1>", html_data)[0]
        self.show_name = show_name
        chapter_links = re.findall('<a rel="nofollow" class="chapter-name text-nowrap" href="(.*?)"', html_data)
        chapter_names = []
        for row in chapter_links:
            chapter_name = re.findall('<a rel="nofollow" class="chapter-name text-nowrap" href="'+ row +'" title="(.*?)"',html_data)[0]
            chapter_names.append(chapter_name)
        return chapter_names, chapter_links, show_name
    def get_manga_chapter(self, manga_chapter):
        manga_data = self.manga_data[0]
        html_data = urllib.request.urlopen(
            urllib.request.Request("https://manganelo.com/chapter/" + manga_data + "/chapter_" + str(manga_chapter),
                                   headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
            "utf8")
        chapter_images = re.findall('<img src="(.*?)"', html_data)[1:-1]
        return chapter_images
class Comic():
    def __init__(self, *comic_data):
        self.comic_data = comic_data
    @staticmethod
    def latest_comic():

        html_data = urllib.request.urlopen(
            urllib.request.Request("https://readcomicsonline.ru",
                                   headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
            "utf8")
        comic_names = re.findall('" class="chart-title"><strong>(.*?)</strong>', html_data)[20:45]
        comic_links = []
        links_comic = re.findall('<a href="(.*?)" class="chart-title"><strong>', html_data)[20:45]
        photos_comic = re.findall('<img width="100" src=\'(.*?)\' alt=\'', html_data)[:25]
        comic_photos = []
        for row in photos_comic:
            row = "http:" + row
            comic_photos.append(row)
        for row in links_comic:
            row += "code6969"
            link = re.findall("/comic/(.*?)code6969", row)
            comic_links.append(link)
        comic = []
        for row in range(len(comic_photos)):
            comic_data = {}
            comic_data["name"] = comic_names[row]
            comic_data["link"] = comic_links[row][0]
            comic_data["photo"] = comic_photos[row]
            comic.append(comic_data)
        return comic
    def search_comic(self):
        comic_data = self.comic_data
        if len(comic_data) == 2:
            comic_data = comic_data[1]
        elif len(comic_data) == 1:
            comic_data = comic_data[0]
        comic_data = comic_data.lower()
        if len(comic_data.split()) == 2:
            comic_data = comic_data.split()[0] + "-" + comic_data.split()[1]
        if len(comic_data.split()) == 3:
            comic_data = comic_data.split()[0] + "-" + comic_data.split()[1] + "-" + comic_data.split()[2]
        if len(comic_data.split()) == 4:
            comic_data = comic_data.split()[0] + "-" + comic_data.split()[1] + "-" + comic_data.split()[2] + "-" + \
                         comic_data.split()[3]
        html_data = urllib.request.urlopen(urllib.request.Request("https://readcomicsonline.ru/comic-list/tag/"+ comic_data,headers={'User-Agent': 'Mozilla/5.0'})).read().decode("utf8")
        comic_photos = re.findall('<img width="100" src=\'(.*?)\'', html_data)
        comic_links = []
        for row in comic_photos:
            row = re.findall('/manga/(.*?)/cover/', row)[0]
            comic_links.append(row)
        comic_names = re.findall('" class="chart-title"><strong>(.*?)</strong></a></h5>',html_data)
        comic = []
        for row in range(len(comic_photos)):
            comic_data = {}
            comic_data["name"] = comic_names[row]
            comic_data["link"] = comic_links[row]
            comic_data["photo"] = comic_photos[row]
            comic.append(comic_data)
        return comic

    def get_comic(self):
        comic_data = self.comic_data[0]
        if 'http://' in comic_data:
            html_data = urllib.request.urlopen(
                urllib.request.Request(comic_data,
                                       headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
                "utf8")
            link = comic_data
        else:
            link = "https://readcomicsonline.ru/comic/"+ comic_data
            html_data = urllib.request.urlopen(
                urllib.request.Request(link,
                                       headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
                "utf8")
        chapter_numbers = list(range(1,int(re.findall('<a href="'+link+'/(.*?)">', html_data)[0]) + 1))
        show_name = re.findall('<meta name="keywords" content="(.*?),', html_data)[0]
        self.show_name = show_name
        return chapter_numbers,show_name
    def get_comic_chapter(self, chapter_number):
        comic_data = self.comic_data[0]
        if 'http://' in comic_data:
            html_data = urllib.request.urlopen(
                urllib.request.Request(comic_data+ "/" + str(chapter_number),
                                       headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
                "utf8")
            link = comic_data + "/" + str(chapter_number)
        else:
            link = "https://readcomicsonline.ru/comic/"+ comic_data + "/" + str(chapter_number)
            html_data = urllib.request.urlopen(
                urllib.request.Request(link,
                                       headers={'User-Agent': 'Mozilla/5.0'})).read().decode(
                "utf8")
        chapter_images_len = range(1,int(re.findall('<option value="(.*?)" >', html_data)[-1]) + 1)
        chapters_images = []
        for row in chapter_images_len:
            row = int(row)
            if row > 9:
                link =  "https://readcomicsonline.ru/uploads/manga/"+comic_data+"/chapters/"+ str(chapter_number) +"/"+ str(row) +".jpg"
            else:
                link = "https://readcomicsonline.ru/uploads/manga/" + comic_data + "/chapters/" + str(
                    chapter_number) + "/0" + str(row) + ".jpg"
            chapters_images.append(link)
        return chapters_images


