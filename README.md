
## Introduction

This project is part of QAP 4 and includes all necessary files for the OneStepInsurance program and a JavaScript project. The OneStepInsurance program is designed to facilitate the entry and calculation of new insurance policy information for clients of the One Stop Insurance Company. The JavaScript project handles customer information and generates formatted outputs for display on a web page. The projects perform various calculations, manage client data, and generate formatted outputs.

## Description

### OneStepInsurance.py

OneStepInsurance.py is a program designed for the One Stop Insurance Company to facilitate the entry and calculation of new insurance policy information for clients. The program performs various calculations, manages client data, and generates formatted outputs.

### JavaScript Project

The JavaScript project in the `JavaScript QAP 4` folder defines customer objects, calculates their age and duration of stay, and generates HTML descriptions for display on a web page.

## Features

### OneStepInsurance (Python Project)
- Reads and sets various constants from a configuration file (`Const.dat`).
- Calculates insurance premiums based on input data.
- Formats and displays client addresses.
- Generates and displays progress bars.
- Manages insurance claim data and saves it to a file (`ClaimInformation.dat`).
- Provides functionality to handle multiple types of payments.
- Updates constants and client data for future use.

### JavaScript Project
- Defines customer objects and their properties.
- Calculates age and duration of stay for customers.
- Generates HTML descriptions for customers.

## Requirements

### Python Project
- Python 3.x
- `datetime` module
- `time` module
- `sys` module
- `FormatLibrary` (Included with program!)

### JavaScript Project
- A web browser to open the `index.html` file.

## Constants

The OneStepInsurance program uses the following constants, read from `Const.dat`:

1. `POLICY_NUM`: Initial policy number.
2. `INSURANCE_PREM_BASE`: Base insurance premium.
3. `ADD_VEHC_DISCOUNT_RATE`: Additional vehicle discount rate.
4. `CAR_LIABILITY_RATE`: Car liability rate.
5. `GLASS_COVER_RATE`: Glass coverage rate.
6. `LOAN_CAR_RATE`: Loaner car rate.
7. `HST_RATE`: HST rate.
8. `PROCESSING_FEE`: Processing fee.

## Usage

### OneStepInsurance (Python Project)
1. Ensure `Const.dat` and `FormatLibrary` are present in the working directory.
2. Run the `OneStepInsurance.py` script.
3. Follow the on-screen prompts to enter client and policy details.
4. The program will calculate the necessary premiums and generate outputs.
5. Claim data will be saved to `ClaimInformation.dat`.

### JavaScript Project
1. Open the `index.html` file in a web browser.
2. The JavaScript code in `script.js` will execute, displaying customer information and generating HTML descriptions.

## Files

### OneStepInsurance (Python Project)
- **OneStepInsurance.py**: Main program file that handles client and policy data input, performs calculations, and generates outputs.
- **Const.dat**: Configuration file containing constants used throughout the program.
- **ClaimInformation.dat**: File used to save and manage insurance claim data.
- **FormatLibrary.py**: Custom library for formatting-related functions.
- **README.txt**: This README file providing an overview of the project and its components.

### JavaScript Project
- **index.html**: HTML file for the JavaScript project that sets up the web page structure.
- **script.js**: JavaScript file that defines customer objects and performs various operations such as calculating age, duration of stay, and generating HTML descriptions.
