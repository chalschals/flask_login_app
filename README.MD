### Python flask login application

##### Run the following commands to configure this applciation

	 pip install pipenv
	 pipenv shell
	 pipenv update
	 flask run

Open [http://localhost:5000/](http://localhost:5000/) in browser to view the application.


##### Error may occurs:
- User table not found

Solution:

run the follwoing commands to add user table in sqllite db (make sure you are in active pipenv environment)

		 python
		 from app import db, create_app
		 db.create_all(app=create_app())
	these command will add user model into DB

##### Other statements

- if required enable the debug option by setting FLASK_DEBUG=1 environment varibale.
- control+c to stop the application.
- Type "exit" to deactivate the pipenv environment.

