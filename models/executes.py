master = """
CREATE TABLE masters (
    ID SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    tg_id VARCHAR(30),
    available_time_slots JSONB
);
"""

client = """
CREATE TABLE client (
ID SERIAL PRIMARY KEY,
fi VARCHAR(255),
phone_number VARCHAR(15)
);
"""

service = """
CREATE TABLE services (
    ID SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2)
);
"""

appointments = """
CREATE TABLE appointments (
    ID SERIAL PRIMARY KEY,
    client_id INT,
    master_id INT,
    service_id INT,
    appointment_date DATE,
    appointment_time TIME,
    FOREIGN KEY (client_id) REFERENCES client (ID),
    FOREIGN KEY (master_id) REFERENCES masters (ID),
    FOREIGN KEY (service_id) REFERENCES services (ID)
);"""
