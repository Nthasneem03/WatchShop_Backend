# API Documentation

This document provides detailed information on the API endpoints available in the WatchShop backend.

## Endpoints

### 1. Get Watch List

- **URL**: `http://127.0.0.1:8000/api/watchList`
- **Method**: `GET`
- **Description**: Retrieves a list of all watches available in the inventory.
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "Watch1",
      "brand": "Dior",
      "price": 11000.0,
      "image": "/media/watches/w1.png",
      "created": "2024-08-31T13:23:41.219514Z",
      "updated": "2024-08-31T13:23:41.219514Z"
    },
    // Additional watch objects
  ]
### 2. Create a New Watch

- **URL**: `http://127.0.0.1:8000/api/watchCreate`
- **Method**: `POST`
- **Description**: Adds a new watch to the inventory.
- **Response Body**:
  ```json
  [
    {
      "name": "New Watch",
      "brand": "Omega",
      "price": 12000.0,
      "image": "image-file-path"
    }
  ]
  
- **Response**:
  ```json
  [
    {
    "id": 2,
    "name": "New Watch",
    "brand": "Omega",
    "price": 12000.0,
    "image": "/media/watches/omega.png",
    "created": "2024-09-02T15:30:00.000000Z",
    "updated": "2024-09-02T15:30:00.000000Z"
    }
  ]
  


### Notes
- GET Request: Fetches the list of all watches. It does not require any authentication or parameters.
- POST Request: Adds a new watch to the inventory. The image field expects a path to the image file. The response returns the newly created watch object, including the id and URLs for accessing the resource.
For more detailed setup and usage instructions, refer to the [Setup Instructions](SETUP.md).








