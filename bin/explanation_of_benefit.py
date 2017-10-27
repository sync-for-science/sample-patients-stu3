import csv
from testdata import EOB_FILE
from security_tags import SecurityTags

class ExplanationOfBenefit(object):
    """Create instances of ExplanationOfBenefit"""

    explanation_of_benefits = {}

    @classmethod
    def load(cls):
        # Loop through problems and build patient problem lists:
        rows = csv.reader(file(EOB_FILE,'U'), dialect='excel-tab')
        header = rows.next()
        for row in rows:
            cls(dict(zip(header, row)))

    def __init__(self,p):

        self.id = p['ID']
        self.pid = p['PID']

        # Append problem to the patient's problem list:
        if self.pid in self.__class__.explanation_of_benefits:
            self.__class__.explanation_of_benefits[self.pid].append(self)
        else:
            self.__class__.explanation_of_benefits[self.pid] = [self]

    def toJSON(self, prefix=""):

        if prefix:
            prefix += "-"

        security_tags = SecurityTags("explanation-of-benefit", prefix + self.pid)

        out = {
            "request": {
                "method": "PUT",
                "url": "ExplanationOfBenefit/" + prefix + "ExplanationOfBenefit-" + self.id
            },
            "resource": {
  "resourceType": "ExplanationOfBenefit",
                "meta": security_tags.get_security_tags(),
  "id": "EB3500",
  "text": {
    "status": "generated",
    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the ExplanationOfBenefit</div>"
  },
  "identifier": [
    {
      "system": "http://www.BenefitsInc.com/fhir/explanationofbenefit",
      "value": "987654321"
    }
  ],
  "status": "active",
  "type": {
    "coding": [
      {
        "system": "http://hl7.org/fhir/ex-claimtype",
        "code": "oral"
      }
    ]
  },
  "patient": {
    "reference": "Patient/" + prefix + self.pid
  },
  "created": "2014-08-16",
  "enterer": {
    "reference": "Practitioner/smart-Practitioner-71032702"
  },
  "provider": {
    "reference": "Practitioner/smart-Practitioner-71032702"
  },
  "outcome": {
    "coding": [
      {
        "system": "http://hl7.org/fhir/remittance-outcome",
        "code": "complete"
      }
    ]
  },
  "disposition": "Claim settled as per contract.",
  "payee": {
    "type": {
      "coding": [
        {
          "system": "http://hl7.org/fhir/payeetype",
          "code": "provider"
        }
      ]
    },
    "resourceType": {
      "coding": [
        {
          "system": "http://hl7.org/fhir/resource-type-link",
          "code": "organization"
        }
      ]
    }
  },
  "careTeam": [
    {
      "sequence": 1,
      "provider": {
        "reference": "Practitioner/smart-Practitioner-71032702"
      }
    }
  ],
  "insurance": {
    "coverage": {
      "reference": "Coverage/smart-Coverage-1"
    }
  },
  "item": [
    {
      "sequence": 1,
      "careTeamLinkId": [
        1
      ],
      "service": {
        "coding": [
          {
            "system": "http://hl7.org/fhir/service-uscls",
            "code": "1200"
          }
        ]
      },
      "servicedDate": "2014-08-16",
      "unitPrice": {
        "value": 135.57,
        "system": "urn:iso:std:iso:4217",
        "code": "USD"
      },
      "net": {
        "value": 135.57,
        "system": "urn:iso:std:iso:4217",
        "code": "USD"
      },
      "encounter": [
        {
          "reference": "Encounter/smart-828"
        }
      ],
      "adjudication": [
        {
          "category": {
            "coding": [
              {
                "code": "eligible"
              }
            ]
          },
          "amount": {
            "value": 120.00,
            "system": "urn:iso:std:iso:4217",
            "code": "USD"
          }
        },
        {
          "category": {
            "coding": [
              {
                "code": "eligpercent"
              }
            ]
          },
          "value": 0.80
        },
        {
          "category": {
            "coding": [
              {
                "code": "benefit"
              }
            ]
          },
          "amount": {
            "value": 96.00,
            "system": "urn:iso:std:iso:4217",
            "code": "USD"
          }
        }
      ]
    }
  ],
  "totalCost": {
    "value": 135.57,
    "system": "urn:iso:std:iso:4217",
    "code": "USD"
  },
  "totalBenefit": {
    "value": 96.00,
    "system": "urn:iso:std:iso:4217",
    "code": "USD"
  }
}
        }

        return out
