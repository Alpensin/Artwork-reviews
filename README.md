## API Service for films, books and songs reviews

### Functionality
#### Project collects reviews of books, songs, films.
#### Registration algorithm:
1. User sends request with email address on `/auth/email/`.
2. Service sends email with `confirmation_code` to this address.
3. User sends request with this email and `confirmation_code` to `/auth/token/`. In response user gets JWT-token.
4. User can send PATCH-request to `/users/me/` and fill his profile.

#### Roles:
- Anonimous user can get Book/Song/Film description, read reviews and comments under them.
- Authorized user can get read same things as Anonimous plus publish reviews, comments, and rate Book/Song/Film.
- Moderator can do same as Authorized user plus he can remove any review and comment.
- Administrator and Django admin can do same as Moderator plus can add and remove categories and Books/Songs/Films. Can change user roles.


### To deploy with GitHub actions on remote server in docker containers you need set In GitHub secrets:

`DB_ENGINE=django.db.backends.postgresql` — This project meant the use of this DB.

`DB_NAME=postgres` — Default DB name.

`POSTGRES_USER=postgres` — Default Login. You should set yours.

`POSTGRES_PASSWORD=postgres` — Default password. You should set yours.

`DB_HOST=db` — service name (and docker-compose container)

`DB_PORT=5432` — Default TCP port.

#### To publish at Docker Hub
`DOCKER_PASSWORD`
`DOCKER_USERNAME`

#### For SSH connection to remote server:
`USER`
`SSH_KEY`
`PASSPHRASE`

#### To get deploy results on Telegram messanger:
`TELEGRAM_TO` — Your id

`TELEGRAM_TOKEN` — Bot token

##### After deploy your need to do next on server:
```
docker-compose exec web python manage.py makemigrations --noinput
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py collectstatic --noinput
docker-compose exec web python manage.py createsuperuser
```
