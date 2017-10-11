# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()


drive = GoogleDrive(gauth)

# Create your views here.
from django.shortcuts import HttpResponse, redirect, render



def index(request):
    auth_url = gauth.GetAuthUrl()
    # code = AskUserToVisitLinkAndGiveCode(auth_url)
    # gauth.Auth(code)
    response = "Auth_url:" + str(auth_url) + "; Code: unknown"
    return HttpResponse(response)


def create_folder(request):
    gauth = GoogleAuth()
    # gauth.ServiceAuth()
    drive = GoogleDrive(gauth)
    title = 'WatPi'
    folder_metadata = {
        'title' : title,
        # The mimetype defines this new file as a folder, so don't change this.
        'mimeType' : 'application/vnd.google-apps.folder'
    }
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()
    
    # Get folder info and print to screen.
    folder_title = folder['title']
    folder_id = folder['id']
    response = str(('title: %s, id: %s' % (folder_title, folder_id)))
    # response = title + ' folder created!'
        
    # Upload file to folder.
    f = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": folder_id}]})
    # Make sure to add the path to the file to upload below.
    f.SetContentFile('apps/gcloud/static/practice.txt')
    f.Upload()
    return HttpResponse(response)

