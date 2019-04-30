def applicant_selector(gpa, ps_score, ec_count):
  if (gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
    return "This applicant should be accepted."
  if (gpa >= 3.0) and (ps_score >= 90) and not (ec_count >= 3):
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."

Jack = applicant_selector(3.8, 90, 3)
Lisa = applicant_selector(4.0, 94, 5)
Jenny = applicant_selector(3.2, 90, 2)
Bob = applicant_selector(3.0, 88, 2)
