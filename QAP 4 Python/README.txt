# OneStepInsurance

## Description

OneStepInsurance.py is a program designed for the One Stop Insurance Company to facilitate the entry and calculation of new insurance policy information for clients. The program performs various calculations, manages client data, and generates formatted outputs.

## Author

Chris M

## Date(s)

July 18 - 22, 2024

## Features

- Reads and sets various constants from a configuration file (`Const.dat`).
- Calculates insurance premiums based on input data.
- Formats and displays client addresses.
- Generates and displays progress bars.
- Manages insurance claim data and saves it to a file (`ClaimInformation.dat`).
- Provides functionality to handle multiple types of payments.
- Updates constants and client data for future use.

## Requirements

- Python 3.x
- `datetime` module
- `time` module
- `sys` module
- `FormatLibrary` (Included with program!)

## Constants

The program uses the following constants, read from `Const.dat`:

1. `POLICY_NUM`: Initial policy number.
2. `INSURANCE_PREM_BASE`: Base insurance premium.
3. `ADD_VEHC_DISCOUNT_RATE`: Additional vehicle discount rate.
4. `CAR_LIABILITY_RATE`: Car liability rate.
5. `GLASS_COVER_RATE`: Glass coverage rate.
6. `LOAN_CAR_RATE`: Loaner car rate.
7. `HST_RATE`: HST rate.
8. `PROCESSING_FEE`: Processing fee.

## Functions

### `first_payment_date()`

Calculates and returns the first payment date based on the current date.

### `progress_bar(iteration, total, prefix='', suffix='', length=30, fill='█')`

Generates and displays a progress bar with percentage completion.

### `address_formatting()`

Formats and returns the client address for display.

## Usage

1. Ensure `Const.dat` and `FormatLibrary` are present in the working directory.
2. Run the `OneStepInsurance.py` script.
3. Follow the on-screen prompts to enter client and policy details.
4. The program will calculate the necessary premiums and generate outputs.
5. Claim data will be saved to `ClaimInformation.dat`.

## Files

- `OneStepInsurance.py`: Main program file.
- `Const.dat`: Configuration file containing constants.
- `ClaimInformation.dat`: File to save claim information.

## Notes

- The program assumes `FormatLibrary` is a custom module for formatting-related functions.
- Ensure all required modules and files are in the working directory before running the program.
  