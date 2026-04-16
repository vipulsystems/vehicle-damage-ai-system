-- USERS TABLE
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    vehicle_id TEXT,
    phone_number TEXT,
    address TEXT,
    car_brand TEXT,
    car_model TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- VEHICLE PART PRICING TABLE
CREATE TABLE IF NOT EXISTS vehicle_parts_pricing (
    id SERIAL PRIMARY KEY,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    part TEXT NOT NULL,
    price NUMERIC NOT NULL
);


-- DAMAGE REPORTS TABLE
CREATE TABLE IF NOT EXISTS damage_reports (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    image_path TEXT NOT NULL,
    detected_parts JSONB,
    total_cost NUMERIC,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);