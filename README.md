"# abidibo" 

To install postgres

docker run --rm   --name pg-docker -e POSTGRES_PASSWORD=chef -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres