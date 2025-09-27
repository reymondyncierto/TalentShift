from database import client

class DatabaseService:
  def __init__(self):
    self.db = client

  def insert_resume(self, data: dict):
    # prepare user payload
    user_payload = {
      "name": data.get("Name") or "",
      "email": data.get("Email") or "",
      "phone": data.get("Phone") or "",
      "linkedin": data.get("Linkedin") or "",
      "github": data.get("Github") or "",
    }

    # helper to lowercase keys of nested objects (keeps values as-is)
    def lower_keys(d):
      if not isinstance(d, dict):
        return {}
      return {k.lower(): v for k, v in d.items()}

    # insert user and validate response
    user_result = self.db.table("users").insert(user_payload).execute()

    # helper to read fields from either dict-like or object-like responses
    def resp_get(resp, key, default=None):
      try:
        if isinstance(resp, dict):
          return resp.get(key, default)
        return getattr(resp, key, default)
      except Exception:
        return default

    # check for errors in the response
    if resp_get(user_result, "error"):
      raise Exception(f"Users insert error: {resp_get(user_result, 'error')}")

    user_data = resp_get(user_result, "data")
    if not user_data:
      # sometimes the client returns a top-level 'response' with .text or similar; include full repr
      raise Exception(f"Users insert returned no data: {repr(user_result)}")

    try:
      # user_data may be a list of rows
      user_id = user_data[0]["id"]
    except Exception as e:
      raise Exception(f"Could not read inserted user id: {e} - result data: {repr(user_data)}")

    # generic bulk insert helper with error checking
    def bulk_insert(table, rows):
      if not rows:
        return
      res = self.db.table(table).insert(rows).execute()
      try:
        print(f"insert {table} result:", repr(res))
      except Exception:
        print(f"insert {table} result: (unprintable)")

      if resp_get(res, "error"):
        raise Exception(f"Insert into {table} failed: {resp_get(res, 'error')}")
      status = resp_get(res, "status_code", 200)
      if isinstance(status, int) and status >= 400:
        raise Exception(f"Insert into {table} failed with status {status}: {repr(res)}")

    # prepare and insert experience
    experience_rows = [
      {**lower_keys(item), "user_id": user_id}
      for item in (data.get("Experience") or [])
    ]
    bulk_insert("experience", experience_rows)

    # prepare and insert education
    education_rows = [
      {**lower_keys(item), "user_id": user_id}
      for item in (data.get("Education") or [])
    ]
    bulk_insert("education", education_rows)

    # technical skills
    skills_rows = [
      {"user_id": user_id, "skill": skill}
      for skill in (data.get("Technical_Skills") or [])
    ]
    bulk_insert("technical_skills", skills_rows)

    # certifications
    cert_rows = [
      {"user_id": user_id, "certification": cert}
      for cert in (data.get("Certifications") or [])
    ]
    bulk_insert("certifications", cert_rows)

    # projects
    project_rows = [
      {**lower_keys(item), "user_id": user_id}
      for item in (data.get("Projects") or [])
    ]
    bulk_insert("projects", project_rows)

    # hackathons
    hackathon_rows = [
      {**lower_keys(item), "user_id": user_id}
      for item in (data.get("Hackathons") or [])
    ]
    bulk_insert("hackathons", hackathon_rows)

    return {"user_id": user_id}
