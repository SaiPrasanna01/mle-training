# Use an official Python image as the base image
FROM python:3.6

# Set the working directory
WORKDIR /housingprice_packaging

# Copy the .whl file into the image
COPY . .

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install the required packages
#RUN pip install argparse sklearn pandas pickle mlflow numpy scipy.stats tarfile urllib.request
RUN pip install argparse==1.4.0 \
    scikit-learn==0.23.1 \
    pandas==1.0.3 \
    cloudpickle==2.2.1 \
    mlflow==1.7.2 \
    numpy==1.18.5 \
    scipy==1.4.1 \
   # tarfile==20.0 \
    urllib3==1.25.10\
    matplotlib==3.3.4

# Install the .whl file
RUN pip install dist/housing_price_sp_final-0.0.2-py3-none-any.whl

# Set the environment variables
ENV PYTHONPATH "${PYTHONPATH}:/dist"

# Set the default command to run when the container starts
CMD ["/bin/bash"]
