# Qbeyond Uzdevums
Hosted on heroku with automatic deployment.

### Getting started
    1.Create a virtual Environment `python3 venv env`
    2.Start the virtual env. `source env/bin/activate`
    3.Install packages by running `pip install -r requirements.txt`
    4.Run the app with `python3 ./app.py`

### Saving libraries
write `pip freeze > requirements.txt` to save libraries for package manager use.

### Request Example

`
{
  "input1": 3,
  "input2": 3,
  "operator":"/"
}
`
