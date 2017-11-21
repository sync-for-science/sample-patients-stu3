import csv
from testdata import COVERAGE_FILE
from security_tags import SecurityTags

class Coverage(object):
    """Create instances of Coverage"""

    coverages = {} # Dictionary of Coverage lists, by patient id

    @classmethod
    def load(cls):
        """Loads patient coverage records"""

        # Loop through coverages and build patient coverage lists:
        rows = csv.reader(file(COVERAGE_FILE,'U'), dialect='excel-tab')
        header = rows.next()
        for row in rows:
            cls(dict(zip(header, row)))

    def __init__(self,p):

        self.id = p['ID']
        self.pid = p['PID']

        # Append coverage to the patient's coverage list:
        if self.pid in self.__class__.coverages:
            self.__class__.coverages[self.pid].append(self)
        else:
            self.__class__.coverages[self.pid] = [self]

    def toJSON(self, prefix=""):
        """Builds and returns the Coverage JSON"""

        if prefix:
            prefix += "-"

        security_tags = SecurityTags("coverage", prefix + self.pid)

        out = {
            "request": {
                "method": "PUT",
                "url": "Coverage/" + prefix + "Coverage-" + self.id
            },
            "resource": {
                "id"            : prefix + "Coverage-" + self.id,
                "resourceType"  : "Coverage",
                "extension": [
                    {
                        "url": "https://www.ccwdata.org/cs/groups/public/documents/datadictionary/ms_cd.txt",
                        "valueCodeableConcept": {
                            "coding": [
                                {
                                    "system": "https://www.ccwdata.org/cs/groups/public/documents/datadictionary/ms_cd.txt",
                                    "code": "24"
                                }
                            ]
                        }
                    },
                    {
                        "url": "https://www.ccwdata.org/cs/groups/public/documents/datadictionary/orec.txt",
                        "valueCodeableConcept": {
                            "coding": [
                                {
                                    "system": "https://www.ccwdata.org/cs/groups/public/documents/datadictionary/orec.txt",
                                    "code": "3"
                                }
                            ]
                        }
                    },
                    {
                        "url": "https://www.ccwdata.org/cs/groups/public/documents/datadictionary/crec.txt",
                        "valueCodeableConcept": {
                            "coding": [
                                {
                                    "system": "https://www.ccwdata.org/cs/groups/public/documents/datadictionary/crec.txt",
                                    "code": "6"
                                }
                            ]
                        }
                    },
                    {
                        "url": "https://www.ccwdata.org/cs/groups/public/documents/datadictionary/esrd_ind.txt",
                        "valueCodeableConcept": {
                            "coding": [
                                {
                                    "system": "https://www.ccwdata.org/cs/groups/public/documents/datadictionary/esrd_ind.txt",
                                    "code": "C"
                                }
                            ]
                        }
                    }
                ],
                "status": "cancelled",
                "meta": security_tags.get_security_tags(),
                "type": {
                    "coding": [
                        {
                            "system": "http://hl7.org/fhir/sid/us-medicare",
                            "code": "Part A"
                        }
                    ]
                },
                "beneficiary": {
                    "reference": "Patient/" + prefix + self.pid
                },
                "grouping": {
                    "subGroup": "Medicare",
                    "subPlan": "Part A"
                }
            }
        }

        return out
