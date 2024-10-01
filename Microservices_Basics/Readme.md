# Python Microservices with Flask and MongoDB

## Project Overview

This project demonstrates a basic microservices architecture using Python, Flask, and MongoDB. It consists of two services:

1. User Service: Manages user information
2. Order Service: Manages orders and communicates with the User Service

Both services use MongoDB for data persistence and communicate with each other via RESTful APIs.

## Prerequisites

- Docker
- Docker Compose

## Project Structure

```
microservices_project/
├── user_service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── order_service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Setup and Running

1. Clone the repository:
   ```
   git clone <repository-url>
   cd microservices_project
   ```

2. Build and run the services:
   ```
   docker-compose up --build
   ```

This command will start the MongoDB instance, User Service, and Order Service.

## API Endpoints

### User Service (localhost:5000)

- Create a user: `POST /users`
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com"
  }
  ```
- Get a user: `GET /users/<user_id>`

### Order Service (localhost:5001)

- Create an order: `POST /orders`
  ```json
  {
    "user_id": "<user_id>",
    "items": ["item1", "item2"],
    "total": 29.99
  }
  ```
- Get an order: `GET /orders/<order_id>`

## Testing the Services

You can use curl or a tool like Postman to test the services. Here are some example curl commands:

1. Create a user:
   ```
   curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}' http://localhost:5000/users
   ```

2. Get a user (replace `<user_id>` with the ID returned from the create user request):
   ```
   curl http://localhost:5000/users/<user_id>
   ```

3. Create an order (replace `<user_id>` with a valid user ID):
   ```
   curl -X POST -H "Content-Type: application/json" -d '{"user_id": "<user_id>", "items": ["item1", "item2"], "total": 29.99}' http://localhost:5001/orders
   ```

4. Get an order (replace `<order_id>` with the ID returned from the create order request):
   ```
   curl http://localhost:5001/orders/<order_id>
   ```

## Shutting Down

To stop the services, use:

```
docker-compose down
```

## Future Improvements

- Implement authentication and authorization
- Add more CRUD operations for users and orders
- Implement service discovery and load balancing
- Add unit and integration tests
- Implement logging and monitoring

## Contributing

Feel free to fork this project and submit pull requests with improvements or open issues for any bugs or feature requests.

## License

This project is open-source and available under the MIT License.