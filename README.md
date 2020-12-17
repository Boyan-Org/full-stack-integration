# Next-gen EHS 🐍
![Vue Logo](/src/assets/logo-vue.png "Vue Logo")
![Django Logo](/src/assets/logo-django.png "Django Logo")

## I. Introduction
This is the course project for CSCI-410. We built a platform that allows easy and secure storage and retrieval of **medical records** for both the patients🤕 and the doctors👨🏻‍⚕️.

![Booking Appointment](/public/static/appointment.png "Booking Appointment")

![working schedule](/public/static/schedule.png "View my working schedule")

With personal information and medical records digitized, we can provide a smooth workflow among departments and people that the needed information will be delivered to the right person and new information will be collected automatically to form a new record entry.

![working schedule](/public/static/record.png "View my patient's medical record")

![Diagnosis](/public/static/diagnosis.png "Diagnose my patient")


At the bottom level, all the account information and record data are encrypted. We will also implement an access control mechanism to ensure certain information is only visible to specific user groups.

## Ⅱ. Prerequisites

Before getting started you should have the following installed and running:

- [X] Yarn - [instructions](https://yarnpkg.com/en/docs/install)
- [X] Vue CLI 3 - [instructions](https://cli.vuejs.org/guide/installation.html)
- [X] Python 3 - [instructions](https://wiki.python.org/moin/BeginnersGuide)
- [X] Anaconda - [instructions](https://www.anaconda.com/products/individual)


## Ⅲ. Setup Codebase

**Step 1** : Clone the repo to local machine

```
$ git clone https://github.com/Boyan-Org/full-stack-integration
$ cd full-stack-integration
```

**Step 2** : Install JavaScript dependencies
```
$ yarn install
```
**Step 3** : Initialize python virtual environment ([why?](https://stackoverflow.com/questions/41972261/what-is-a-virtualenv-and-why-should-i-use-one))
```
$ conda create -n venv
$ conda activate venv
```
**Step 4** : Install Python dependencies
```
$ pip install -r requirement.txt
```
**Step 5** : Initialize sqlite database
```
$ python manage.py migrate
```
- To inspect sqlite database from GUI, install [Sqlite Browser](https://sqlitebrowser.org/dl/)


## Ⅳ. Running Development Servers

**Step 1** : Run Django server
```
$ python manage.py runserver
```
- The Django API and static files will be served from [`localhost:8000`](http://localhost:8000/).

**Step 2** : Run Vue.js server (in another tab)
```
$ yarn serve
```
- The Vue application will be served from [`localhost:8080`](http://localhost:8080/)

## Ⅴ. Run Unit Test
We have a series of unit test to help our develop procedure. The way to call test is:
```sh
$ python manage.py test
```

## Ⅵ. Project Stricture

- 📂 __django\-vue\-template__
   - 📄 [README.md](README.md)
   - 📄 [app.json](app.json)
   - 📂 __backend__
     - 📂 __api__
       - 📄 [\_\_init\_\_.py](backend/api/__init__.py)
       - 📄 [admin.py](backend/api/admin.py)
       - 📄 [apps.py](backend/api/apps.py)
       - 📄 [models.py](backend/api/models.py)
       - 📄 [serializers.py](backend/api/serializers.py)
       - 📄 [tests.py](backend/api/tests.py)
       - 📄 [views.py](backend/api/views.py)
     - 📂 __settings__
       - 📄 [\_\_init\_\_.py](backend/settings/__init__.py)
       - 📄 [dev.py](backend/settings/dev.py)
       - 📄 [prod.py](backend/settings/prod.py)
     - 📄 [urls.py](backend/urls.py)
     - 📄 [wsgi.py](backend/wsgi.py)
   - 📄 [database\_models.png](database_models.png)
   - 📄 [db.sqlite3](db.sqlite3)
   - 📄 [manage.py](manage.py)
   - 📄 [package.json](package.json)
   - 📄 [requirements.txt](requirements.txt)
   - 📂 __src__
     - 📄 [App.vue](src/App.vue)
     - 📂 __assets__
     - 📂 __components__
       - 📄 [AccountInput.vue](src/components/AccountInput.vue)
       - 📄 [DashInfo.vue](src/components/DashInfo.vue)
       - 📄 [Dashboard.vue](src/components/Dashboard.vue)
       - 📄 [InfoBoard.vue](src/components/InfoBoard.vue)
       - 📄 [Interview.vue](src/components/Interview.vue)
       - 📄 [ListAppointment.vue](src/components/ListAppointment.vue)
       - 📄 [LoginForm.vue](src/components/LoginForm.vue)
       - 📄 [MakeAppointment.vue](src/components/MakeAppointment.vue)
       - 📄 [Med.vue](src/components/Med.vue)
       - 📄 [Page404.vue](src/components/Page404.vue)
       - 📄 [Person.vue](src/components/Person.vue)
       - 📄 [RecordCreate.vue](src/components/RecordCreate.vue)
       - 📄 [RecordEdit.vue](src/components/RecordEdit.vue)
       - 📄 [RecordFilter.vue](src/components/RecordFilter.vue)
       - 📄 [RecordUpload.vue](src/components/RecordUpload.vue)
       - 📄 [RecordView.vue](src/components/RecordView.vue)
       - 📄 [RegForm.vue](src/components/RegForm.vue)
       - 📄 [Schedule.vue](src/components/Schedule.vue)
     - 📄 [main.js](src/main.js)
     - 📄 [router.js](src/router.js)
   - 📄 [vue.config.js](vue.config.js)

## Ⅶ. API Document
### 1. Login API
  ```json
  PATH:
      `localhost:8000/api/login/`

  METHOD: POST

  Request Format:

      { username: "frank",
          password: "frank" }

  Response Status:

      200: Success
      401: `password` doesn't match the `username`
      404: `username` not found

  Response Format:

      { id: 1,
          username: "userfrank",
          password: "frank",
          role    : "patient",
          name    : "Frank Zhou"
      }
  ```
### 2. Register API

  ```json
  PATH:
      `localhost:8000/api/register/`

  METHOD: GET

  Request Format:

      { username   : "userboyan",
          password: "boyan",
          role    : "patient",
          name    : "Boyan Xu"
          }
      }

  Response Status:

      201: Success
      409: `Username` already taken by someone else
  ```

### 3. `personal_information` API
1. List all `personal_information` records
    ```json
    PATH:
      `localhost:8000/api/personal_information/`

    METHOD: GET

    Response Format:
        {
          name       : "userboyan",
          addr       : "Weifan Road 401",
          gender     : "Male",
          email      : "one@nyu.edu",
          dateOfBirth: "1998-03-20",
          marital    : "Single",
          phone      : "17878728172",
        }

    Response Status:
                200  : OK
                Other: Buggy
    ```
2. Create a `personal_information` record
   ```json
    PATH:
      `localhost:8000/api/personal_information/`

    METHOD: POST

    Request Format:
      {
          id           : "1",
          address      : "Weifang Road 401",
          dateOfBirth  : "1998-03-20"
          email        : "one@nyu.edu",
          gender       : "Male",
          maritalStatus: "Single",
          name         : "Boyan Xu",
          phoneNumber  : "17878728172",
      }

    Response Status:
        201: Created
        400: Creation Failed
   ```
3. Retrieve `personal_information` record with id=x
    ```json
    PATH:
        localhost:8000/api/personal_info/<int>

    METHOD:
          GET

    Response Format:
        {
          id           : "1",
          address      : "Weifang Road 401",
          dateOfBirth  : "1998-03-20"
          email        : "one@nyu.edu",
          gender       : "Male",
          maritalStatus: "Single",
          name         : "Boyan Xu",
          phoneNumber  : "17878728172"
      }

    Response Status:
        200: OK
        404: Record Not Found
    ```

4. Delete `personal_information` record with id=x
    ```json
    PATH:
        localhost:8000/api/personal_info/<int>

    METHOD: DELETE

    Response Status:
                204: Deleted
                404: Not Found
    ```
5. Update `personal_information` record with id=x
    ```json
    PATH:
        localhost:8000/api/personal_info/<int>

    METHOD: PATCH

    Request Format: (Each Attribute is optionally given)
    {
        id           : "1",
        address      : "Weifang Road 401",
        dateOfBirth  : "1998-03-20"
        email        : "one@nyu.edu",
        gender       : "Male",
        maritalStatus: "Single",
        name         : "Boyan Xu",
        phoneNumber  : "17878728172",
    }

    Response Format: Same as request payload

    Response Status:
                200: OK
                404: Not Found
                400: Update Failed
    ```

### 4. `medical_info` API

1. List all `medical_info` records
    ```json
    PATH:
      localhost:8000/api/medical_information/

    METHOD: GET

    Response Format:
        {
          bloodType      : "A",
          height         : 180,
          weight         : 50,
          allergies      : "None",
          familyHistory  : "None",
          surgicalHistory: "None",
          habits         : "None",
        }

    Response Status:
                200  : OK
                Other: Buggy
    ```
2. Create  `medical_info` record
   ```json
    PATH:
      localhost:8000/api/medical_information/<int>

    METHOD: POST

    Request Format:
        {
          bloodType      : "A",
          height         : 180,
          weight         : 50,
          allergies      : "None",
          familyHistory  : "None",
          surgicalHistory: "None",
          habits         : "None",
        }

    Response Status:
        201: Created
        400: Creation Failed
   ```
3. Retrieve `medical_info` record with id=x
    ```json
    PATH:
      localhost:8000/api/medical_information/<int>

    METHOD:
          GET

    Response Format:
        {
          bloodType      : "A",
          height         : 180,
          weight         : 50,
          allergies      : "None",
          familyHistory  : "None",
          surgicalHistory: "None",
          habits         : "None",
        }

    Response Status:
        200: OK
        404: Record Not Found
    ```

4. Delete `medical_info` record with id=x
    ```json
    PATH:
      localhost:8000/api/medical_information/<int>

    METHOD: DELETE

    Response Status:
                204: Deleted
                404: Not Found
    ```
5. Update `medical_info` record with id=x
    ```json
    PATH:
      localhost:8000/api/medical_information/<int>

    METHOD: PATCH

    Request Format: (Attributes are optionally given)
        {
          bloodType      : "A",
          height         : 180,
          weight         : 50,
          allergies      : "None",
          familyHistory  : "None",
          surgicalHistory: "None",
          habits         : "None",
        }

    Response Format: Same as request payload

    Response Status:
                200: OK
                404: Not Found
                400: Update Failed
    ```

### 5. `medical_record`


PATH: http://127.0.0.1:8000/api/medical_record/


1. List all `medical_record` records
    ```json
    PATH:
      localhost:8000/api/medical_record/

    METHOD: GET

    Response Format:
        {
          bloodType      : "A",
          height         : 180,
          weight         : 50,
          allergies      : "None",
          familyHistory  : "None",
          surgicalHistory: "None",
          habits         : "None",
        }

    Response Status:
                200  : OK
                Other: Buggy
    ```
2. Create a `medical_record` record
   ```json
    PATH:
      localhost:8000/api/medical_record/<int>

    METHOD: POST

    Request Format:
        {
          bloodType      : "A",
          height         : 180,
          weight         : 50,
          allergies      : "None",
          familyHistory  : "None",
          surgicalHistory: "None",
          habits         : "None",
        }

    Response Status:
        201: Created
        400: Creation Failed
   ```
3. Retrieve `medical_record` record with id=x
    ```json
    PATH:
      localhost:8000/api/medical_record/<int>

    METHOD:
          GET

    Response Format:
            {
              recordID        : 1,
              patient_id      : 1,
              patient_name    : "Frank",
              doctor_id       : 1
              doctor_name     : "Boyan",
              symptoms        : "Headache",
              treatments      : "Sleep more",
              diagnosis       : "神经衰弱",
              department      : "神经内科",
              patient_birthday: "1998-02-12",
              patient_gender  : "Male",
              dateTime        : "2020-12-21",
              attachmentNb    : "2",
              flag            : false,
            }

    Response Status:
        200: OK
        404: Record Not Found
    ```

4. Delete `medical_record` record with id=x
    ```json
    PATH:
      localhost:8000/api/medical_record/<int>

    METHOD: DELETE

    Response Status:
                204: Deleted
                404: Not Found
    ```
5. Update `medical_record` record with id=x
    ```json
    PATH:
      localhost:8000/api/medical_record/<int>

    METHOD: PATCH

    Request Format: (Attributes are optionally given)
            {
              recordID        : 1,
              patient_id      : 1,
              patient_name    : "Frank",
              doctor_id       : 1
              doctor_name     : "Boyan",
              symptoms        : "Headache",
              treatments      : "Sleep more",
              diagnosis       : "神经衰弱",
              department      : "神经内科",
              patient_birthday: "1998-02-12",
              patient_gender  : "Male",
              dateTime        : "2020-12-21",
              attachmentNb    : "2",
              flag            : false,
            }

    Response Format: Same as request payload

    Response Status:
                200: OK
                404: Not Found
                400: Update Failed
    ```


6. Filter `medical_record` record with given condition
    ```json
    PATH:
        localhost/api/medical_record/filter_record/

    Method: POST

    Request JSON:
        {
            filter_entry: value
        }

    Response JSON:
        {
          record_data: [
              {
                dateTime    : "2020-11-29T00:17:34",
                department  : "dept1",
                doctor_name : "Boyan Xu",
                patient_name: "Frank Zhou",
                recordID    : 1
              },],
          record_num: 1
        }
    ```

### 6. `dept_info` API

PATH: http://127.0.0.1:8000/api/department_information/

`workingHour` format example:

[[0,1],[0,0],[1,0],[1,1],[1,1],[0,0],[0,1]]

From Monday to Sunday

0 means on-duty; 1 means off.

### 7. `Appointment`

Similar to personal_info. See concrete fields/values in the database diagram

PATH: http://127.0.0.1:8000/api/appointment/

**Modified Function:**

ModelViewSet.create()

```python
@action(detail=False, methods=['POST'])
def create(self, request):
    """
    patient book appointment with a doctor.

    Request Json:
    {"date":"2020-11-29",
    "time": "morning",
    "submitTime":"2020-11-28T22:00:00",
    "doctor":2,
    "patient":1
    }

    Response status:
        406: Data not acceptable
        409: condition not satisfied (check response.data["error"])
        201: Created
    """
```


**Additional Function**

filter_appointment()

```python
@action(detail=False, methods=['POST'])
def filter_appointment(self, request):
    """
    PATH: http://127.0.0.1:8000/api/appointment/filter_appointment/
    Method: POST
    Description: return the filtered appointment that satisfies the requested criteria.
    Request JSON:
            {
                "record_data": [
                    {
                        "appointmentID": 2,
                        "date": "2020-12-02",
                        "department": "dept1",
                        "doctor_id": 2,
                        "doctor_name": "Boyan Xu",
                        "patient_id": 1,
                        "patient_name": "Frank Zhou",
                        "submitTime": "2020-11-28T22:00:00",
                        "time": "morning"
                    }
                ],
                "record_num": 1
            }
    """
```

Test code

```shell
echo '{"submitTime": "2020-11-28T22:00:00"}'|http POST http://127.0.0.1:8000/api/appointment/filter_appointment/
```

get_available_slots()

```python
@action(detail=False, methods=['POST'])
def get_available_slots(self, request):
    """
    PATH: http://127.0.0.1:8000/api/appointment/get_available_slots/
    Note:
        The slot is available if and only if:
            1). The doctor works at that slot
            2). There are less than 10 people book the slot with the doctor
            3). The patient has not booked the slot with the doctor
    Request Json:
        {
            "patient_id": 1,
        }
    Response Json:
        {
            "dates": [
                "2020-12-14",
                "2020-12-11",
                "2020-12-07",
                "2020-12-17",
                "2020-12-04",
                "2020-12-13",
                "2020-12-10",
                "2020-12-09",
                "2020-12-06",
                "2020-12-16"
            ],
            "dept_names": [
                "dept2",
                "dept1"
            ],
            "doctor_names": [
                "Hellen Wang",
                "Boyan Xu"
            ],
            "slots": [
                {
                    "date": "2020-12-04",
                    "department": "dept1",
                    "doctor_id": 2,
                    "doctor_name": "Boyan Xu",
                    "time": "morning"
                },
                ...,
                ...,
                {
                    "date": "2020-12-17",
                    "department": "dept1",
                    "doctor_id": 2,
                    "doctor_name": "Boyan Xu",
                    "time": "afternoon"
                },
                {
                    "date": "2020-12-04",
                    "department": "dept2",
                    "doctor_id": 3,
                    "doctor_name": "Hellen Wang",
                    "time": "morning"
                },
                ...,
                ...,
                {
                    "date": "2020-12-17",
                    "department": "dept2",
                    "doctor_id": 3,
                    "doctor_name": "Hellen Wang",
                    "time": "afternoon"
                }
            ],
            "times": [
                "morning",
                "afternoon"
            ]
        }
    """
```

Test code

```shell
echo '{"patient_id":1}'|http POST http://127.0.0.1:8000/api/appointment/get_available_slots/
```

appointment ->

- doctor/patient: view appointments

  - filter_appointment() : appointment_record
- doctor: diagnosis

  - Appointment.DELETE()

  - MedicalRecord.CREATE()

- patient: make an appointment (data)

  - get_info:

  - -get_filter_info: all availble department names/ doctors (name)/date(近两周)

    - request: patient_id

    - reponse: {department_names : [...,...],


doctor_names: [(id, doc_name)],

date: [unique dates]

available_slots:{

}

}

```
- -display: available date(近两周)/department/doctor (ID, name)/

- -create:
```

**Method to convert between JSON and DateTime and extract information**

Note: db只负责精确到秒 后面的小数不要包含在request里

```shell
>>> import datetime
>>> dt = datetime.datetime.today()
>>> dt
datetime.datetime(2020, 11, 29, 11, 22, 0, 12750)
>>> dt.weekday()
6
>>> dt.hour
11
>>> string = dt.isoformat()
>>> string
'2020-11-29T11:22:00.012750'
>>> datetime.datetime.strptime(string, '%Y-%m-%dT%H:%M:%S.%f')
datetime.datetime(2020, 11, 29, 11, 22, 0, 12750)
```

Current problems:

1. Get method 目前希望能够直接返还以下data，在前端拿到整块data再去做filter很不好操作

2. Get method 返还的appointment是 all available appointments 还是all appointments 还是 all booked appointments?Post method返还的data希望不仅有doctor ID, 也有对应的name

3. what is submit time


Get:

path: api/appointment

return:

```
    1. all available appointments as a list [ {date, doctorName, doctorID, department, morning/afternoon}]

    1. all available dates

    1. all available doctors (**name**, ID)

    1. all available departments
```

Post:

request json: {date: date, doctorID: doctorID, ~~department:department, ~~

~~morning/afternoon: m/a~~}@Helium Liu

Attention: there may not be that many conditions

return: the filtered available appointments

Put:

(when an appointment is booked by the patient/doctor)

request json :{date: date, doctorID: doctorID, department:department,

morning/afternoon: m/a}

return:

400 if the appintment is successfully booked (change the status of the appointment in the backend?)

...