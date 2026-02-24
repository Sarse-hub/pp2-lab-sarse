# ============================================================================
# Python Date and Time Operations - Practice Exercises
# ============================================================================

import datetime
import time
import pytz  # For timezone operations

# ============================================================================
# 1. DATETIME MODULE BASICS
# ============================================================================

print("=== DateTime Module Basics ===")

# Current date and time
now = datetime.datetime.now()
print(f"Current date and time: {now}")
print(f"Current date: {now.date()}")
print(f"Current time: {now.time()}")

# Create specific date
specific_date = datetime.datetime(2024, 12, 25, 10, 30, 45)
print(f"Specific date: {specific_date}")

# ============================================================================
# 2. CREATING DATE OBJECTS
# ============================================================================

print("\n=== Creating Date Objects ===")

# Date object (no time)
today = datetime.date.today()
print(f"Today's date: {today}")

# Time object (no date)
current_time = datetime.time(14, 30, 45)
print(f"Current time object: {current_time}")

# Date from year, month, day
custom_date = datetime.date(2024, 3, 15)
print(f"Custom date: {custom_date}")

# ============================================================================
# 3. DATE FORMATTING
# ============================================================================

print("\n=== Date Formatting ===")

now = datetime.datetime.now()

# Common format codes:
# %Y - Year (4 digits)
# %m - Month (2 digits)
# %d - Day (2 digits)
# %H - Hour (24-hour)
# %M - Minute
# %S - Second
# %A - Full weekday name
# %B - Full month name

print(f"Formatted date: {now.strftime('%Y-%m-%d')}")
print(f"Formatted time: {now.strftime('%H:%M:%S')}")
print(f"Full format: {now.strftime('%A, %B %d, %Y at %I:%M %p')}")

# ============================================================================
# 4. PARSING DATES FROM STRINGS
# ============================================================================

print("\n=== Parsing Dates from Strings ===")

date_string = "2024-03-15 14:30:45"
parsed_date = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
print(f"Parsed date: {parsed_date}")

# ============================================================================
# 5. CALCULATING TIME DIFFERENCES
# ============================================================================

print("\n=== Calculating Time Differences ===")

# Date arithmetic
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print(f"Today: {today}")
print(f"Yesterday: {yesterday}")
print(f"Tomorrow: {tomorrow}")

# Time difference between two dates
date1 = datetime.datetime(2024, 3, 15, 10, 0, 0)
date2 = datetime.datetime(2024, 3, 16, 14, 30, 45)
difference = date2 - date1

print(f"Date 1: {date1}")
print(f"Date 2: {date2}")
print(f"Difference: {difference}")
print(f"Days: {difference.days}, Seconds: {difference.seconds}")

# ============================================================================
# 6. WORKING WITH TIMEZONES
# ============================================================================

print("\n=== Working with Timezones ===")

# Get timezone-aware datetime
utc = pytz.UTC
eastern = pytz.timezone('US/Eastern')
london = pytz.timezone('Europe/London')

# Current time in different timezones
utc_now = datetime.datetime.now(utc)
eastern_now = datetime.datetime.now(eastern)
london_now = datetime.datetime.now(london)

print(f"UTC time: {utc_now}")
print(f"Eastern time: {eastern_now}")
print(f"London time: {london_now}")

# Convert between timezones
utc_time = datetime.datetime(2024, 3, 15, 12, 0, 0, tzinfo=utc)
eastern_time = utc_time.astimezone(eastern)
print(f"UTC: {utc_time} -> Eastern: {eastern_time}")

# ============================================================================
# 7. PRACTICAL EXAMPLES
# ============================================================================

print("\n=== Practical Examples ===")

# Calculate age
def calculate_age(birth_date):
    """Calculate age from birth date"""
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

birth_date = datetime.date(1990, 5, 15)
print(f"Age: {calculate_age(birth_date)} years old")

# Countdown timer
def countdown_timer(seconds):
    """Simple countdown timer"""
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Uncomment to test countdown (commented out to avoid delay)
# countdown_timer(5)

# Format date for different locales
def format_date_locale(dt, locale='en'):
    """Format date for different locales"""
    if locale == 'en':
        return dt.strftime('%B %d, %Y')
    elif locale == 'de':
        return dt.strftime('%d.%m.%Y')
    elif locale == 'fr':
        return dt.strftime('%d/%m/%Y')
    else:
        return dt.strftime('%Y-%m-%d')

sample_date = datetime.datetime(2024, 12, 25)
print(f"English: {format_date_locale(sample_date, 'en')}")
print(f"German: {format_date_locale(sample_date, 'de')}")
print(f"French: {format_date_locale(sample_date, 'fr')}")

# ============================================================================
# 8. WORKING WITH TIMESTAMPS
# ============================================================================

print("\n=== Working with Timestamps ===")

# Convert datetime to timestamp
now = datetime.datetime.now()
timestamp = now.timestamp()
print(f"Current timestamp: {timestamp}")

# Convert timestamp back to datetime
from_timestamp = datetime.datetime.fromtimestamp(timestamp)
print(f"From timestamp: {from_timestamp}")

# ============================================================================
# 9. CALENDAR OPERATIONS
# ============================================================================

print("\n=== Calendar Operations ===")

import calendar

# Check if year is leap year
year = 2024
is_leap = calendar.isleap(year)
print(f"Is {year} a leap year? {is_leap}")

# Get number of days in month
month_days = calendar.monthrange(2024, 2)[1]  # February 2024
print(f"Days in February 2024: {month_days}")

# Print calendar for a month
print("\nCalendar for March 2024:")
print(calendar.month(2024, 3))

print("\n=== Date and Time Practice Complete ===")