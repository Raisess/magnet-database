CREATE TABLE magnet_links(
  id          VARCHAR(36) UNIQUE,
  name        VARCHAR(100),
  uri         VARCHAR(255) UNIQUE,
  create_date DATETIME,
  hash        VARCHAR(64) UNIQUE
);
