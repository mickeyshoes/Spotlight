from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import MovieInfo
# Create your views here.

def initiate_movie_to_naver(request):
    import selenium.webdriver as webdriver
    import urllib.request
    import os
    from selenium.common.exceptions import NoSuchElementException

    options = webdriver.ChromeOptions()
    options.add_argument('disable_gpu')
    # options.add_argument('lang=ko_KR')
    driver = webdriver.Chrome('C:\\Users\\user\\Documents\\Spotlight\\Spotlight\\main\\Untitled Folder\\chromedriver.exe')

    url = 'https://movie.naver.com/movie/running/current.nhn'
    driver.get(url)

    try:
        title = driver.find_elements_by_class_name('tit')
        image = driver.find_elements_by_class_name('thumb')
        ganre = driver.find_elements_by_class_name('link_txt')
        print(len(title))
        print(len(image))
        print(len(ganre))
        title_list = []
        img_list = []
        ganre_dummy_list = []
        ganre_list = []
        ganre_total_list = ['액션', '모험', '드라마', '멜로/로맨스', '판타지', '애니메이션', '스릴러', 'SF', '다큐멘터리', '코미디', '범죄', '공포', '서부', '가족', '뮤지컬', '전쟁', '미스터리', '공연실황']
    
        print('---------------구분자----------------------')
#     제목 출력
        for title_name in title:
            title_list.append(title_name.find_element_by_tag_name('a').text)
        print(len(title_list))
    
#     이미지 출력
        for img_list_temp in image:
            temp = img_list_temp.find_element_by_tag_name('a')
            tmp_img = temp.find_element_by_tag_name('img').get_attribute('src')
            print(tmp_img.lstrip('/'))
            img_list.append(tmp_img.lstrip('/'))
        print(len(img_list))
        
#     for image_url in image:
#         print(image_url.text)

#     for i in ganre:
#         for j in range(len(ganre)):
#             if(j%3 == 1):
#                 print(i.find_element_by_tag_name('a').text)
#                 break

#    장르 출력
        for i in ganre:
#         print(i.find_element_by_tag_name('a').text)
            ganre_dummy_list.append(i.find_element_by_tag_name('a').text)
        
        print(len(ganre_dummy_list))
        for j in range(len(ganre_dummy_list)):
            if ganre_dummy_list[j] in ganre_total_list:
#             print(ganre_dummy_list[j])
                ganre_list.append(ganre_dummy_list[j])
            
        print(len(ganre_list))
        print('end')



        for s in range(len(ganre_list)):
            movie_list = MovieInfo()
            movie_list.movieTitle = title_list[s]
            movie_list.movieGenre = ganre_list[s]
            movie_list.movieImage = img_list[s]
            movie_list.save()

        return HttpResponse("ok")
        
        
    except NoSuchElementException as exception:
        print("error")
        print(exception)
        return HttpResponse("error")

def index(request):
    movielist = MovieInfo.objects.all
    return render(request,'searchlist.html', {'movielists':movielist})
