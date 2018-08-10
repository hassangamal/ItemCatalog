# ItemCatalog
Item Catalog Project Web Application with Flask framework.

#Installation & Run Application

1- install vagrant &virualbox OR linux

2- install python 2.7

3- Install Flask

4- Install Jinja2

5- Install SQLAchemy

6- Install OAuth

7- run database python itemcatalog/catalog_db.py

8- run insert first data  python itemcatalog/database_input.py

9- run project python itemcatlog/project.py in  http://localhost:5000


# Using Google Login

1- Go to your app's page in the Google APIs Console — https://console.developers.google.com/apis

2- Choose Credentials from the menu on the left.

3- Create an OAuth Client ID.

4- choose Web application.

5- You will then be able to get the client ID and client secret.

 # JSON Endpoints APIS
 
 this data public to any one can see it
 
 1- Catalog JSON: http://localhost:5000/Api/Catalog/JSON - Displays All Catalogs Data.
 
 2- Catalog Items JSON: http://localhost:5000/Api/Catalog/<int:catalog_id>/items/JSON - Displays All Items Catalogs Data.
 
 3- Item JSON : http://localhost:5000/Api/Catalog/<int:catalog_id>/items/<int:item_id>/JSON - Display Catalog Item Data.

