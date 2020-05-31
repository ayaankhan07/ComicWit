from django.shortcuts import render
from ComicManga.ComicManga import Comic, Manga
import random
# Create your views here.


def ComicMangaLatestView(request):
    m = Manga()
    c = Comic()
    manga_latest_data = m.latest_manga()[:25]
    for row in range(len(manga_latest_data)):
        manga_latest_data[row]["link"] = "/manga/" + manga_latest_data[row]["link"]
    comic_latest_data = c.latest_comic()[:25]
    for row in range(len(comic_latest_data)):
        comic_latest_data[row]["link"] = "/comic/" + comic_latest_data[row]["link"]
    latest_data = manga_latest_data + comic_latest_data
    random.shuffle(latest_data)
    return render(request, "comic-manga-index-latest.html", {"latest": latest_data})
def MangaLatestView(request):
    m = Manga()
    manga_latest_data = m.latest_manga()[:25]
    return render(request, "manga-index-latest.html", {"manga_latest": manga_latest_data})
def ComicLatestView(request):
    c = Comic()
    comic_latest_data = c.latest_comic()[:25]
    return render(request, "comic-index-latest.html", {"comic_latest": comic_latest_data})
def MangaView(request, manga_link):
    m = Manga(manga_link)
    manga_data = m.get_manga()
    return render(request, "manga-index.html", {"manga_link": manga_link,"manga_data": manga_data, "range": list(range(1,len(manga_data[0]) + 1))})
def ComicView(request, comic_link):
    c = Comic(comic_link)
    comic_data = c.get_comic()
    return render(request, "comic-index.html", {"comic_link": comic_link,"comic_data": comic_data})
def MangaChapterView(request, manga_link, chapter_number):
    m = Manga(manga_link)
    m.get_manga()
    manga_data = m.get_manga_chapter(chapter_number)
    manga_name = m.show_name
    return render(request, "manga-chapter-index.html", {"name": manga_name, "chapter_images": manga_data})
def ComicChapterView(request, comic_link, chapter_number):
    c = Comic(comic_link)
    c.get_comic()
    comic_data = c.get_comic_chapter(chapter_number)
    comic_name = c.show_name
    return render(request, "comic-chapter-index.html", {"name": comic_name, "chapter_images": comic_data})
def MangaSearchView(request, manga_name):
    m = Manga(manga_name)
    manga_data = m.search_manga()
    return render(request, "manga-search-index.html", {"manga_data": manga_data})
def ComicSearchView(request, comic_name):
    c = Comic(comic_name)
    comic_data = c.search_comic()
    return render(request, "comic-search-index.html", {"comic_data": comic_data})