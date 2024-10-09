from conversions import (
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit
)

def testCelsiusToKelvin():
    print("Testing Celsius to Kelvin conversions...")
    
    try:
        assert convertCelsiusToKelvin(0) == 273.15
        print("Test Case 1 Passed")
    except AssertionError:
        print("Test Case 1 Failed")

    try:
        assert convertCelsiusToKelvin(100) == 373.15
        print("Test Case 2 Passed")
    except AssertionError:
        print("Test Case 2 Failed")

    try:
        assert convertCelsiusToKelvin(-273.15) == 0.0
        print("Test Case 3 Passed")
    except AssertionError:
        print("Test Case 3 Failed")

    try:
        assert convertCelsiusToKelvin(300) == 573.15
        print("Test Case 4 Passed")
    except AssertionError:
        print("Test Case 4 Failed")

    try:
        assert convertCelsiusToKelvin(-100) == 173.15
        print("Test Case 5 Passed")
    except AssertionError:
        print("Test Case 5 Failed")

def testCelsiusToFahrenheit():
    print("Testing Celsius to Fahrenheit conversions...")
    
    try:
        assert convertCelsiusToFahrenheit(0) == 32.0
        print("Test Case 1 Passed")
    except AssertionError:
        print("Test Case 1 Failed")

    try:
        assert convertCelsiusToFahrenheit(100) == 212.0
        print("Test Case 2 Passed")
    except AssertionError:
        print("Test Case 2 Failed")

    try:
        assert convertCelsiusToFahrenheit(-40) == -40.0
        print("Test Case 3 Passed")
    except AssertionError:
        print("Test Case 3 Failed")

    try:
        assert convertCelsiusToFahrenheit(300) == 572.0
        print("Test Case 4 Passed")
    except AssertionError:
        print("Test Case 4 Failed")

    try:
        assert convertCelsiusToFahrenheit(-100) == -148.0
        print("Test Case 5 Passed")
    except AssertionError:
        print("Test Case 5 Failed")

def testFahrenheitToCelsius():
    print("Testing Fahrenheit to Celsius conversions...")
    
    try:
        assert convertFahrenheitToCelsius(32) == 0.0
        print("Test Case 1 Passed")
    except AssertionError:
        print("Test Case 1 Failed")

    try:
        assert convertFahrenheitToCelsius(212) == 100.0
        print("Test Case 2 Passed")
    except AssertionError:
        print("Test Case 2 Failed")

    try:
        assert convertFahrenheitToCelsius(-40) == -40.0
        print("Test Case 3 Passed")
    except AssertionError:
        print("Test Case 3 Failed")

    try:
        assert convertFahrenheitToCelsius(572) == 300.0
        print("Test Case 4 Passed")
    except AssertionError:
        print("Test Case 4 Failed")

    try:
        assert convertFahrenheitToCelsius(-148) == -100.0
        print("Test Case 5 Passed")
    except AssertionError:
        print("Test Case 5 Failed")

def testFahrenheitToKelvin():
    print("Testing Fahrenheit to Kelvin conversions...")
    
    try:
        assert convertFahrenheitToKelvin(32) == 273.15
        print("Test Case 1 Passed")
    except AssertionError:
        print("Test Case 1 Failed")

    try:
        assert convertFahrenheitToKelvin(212) == 373.15
        print("Test Case 2 Passed")
    except AssertionError:
        print("Test Case 2 Failed")

    try:
        assert convertFahrenheitToKelvin(-40) == 233.15
        print("Test Case 3 Passed")
    except AssertionError:
        print("Test Case 3 Failed")

    try:
        assert convertFahrenheitToKelvin(572) == 573.15
        print("Test Case 4 Passed")
    except AssertionError:
        print("Test Case 4 Failed")

    try:
        assert convertFahrenheitToKelvin(-148) == 173.15
        print("Test Case 5 Passed")
    except AssertionError:
        print("Test Case 5 Failed")

def testKelvinToCelsius():
    print("Testing Kelvin to Celsius conversions...")
    
    try:
        assert convertKelvinToCelsius(273.15) == 0.0
        print("Test Case 1 Passed")
    except AssertionError:
        print("Test Case 1 Failed")

    try:
        assert convertKelvinToCelsius(373.15) == 100.0
        print("Test Case 2 Passed")
    except AssertionError:
        print("Test Case 2 Failed")

    try:
        assert convertKelvinToCelsius(0.0) == -273.15
        print("Test Case 3 Passed")
    except AssertionError:
        print("Test Case 3 Failed")

    try:
        assert convertKelvinToCelsius(573.15) == 300.0
        print("Test Case 4 Passed")
    except AssertionError:
        print("Test Case 4 Failed")

    try:
        assert convertKelvinToCelsius(173.15) == -100.0
        print("Test Case 5 Passed")
    except AssertionError:
        print("Test Case 5 Failed")

def testKelvinToFahrenheit():
    print("Testing Kelvin to Fahrenheit conversions...")
    
    try:
        assert convertKelvinToFahrenheit(273.15) == 32.0
        print("Test Case 1 Passed")
    except AssertionError:
        print("Test Case 1 Failed")

    try:
        assert convertKelvinToFahrenheit(373.15) == 212.0
        print("Test Case 2 Passed")
    except AssertionError:
        print("Test Case 2 Failed")

    try:
        assert convertKelvinToFahrenheit(0.0) == -459.67
        print("Test Case 3 Passed")
    except AssertionError:
        print("Test Case 3 Failed")

    try:
        assert convertKelvinToFahrenheit(573.15) == 572.0
        print("Test Case 4 Passed")
    except AssertionError:
        print("Test Case 4 Failed")

    try:
        assert convertKelvinToFahrenheit(173.15) == -148.0
        print("Test Case 5 Passed")
    except AssertionError:
        print("Test Case 5 Failed")

testCelsiusToKelvin()
testCelsiusToFahrenheit()
testFahrenheitToCelsius()
testFahrenheitToKelvin()
testKelvinToCelsius()
testKelvinToFahrenheit()
