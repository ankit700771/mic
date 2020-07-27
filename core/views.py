from django.shortcuts import render,redirect
from core.models import Loan
from mic.settings import Loan_Model
import pandas as pd

# Create your views here.

def home(request):
    context={
        'home_active':'active',
        'home_disabled':'disabled',
    }
    return render(request,'core/home.html',context)

def about(request):
    context={
        'about_active':'active',
        'about_disabled':'disabled',
    }
    return render(request,'core/about.html',context)

def contact(request):
    context={
        'contact_active':'active',
        'contact_disabled':'disabled',
    }
    return render(request,'core/contact.html',context)

def loan(request):
    context={
        'loan_active':'active',
        'loan_disabled':'disabled',
    }
    return render(request,'core/loan.html',context)

def loan_predict(request):
    if request.method=='POST':
        gender=request.POST['gender']
        married=request.POST['married']
        dependents=request.POST['dependents']
        education=request.POST['education']
        SelfEmp=request.POST['SelfEmp']
        ApplicantIncome=request.POST['ApplicantIncome']
        coApplicantIncome=request.POST['coApplicantIncome']
        LoanAmount=request.POST['LoanAmount']
        LoanAmountTerm=request.POST['LoanAmountTerm']
        CreditHistory=request.POST['CreditHistory']
        PropertyArea=request.POST['PropertyArea']

        data = [[gender,married,dependents,education,SelfEmp,ApplicantIncome,coApplicantIncome,LoanAmount,LoanAmountTerm,CreditHistory,PropertyArea]]
        newdf = pd.DataFrame(data, columns = ['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area'])
        newdf = pd.get_dummies(newdf)

        XtrainCols=['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Gender_Female', 'Gender_Male',
       'Married_No', 'Married_Yes', 'Dependents_0', 'Dependents_1',
       'Dependents_2', 'Dependents_3+', 'Education_Graduate',
       'Education_Not Graduate', 'Self_Employed_No', 'Self_Employed_Yes',
       'Property_Area_Rural', 'Property_Area_Semiurban',
       'Property_Area_Urban']

        missing_cols = set( XtrainCols ) - set( newdf.columns )
        for c in missing_cols:
            newdf[c] = 0

        newdf = newdf[XtrainCols]

        yp=Loan_Model.predict(newdf)

        reg=Loan(gender=gender, married=married, dependents=dependents, 
            education=education, self_employed=SelfEmp, applicant_income=ApplicantIncome,
            co_applicant_income=coApplicantIncome, loan_amount=LoanAmount,
            loan_amount_term=LoanAmountTerm, credit_history=CreditHistory, 
            property_area=PropertyArea,result=yp[0])
        reg.save()

        context={
            'gender':gender,
            'married':married,
            'dependents':dependents,
            'education':education,
            'SelfEmp':SelfEmp,
            'ApplicantIncome':ApplicantIncome,
            'coApplicantIncome':coApplicantIncome,
            'LoanAmount':LoanAmount,
            'LoanAmountTerm':LoanAmountTerm,
            'CreditHistory':CreditHistory,
            'PropertyArea':PropertyArea,
            'result':yp[0],
        }

        print(yp[0])
        return render(request,'core/loanprediction.html',context)
    else:
        return redirect('loan')