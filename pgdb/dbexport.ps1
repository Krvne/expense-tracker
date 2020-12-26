heroku pg:backups:capture -a loan-kiosk
heroku pg:backups:download -o latest.dump -a loan-kiosk 
pg_restore --verbose --clean --no-acl --no-owner -h localhost -U postgres -d kiosk latest.dump
