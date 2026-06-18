-- Optional database schema for stock analysis

CREATE TABLE stocks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(20) NOT NULL,
    trade_date DATE NOT NULL,
    open_price DECIMAL(18,4),
    close_price DECIMAL(18,4),
    volume BIGINT
);
