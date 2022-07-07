run-all:
	docker-compose up --build

stop-all:
	docker-compose down

execute-auth-on-token:
	curl --location --request POST 'http://localhost:8083/auth/realms/baeldung/protocol/openid-connect/token' \
	--header 'Content-Type: application/x-www-form-urlencoded' \
	--data-urlencode 'grant_type=password' \
	--data-urlencode 'client_id=account' \
	--data-urlencode 'client_secret=**********' \
	--data-urlencode 'ia_method_authorization=gradient' \
	--data-urlencode 'username=user1' \
	--data-urlencode 'password=1' \
	--data-urlencode 'data=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkJydW5vIiwiaWF0IjoxNTE2MjM5MDIyfQ.YDN0wJHLzyzmqdwycv4wgh-RMBwQR4C_0uehWmo_77ZrAB46YnPYmzJJ2Lb36GyyDXDwRP9Bt759hcVmUiGWEg' \
	--data-urlencode 'timestamp=2021-10-17 04:52:00.00000'

execute-auth-on-ia:
	curl --location --request POST 'http://localhost:5000/gradient' \
	--form 'data="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkJydW5vIiwiaWF0IjoxNTE2MjM5MDIyfQ.YDN0wJHLzyzmqdwycv4wgh-RMBwQR4C_0uehWmo_77ZrAB46YnPYmzJJ2Lb36GyyDXDwRP9Bt759hcVmUiGWEg"' \
	--form 'timestamp="2021-10-17 04:54:00.00000"'