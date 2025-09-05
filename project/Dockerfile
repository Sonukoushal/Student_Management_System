FROM python:3.12

# Workdir set karo outer project ke liye
WORKDIR /code

# requirements.txt copy aur install
COPY ../requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# pura outer project copy karo
COPY .. /code/

# Workdir wahi rakho jaha manage.py hai
WORKDIR /code

# runserver command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
