from pydrive.auth import GoogleAuth

# Authenticate user
gauth = GoogleAuth()
# Creates local webserver and auto handles authentication.
gauth.LocalWebserverAuth()


from pydrive.drive import GoogleDrive

# Create GoogleDrive instance with authenticated GoogleAuth instance.
drive = GoogleDrive(gauth)

# Create GoogleDriveFile instance with title 'Hello.txt'.
file1 = drive.CreateFile({'title': 'hello.txt'})
file1.Upload()  # Upload the file.
print('Title: %s, id: %s' % (file1['title'], file1['id']))
# OUTPUT: title: Hello.txt, id: {{FILE_ID}}


# List all files
# Auto-iterate through all files that matches this query
file_list = drive.ListFile(
    {'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
      print('File Titles: %s, id: %s' % (file1['title'], file1['id']))


"""
# Create GoogleDriveFile instance and upload it.
file1 = drive.CreateFile()
file1.Upload()

file1.Trash()  # Move file to trash.
file1.UnTrash()  # Move file out of trash.
file1.Delete()  # Permanently delete the file.
"""
