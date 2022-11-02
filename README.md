# Сначала установите библиотеки с requirements.txt 



# pip freeze >requirements.txt  Команда что бы посмотреть установленые библиотеки,затем сохраняет в "файл.txt"



#  Как пользоваться GITHUB  и GIT:
Quick setup — if you’ve done this kind of thing before
or	
git@github.com:Ramilsas/example.git
Get started by creating a new file or uploading an existing file. We recommend every repository include a README, LICENSE, and .gitignore.


# OR
…or create a new repository on the command line
echo "# example" >> README.md
git init   ( Инициализирует репозиторий )
git add README.md    ( Отслеживать  README.md )
git commit -m "first commit"  ( После добавления нужных файлов,создаем "коммит")
git branch -M main   ( Создаем ветку )
git remote add origin git@github.com:Ramilsas/example.git   (Подключаемся к аккаунту на github )
git push -u origin main   ( Запускам )



# OR
…or push an existing repository from the command line
git remote add origin git@github.com:Ramilsas/example.git
git branch -M main
git push -u origin main
…or import code from another repository
You can initialize this repository with code from a Subversion, Mercurial, or TFS project.


