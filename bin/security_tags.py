
class SecurityTags:

    SMART_SECURITY_CATEGORIES = "http://smarthealthit.org/security/categories"
    SMART_SECURITY_PATIENT = "http://smarthealthit.org/security/patient"

    def __init__(self, code="public", patient_id="public"):
        self.code = code
        self.patient_id = patient_id

    def get_security_tags(self):

        security_tags = {
            "security": [{
                "system": self.SMART_SECURITY_CATEGORIES,
                "code": self.code
            },
            {
                "system": self.SMART_SECURITY_PATIENT,
                "code": "Patient/" + self.patient_id
            }]
        }

        return security_tags

    def get_public_tags(self):
        security_tags = {
            "security": [{
                "system": self.SMART_SECURITY_CATEGORIES,
                "code": "public"
            }]
        }
