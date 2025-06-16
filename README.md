# Pizza API Challenge

A simple RESTful API for managing restaurants, pizzas, and their relationships, built with Flask, SQLAlchemy, and Flask-Migrate.

---

##  Setup

1. **Clone the repository**
   ```sh
   git clone <git@github.com:caninemanace/pizza-api-challenge.git>
   cd pizza-api-challenge
   ```

2. **Install dependencies using Pipenv**
   ```sh
   pip install Flask Flask-SQLAlchemy Flask-Migrate SQLAlchemy python-dotenv
   ```
   
3. **Activate the virtual environment**
   ```sh
   pipenv shell
   ```

4. **Set environment variables**
   - Ensure `.env` contains:
     ```sh
    FLASK_APP=app.py
     FLASK_ENV=development
     ```

---

##  Database Migration & Seeding

1. **Initialize the database**
   ```sh
   flask db upgrade
   ```

2. **Seed the database**
   ```sh
   python seed.py
   ```

---

## 🚦 Route Summary

| Method | Endpoint                        | Description                        |
|--------|---------------------------------|------------------------------------|
| GET    | `/restaurants/`                 | List all restaurants               |
| DELETE | `/restaurants/<id>`             | Delete a restaurant by ID          |
| GET    | `/pizzas/`                      | List all pizzas                    |
| POST   | `/restaurant_pizzas/`           | Add a pizza to a restaurant        |

---

##  Example Requests & Responses

### 1. List all restaurants

**Request**
```sh
GET /restaurants/
```

**Response**
```json
[
  {
    "id": 1,
    "name": "Mario's Pizza",
    "address": "123 Main St"
  },
  {
    "id": 2,
    "name": "Kiki's Pizza",
    "address": "456 Elm St"
  }
]
```

---

### 2. Delete a restaurant

**Request**
```sh
DELETE /restaurants/1
```

**Response**
```
(No content, status 204)
```

**If not found:**
```json
{
  "error": "Restaurant not found"
}
```

---

### 3. List all pizzas

**Request**
```sh
GET /pizzas/
```

**Response**
```json
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Mozzarella"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
```

---

### 4. Add a pizza to a restaurant

**Request**
```sh
POST /restaurant_pizzas/
Content-Type: application/json

{
  "price": 12,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

**Response**
```json
{
  "id": 1,
  "name": "Margherita",
  "ingredients": "Dough, Tomato Sauce, Mozzarella"
}
```

**Validation error (e.g., price out of range):**
```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

---

##  Validation Rules

- **RestaurantPizza price** must be an integer between 1 and 30 (inclusive).
- All fields are required for POST requests.

---

##  Using Postman

1. **Import Endpoints**
   - Use the route summary above to create requests in Postman.

2. **Set Base URL**
   - If running locally: `http://127.0.0.1:5000`

3. **Example: Add a Pizza to a Restaurant**
   - Method: `POST`
   - URL: `http://127.0.0.1:5000/restaurant_pizzas/`
   - Body: raw JSON (see above)

4. **Test GET/DELETE endpoints**
   - Use the appropriate method and endpoint.

---

##  Notes

- Make sure to run migrations and seed the database before testing endpoints.
- All responses are in JSON format.
- For further customization, edit the models and controllers in the `server/` directory.

---
