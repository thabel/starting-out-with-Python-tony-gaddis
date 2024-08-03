import Patient
import Procedure


def main():
    patient = Patient.Patient(
        "nicki",
        "minaj",
        "ADES",
        "New york Jersey",
        "Alaaa",
        "Usa",
        2000,
        "05678793",
        "Dr chunkc",
        "1234567",
    )
    print(patient)
    procedure1 = Procedure.Procedure(
        procedure_name="Physical Exam",
        procedure_date="Today’s date",
        practitionner_name="Dr. Irvine",
        charges=250.00,
    )
    print(procedure1)
    procedure2 = Procedure.Procedure(
        procedure_name="X-ray",
        procedure_date="Today’s date",
        practitionner_name="Dr. Jamison",
        charges=500.00,
    )
    print(procedure2)
    procedure3 = Procedure.Procedure(
        procedure_name="Blood Test",
        procedure_date="Today’s date",
        practitionner_name="Dr. Smith",
        charges=200.00,
    )
    print(procedure3)

main()