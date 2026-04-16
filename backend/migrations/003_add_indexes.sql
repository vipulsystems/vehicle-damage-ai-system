-- Index for faster user lookup
CREATE INDEX idx_users_email ON users(email);

-- Index for pricing lookup
CREATE INDEX idx_vehicle_parts ON vehicle_parts_pricing(brand, model, part);

-- Index for report queries
CREATE INDEX idx_reports_user_id ON damage_reports(user_id);