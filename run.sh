docker-compose up -d

sleep 10

docker exec -i postgres_metabase bash -c "PGPASSWORD=metabase psql --username metabase" < metabase.dump