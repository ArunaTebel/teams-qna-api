#TeamsQnA

This repository contains the REST API of the Arch|TeamsQnA web application.

##Environment Setup
1. Clone the repository.
1. Navigate to the project root directory
2. Down the containers if they are up already
        
        docker-compose down -v
#### For production,
1. Build and up the containers
      
       docker-compose -f docker-compose.prod.yml up -d --build
2. Run the migrations
    
       docker-compose -f docker-compose.prod.yml exec archteamsqnaapiweb python manage.py migrate --noinput
3. Collect and copy the static files
    
       docker-compose -f docker-compose.prod.yml exec archteamsqnaapiweb python manage.py collectstatic --no-input --clear
#### For development,
1. Build and up the containers
      
       docker-compose up -d --build
2. Login to the archteamsqnaapiweb container,
    
       docker exec -it arch-teams-qna-api_archteamsqnaapiweb_1 /bin/ash
    
3. Create a superuser
    
       python manage.py createsuperuser
4. Codebase is found inside the `/usr/src/app` directory of the container.
5. Access the application through http://127.0.0.1:8000/
6. Check logs by executing (on host machine),
        
       docker-compose logs -f
    
