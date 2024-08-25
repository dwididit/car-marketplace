# Car Marketplace System

A PostgreSQL database project for a used car platform. It includes SQL scripts for table creation, data insertion, and queries that analyze sales trends, bid dynamics, and pricing. Ideal for integrating data insights into web applications.

# Entity Relationship Diagram (ERD)
![Logo](https://dwidi.com/wp-content/uploads/2024/08/car-marketplace-erd.png)

# Database Schema Overview

### Table: `sellers`
- **Purpose:** Manages seller information.
- **Description:** Stores contact information and links to the seller's city.
- **Key Columns:**
  - `seller_id` (SERIAL, PRIMARY KEY): Unique identifier for each seller.
  - `name` (VARCHAR(255), NOT NULL): Seller's full name.
  - `phone_number` (VARCHAR(255), NOT NULL): Contact phone number.
  - `email` (VARCHAR(255), NOT NULL): Email address.
  - `kota_id` (INTEGER, NOT NULL, FOREIGN KEY): References `city.kota_id`.

### Table: `cars_products`
- **Purpose:** Details cars listed for sale.
- **Description:** Includes car specifications and sales details linked to sellers.
- **Key Columns:**
  - `product_id` (SERIAL, PRIMARY KEY): Unique identifier for each car product.
  - `seller_id` (INT, NOT NULL, FOREIGN KEY): Links to `sellers.seller_id`.
  - `brand` (VARCHAR, NOT NULL): Car's brand.
  - `model` (VARCHAR, NOT NULL): Car's model.
  - `year` (INT, NOT NULL): Manufacture year.
  - `price` (INTEGER, NOT NULL): Price in whole numbers.
  - `body_type` (VARCHAR(50), NOT NULL): Describes the car's body type.
  - `car_type` (VARCHAR(255)): Optional, describes the type or usage of the car.

### Table: `city`
- **Purpose:** Catalogs city information.
- **Description:** Lists cities with unique names and coordinates.
- **Key Columns:**
  - `kota_id` (SERIAL, PRIMARY KEY): Unique city identifier.
  - `nama_kota` (VARCHAR(255), NOT NULL, UNIQUE): City name.
  - `latitude` (DECIMAL(9,6)): Geographical coordinates.
  - `longitude` (DECIMAL(9,6)): Geographical coordinates.

### Table: `cars_sell`
- **Purpose:** Records car sales transactions.
- **Description:** Tracks each car sale, indicating if it is open for bidding.
- **Key Columns:**
  - `car_sell_id` (SERIAL, PRIMARY KEY): Unique identifier for each sale record.
  - `product_id` (INT, NOT NULL, FOREIGN KEY): References `cars_products.product_id`.
  - `seller_id` (INT, NOT NULL, FOREIGN KEY): References `sellers.seller_id`.
  - `is_bid` (BOOLEAN, DEFAULT TRUE): Indicates if the sale is an open bid.
  - `date_post` (TIMESTAMP, NOT NULL, DEFAULT CURRENT_TIMESTAMP): Timestamp of the sale posting.

### Table: `buyers`
- **Purpose:** Stores buyer profiles.
- **Description:** Contains buyer contact details and city association.
- **Key Columns:**
  - `buyer_id` (SERIAL, PRIMARY KEY): Unique identifier for each buyer.
  - `name` (VARCHAR(255), NOT NULL): Buyer's full name.
  - `phone_number` (VARCHAR(255), NOT NULL): Contact number.
  - `email` (VARCHAR(255), NOT NULL): Email address.
  - `kota_id` (INTEGER, NOT NULL, FOREIGN KEY): References `city.kota_id`.

### Table: `bids`
- **Purpose:** Manages bidding on cars.
- **Description:** Records details of initial and subsequent bids on car sales.
- **Key Columns:**
  - `bid_id` (SERIAL, PRIMARY KEY): Unique identifier for each bid.
  - `buyer_id` (INT, NOT NULL, FOREIGN KEY): Links to `buyers.buyer_id`.
  - `car_sell_id` (INT, NOT NULL, FOREIGN KEY): Links to `cars_sell.car_sell_id`.
  - `first_bid_price` (INTEGER, NOT NULL): Price of the initial bid.
  - `first_bid_date` (TIMESTAMP, NOT NULL): Timestamp of the initial bid.
  - `next_bid_price` (INTEGER): Price of subsequent bids.
  - `next_bid_date` (TIMESTAMP): Timestamp of subsequent bids.

## Database Table Creation Scripts

### Create `sellers` Table
```sql
CREATE TABLE sellers (
   seller_id SERIAL PRIMARY KEY,
   name VARCHAR(255) NOT NULL,
   phone_number VARCHAR(255) NOT NULL,
   email VARCHAR(255) NOT NULL,
   kota_id INTEGER NOT NULL,
   FOREIGN KEY (kota_id) REFERENCES city(kota_id)
);
```

### Create `cars_products` Table
```sql
CREATE TABLE cars_products (
   product_id SERIAL PRIMARY KEY,
   seller_id INT NOT NULL,
   brand VARCHAR(50) NOT NULL,
   model VARCHAR(50) NOT NULL,
   year INT NOT NULL,
   price INTEGER NOT NULL,
   body_type VARCHAR(50) NOT NULL,
   car_type VARCHAR(255),
   FOREIGN KEY (seller_id) REFERENCES sellers(seller_id)
);
```


### Create `city` Table
```sql
CREATE TABLE city (
   kota_id SERIAL PRIMARY KEY,
   nama_kota VARCHAR(255) NOT NULL UNIQUE,
   latitude DECIMAL(9,6),
   longitude DECIMAL(9,6)
);
```

### Create `cars_sell` Table
```sql
CREATE TABLE cars_sell (
   car_sell_id SERIAL PRIMARY KEY,
   product_id INT NOT NULL,
   seller_id INT NOT NULL,
   is_bid BOOLEAN DEFAULT TRUE,
   date_post TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   FOREIGN KEY (product_id) REFERENCES cars_products(product_id),
   FOREIGN KEY (seller_id) REFERENCES sellers(seller_id)
);
```

### Create `buyers` Table
```sql
CREATE TABLE buyers (
   buyer_id SERIAL PRIMARY KEY,
   name VARCHAR(255) NOT NULL,
   phone_number VARCHAR(255) NOT NULL,
   email VARCHAR(255) NOT NULL,
   kota_id INTEGER NOT NULL,
   FOREIGN KEY (kota_id) REFERENCES city(kota_id)
);
```

### Create `bids` Table
```sql
CREATE TABLE bids (
   bid_id SERIAL PRIMARY KEY,
   buyer_id INT NOT NULL,
   car_sell_id INT NOT NULL,
   first_bid_price INTEGER NOT NULL,
   first_bid_date TIMESTAMP NOT NULL,
   next_bid_price INTEGER,
   next_bid_date TIMESTAMP,
   FOREIGN KEY (buyer_id) REFERENCES buyers(buyer_id),
   FOREIGN KEY (car_sell_id) REFERENCES cars_sell(car_sell_id)
);
```

# Car Marketplace Database Setup

This guide will walk you through the process of setting up the Car Marketplace database using PostgreSQL.

## Prerequisites
- PostgreSQL 16 installed on your Windows, Linux, or macOS system.
- pgAdmin, DataGrip or any other PostgreSQL client (optional, for a GUI experience).

## Step-by-Step Setup

### Step 1: Clone or Download This Repository
Clone this repository to your local machine or download the source files directly.

```bash
gh repo clone dwididit/car-marketplace
cd car-marketplace
```

### Step 2: Clone or Download This Repository
If you haven't already, install PostgreSQL 16. You can download it from [the official PostgreSQL website](https://www.postgresql.org/). Note down the superuser password you set during installation.

### Step 3: Install pgAdmin (Optional)
For a graphical interface, install pgAdmin from [pgAdmin's website](https://www.pgadmin.org/). This step is optional but recommended for easier database management.

### Step 4: Create a Connection in pgAdmin
Open pgAdmin, and create a new connection to your PostgreSQL server:

Host: localhost (or your server's IP address if remote)
Port: 5432 (default)
Username: postgres (or another superuser)
Password: your_password

### Step 5: Create the Database
Create a new database named car_marketplace using pgAdmin or the command line:
```sql
CREATE DATABASE car_marketplace;
```

### Step 6: Run SQL Scripts to Set Up Tables
From pgAdmin or another SQL client, open the SQL script files included in the cloned/downloaded repository. Execute the scripts with sufficient privileges to create tables and populate them with data. Ensure you are connected to the car_marketplace database before running the scripts.


### Step 7: Explore the Database
Now that your database is set up, you are free to execute SELECT queries and explore the data. Use pgAdmin or connect using your preferred PostgreSQL client.
