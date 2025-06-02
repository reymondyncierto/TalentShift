from database import client

class DatabaseService:
  def __init__(self):
    self.db = client

  def insert_resume(self, data: dict):

    user_payload = {
      "name": data.get("Name"),
      "email": data.get("Email"),
      "phone": data.get("Phone"),
      "linkedin": data.get("Linkedin"),
      "github": data.get("Github"),
    }

    user_result = self.db.table("users").insert(user_payload).execute()

    user_id = user_result.data[0]["id"]

    def lower_keys(d):
      return {k.lower(): v for k, v in d.items()}

    def bulk_insert(table, rows):
      if rows:
        self.db.table(table).insert(rows).execute()

    experience_rows = [
      {**lower_keys(item), "user_id": user_id}
      for item in data.get("Experience", [])
    ]
    bulk_insert("experience", experience_rows)

    education_rows = [
      {**lower_keys(item), "user_id": user_id}
      for item in data.get("Education", [])
    ]
    bulk_insert("education", education_rows)

    skills_rows = [
      {"user_id": user_id, "skill": skill}
      for skill in data.get("Technical_Skills", [])
    ]
    bulk_insert("technical_skills", skills_rows)

    cert_rows = [
      {"user_id": user_id, "certification": cert}
      for cert in data.get("Certifications", [])
    ]
    bulk_insert("certifications", cert_rows)

    project_rows = [
      {**lower_keys(item), "user_id": user_id}
      for item in data.get("Projects", [])
    ]
    bulk_insert("projects", project_rows)

    hackathon_rows = [
      {**lower_keys(item), "user_id": user_id}
      for item in data.get("Hackathons", [])
    ]
    bulk_insert("hackathons", hackathon_rows)

    return {"user_id": user_id}
