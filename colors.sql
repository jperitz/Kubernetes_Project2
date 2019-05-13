
CREATE DATABASE colors;
use colors;

CREATE TABLE fav_colors (
  name VARCHAR(20),
  color VARCHAR(10)
);

INSERT INTO fav_colors
  (name, color)
VALUES
  ('Cynthia', 'blue'),
  ('Jonathan', 'green'),
  ('Richard', 'yellow');

