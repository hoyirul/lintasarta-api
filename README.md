# Lintasarta API

## Descroption
Lintasarta API is a RESTful API that allows marketplace and seller to communicate with each other. The API provides endpoints for marketplace to manage purchases, seller to manage products, and authentication.

## Installation

1. Clone the repository: `git clone https://github.com/hoyirul/lintasarta-api.git`
2. Make venv: `python3 -m venv venv`
3. Activate venv: Windows `venv\Scripts\activate` MacOS/Linux `source venv/bin/activate`
4. Install the required dependencies: `pip3 install -r requirements.txt`
5. Run the server marketplace: `python3 marketplace.py` with url `http://localhost:5000`.
6. Run the server seller: `python3 seller.py` with url `http://localhost:5001`.

## Example Usage
### GET
Go to PostMan or any other API testing tool.
- Set the base URL to `http://localhost:5000/api/purchase`.
- Set the request type to `GET`.
- Set headers Authorization to `Bearer MARKETPLACE-TOKEN-XXX` where `MARKETPLACE-TOKEN-XXX` is the token obtained from the login API.
- Set headers X-PURCHASE-ID to `PUR-XXX-001` where `PUR-XXX-001` is the purchase ID obtained from the purchase API.
- Click on `Send`.

### POST
Go to PostMan or any other API testing tool.
- Set the base URL to `http://localhost:5000/api/purchase`.
- Set the request type to `POST`.
- Set headers Authorization to `Bearer MARKETPLACE-TOKEN-XXX` where `MARKETPLACE-TOKEN-XXX` is the token obtained from the login API.
- Set headers X-PURCHASE-ID to `PUR-XXX-003` where `PUR-XXX-003` is the purchase ID obtained from the purchase API.
- Set headers Content-Type to `application/json`.
- Set the request body to the following JSON:
```
{
  "name": "Testing",
  "price": 100000
}
```
- Notes: The `name` and `price` fields are required from seller API. so your marketplace should handlde these fields (dynamic fields).
- Click on `Send`.

### PUT
Go to PostMan or any other API testing tool.
- Set the base URL to `http://localhost:5000/api/purchase`.
- Set the request type to `PUT`.
- Set headers Authorization to `Bearer MARKETPLACE-TOKEN-XXX` where `MARKETPLACE-TOKEN-XXX` is the token obtained from the login API.
- Set headers X-PURCHASE-ID to `PUR-XXX-004` where `PUR-XXX-004` is the purchase ID obtained from the purchase API.
- Set headers Content-Type to `application/json`.
- Set parameters `id` to `1` cause seller API need params `id`.
- Set the request body to the following JSON:
```
{
  "name": "Testing",
  "price": 100000
}
```
- Click on `Send`.

### DELETE
Go to PostMan or any other API testing tool.
- Set the base URL to `http://localhost:5000/api/purchase`.
- Set the request type to `DELETE`.
- Set headers Authorization to `Bearer MARKETPLACE-TOKEN-XXX` where `MARKETPLACE-TOKEN-XXX` is the token obtained from the login API.
- Set headers X-PURCHASE-ID to `PUR-XXX-005` where `PUR-XXX-005` is the purchase ID obtained from the purchase API.
- Set parameters `id` to `1` cause seller API need params `id`.
- Click on `Send`.
