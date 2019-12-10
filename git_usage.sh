#Git basic usage
git clone https://github.com/EmreOvunc/MyDailyScripts.git
cd MyDailyScripts
#changing files bla bla..
#git update-index --chmod=+x
#git config core.filemode true
git add .
git commit -S -m "Changing file permissions"
git config --global user.email "@emreovunc.com"
git config --global user.name "EmreOvunc"
git push
