# Running Containers as Services

 * Postgres needs to be enabled to run on more than localhost
   * edit postgresql.conf to listen on *
   * update pg_hba.conf permissions

docker run -e RAILS_ENV=production -e POSTGRES_SERVICE_HOST=192.168.121.165 -e DATABASE_SERVICE_NAME=postgres -e POSTGRES_USER=foreman -e POSTGRES_PASSWORD="LcRcEbsHChS9wyqPZtpNgRJZcJ5CQ2Qg" --publish 8088:8088 foreman

 * Need to reverse proxy Apache to container 
