-- users table
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name TEXT,
  email TEXT,
  phone TEXT,
  linkedin TEXT,
  github TEXT,
  metadata JSONB,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- experience
CREATE TABLE IF NOT EXISTS experience (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  title TEXT,
  company TEXT,
  start_date TEXT,
  end_date TEXT,
  description TEXT,
  metadata JSONB
);

-- education
CREATE TABLE IF NOT EXISTS education (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  degree TEXT,
  institution TEXT,
  start_date TEXT,
  end_date TEXT,
  description TEXT,
  metadata JSONB
);

-- technical_skills
CREATE TABLE IF NOT EXISTS technical_skills (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  skill TEXT
);

-- certifications
CREATE TABLE IF NOT EXISTS certifications (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  certification TEXT
);

-- projects
CREATE TABLE IF NOT EXISTS projects (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  name TEXT,
  description TEXT,
  link TEXT,
  technologies TEXT,
  metadata JSONB
);

-- hackathons
CREATE TABLE IF NOT EXISTS hackathons (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  name TEXT,
  year TEXT,
  prize TEXT,
  description TEXT,
  metadata JSONB
);
