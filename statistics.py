def calculateStats(numbers):
    """
    This function calculates the average and sorts the maximum and minimum values
    :param numbers: Function parameters as a list
    :return: Dictionary with respective values[avg, max, min]
    """
    try:
        avg = sum(numbers) / len(numbers)
        numbers.sort()
        max = numbers[-1]
        min = numbers[0]
    except ZeroDivisionError:
        avg = 0
        max = 0
        min = 0
    computedStats = {'avg': avg, 'max': max, 'min': min}
    return computedStats


def EmailAlert():
    """
    This function is by default true to set the flag for email to be sent
    :return: True flag
    """
    emailSent = True
    return emailSent


def LEDAlert():
    """
    This function is by default true to set the flag for led to glow
    :return: True flag
    """
    ledGlows = True
    return ledGlows


def StatsAlerter(values, maxThreshold, email_led_alert):
    """
    This function checks if max is above threshold and raises the alerts
    :param values: Max values which need to be checked with the threshold value
    :param maxThreshold: Threshold value when crossed raises the flags
    :param email_led_alert: list of email and led alert
    :return: The dictionary which has the relevant alert flag for respective max value
    """
    checkAndAlert_dict = {}
    for value in values:
        email_led_alert_dict = {}  # reset for every max value
        if value > maxThreshold:
            email_led_alert_dict["emailAlert"] = email_led_alert[0]  # Set the default values called from alert function
            email_led_alert_dict["ledAlert"] = email_led_alert[1]  # Set the default values called from alert function
            checkAndAlert_dict[value] = email_led_alert_dict  # append the dictionary
        else:
            email_led_alert[0] = email_led_alert[1] = False  # max value is less than the Threshold, manually reset the alerts
            email_led_alert_dict["emailAlert"] = email_led_alert[0]
            email_led_alert_dict["ledAlert"] = email_led_alert[1]
            checkAndAlert_dict[value] = email_led_alert_dict  # append the dictionary
    return checkAndAlert_dict
