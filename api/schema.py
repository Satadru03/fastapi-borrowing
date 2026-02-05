from pydantic import BaseModel, Field
from pydantic import BaseModel
from enum import Enum

class EducationEnum(str, Enum):
    Bachelor = "Bachelor's"
    Master = "Master's"
    HighSchool = "High School"
    PhD = "PhD"

class EmploymentTypeEnum(str, Enum):
    Fulltime = "Full-time"
    Unemployed = "Unemployed"
    Selfemployed = "Self-employed"
    Parttime = "Part-time"

class MaritalStatusEnum(str, Enum):
    Divorced = "Divorced"
    Married = "Married"
    Single = "Single"

class LoanPurposeEnum(str, Enum):
    Other = "Other"
    Auto = "Auto"
    Business = "Business"
    Home = "Home"
    Education = "Education"

class HasMortgageEnum(str, Enum):
    Yes = "Yes"
    No = "No"

class HasDependentsEnum(str, Enum):
    Yes = "Yes"
    No = "No"

class HasCoSignerEnum(str, Enum):
    Yes = "Yes"
    No = "No"

class Borrower(BaseModel):
    Age: int = Field(..., ge=18, le=75)
    Income: int = Field(..., ge=10000)
    LoanAmount: int = Field(..., ge=1000, le= 300000)
    CreditScore: int = Field(..., ge=300, le= 850)
    MonthsEmployed: int = Field(..., ge=0)
    NumCreditLines: int = Field(..., ge=1, le= 4)
    InterestRate: int = Field(..., ge=2, le= 25)
    LoanTerm: int = Field(..., ge=12, le= 60)
    DTIRatio: float = Field(..., ge=0.1, le= 0.9)
    
    Education: EducationEnum
    EmploymentType: EmploymentTypeEnum
    MaritalStatus: MaritalStatusEnum
    LoanPurpose: LoanPurposeEnum

    HasMortgage: HasMortgageEnum
    HasDependents: HasDependentsEnum
    HasCoSigner: HasCoSignerEnum