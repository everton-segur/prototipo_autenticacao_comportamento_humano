FROM maven:3.6.0-jdk-11-slim AS build
COPY sso-authorization-server/src /home/app/src
COPY sso-authorization-server/pom.xml /home/app
EXPOSE 8083
WORKDIR /home/app
ENTRYPOINT ["mvn","clean", "spring-boot:run"]
