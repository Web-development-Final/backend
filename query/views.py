import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from bs4 import BeautifulSoup

def getEventsData(request):
    list_data = {}
    response = requests.get('https://www.songkick.com/live-stream-concerts')
    soup = BeautifulSoup(response.text, 'html.parser')

    profiles = soup.find_all(class_='artist-profile-image artist')
    list_profiles = [profile.attrs['src'] for profile in profiles]

    containers = soup.find_all(class_='stream-info-container')
    list_titles = [container.find(class_='title').getText() for container in containers]
    list_date = [container.find(class_='date').find(class_='convert-to-local-datetime').getText() for container in containers]
    list_time = [container.find(class_='time').find(class_='convert-to-local-datetime').getText() for container in containers]

    for i, (profile, title, date, time) in enumerate(zip(list_profiles, list_titles, list_date, list_time)):
        list_data[i] = {
            "image": profile,
            "title": title,
            "date": date,
            "time": time,
        }

    return JsonResponse(list_data)