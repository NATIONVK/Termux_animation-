-- Local lab database schema; sample metadata only.
CREATE TABLE IF NOT EXISTS lab_events (
  id INTEGER PRIMARY KEY,
  event_time TEXT NOT NULL,
  level TEXT NOT NULL,
  message TEXT NOT NULL
);
