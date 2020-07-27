"""
Django settings for mic project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=zdem81is+%7#$r507ct_nc1ck6k-xs(inp@p(&&5)nc1%u)hh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


# ML

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# import warnings
# warnings.filterwarnings("ignore")

# df=pd.read_csv('E://OneDrive//Contest//mic//mic//train.csv')

# #seperating features (X) and outcome(y) from historical data
# X=df.drop(['Loan_Status','Loan_ID'], axis=1)
# y=df['Loan_Status']

# X['Gender'].fillna("Male", inplace=True)
# X['Married'].fillna("Yes", inplace=True)
# X['Dependents'].fillna("0", inplace=True)
# X['Self_Employed'].fillna("No", inplace=True)
# mean_loan=X['LoanAmount'].mean()
# X['LoanAmount'].fillna(mean_loan,inplace=True)
# X['Loan_Amount_Term'].fillna(X['Loan_Amount_Term'].mean(),inplace=True)
# X['Credit_History'].fillna(X['Credit_History'].mean(),inplace=True)

# #Now X does not have any null value
# #One hot Encoding- Changing Categorical Values into numerical values
# X=pd.get_dummies(X)

# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.30,random_state=30)

# #Applying Machine Learning Algorithm – Logistic Regression
# Lr = LogisticRegression()
# Lr.fit(X_train,y_train)


import pickle
with open(BASE_DIR+'\\mic\\Loan_Model.pkl', 'rb') as file:  
    Loan_Model = pickle.load(file)