
### Testing it
#### create a user
```bash
curl -X POST http://localhost:8000/users/ -H "Content-Type: application/json" -d '{"email":"a@test.com","name":"A"}'
```

#### get all users
```bash
curl -X GET http://localhost:8000/ -H "Content-Type: application/json"
```