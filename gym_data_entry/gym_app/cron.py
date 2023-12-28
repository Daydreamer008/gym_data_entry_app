# gym_app/cron.py
import pandas as pd
from django_cron import CronJobBase, Schedule
from .models import DailyEntry, MembershipData  # Make sure the import statement is correct

class UpdateDailyCsvCronJob(CronJobBase):
    RUN_EVERY_MINS = 60  # every 1 hour
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'gym_app.UpdateDailyCsvCronJob'

    def do(self):
        try:
            # Read data from the Django model
            queryset = DailyEntry.objects.all()

            # Convert queryset to DataFrame
            df = pd.DataFrame(list(queryset.values()))

            # Save the data to a CSV file
            csv_path = '/Users/ramahesh/Desktop/daily_entry.csv'
            df.to_csv(csv_path, index=False)

            # Print success message
            print('Daily CSV file updated successfully.')
        except Exception as e:
            # Print error message
            print(f'Error: {e}')

class UpdateMembershipCsvCronJob(CronJobBase):
    RUN_EVERY_MINS = 4 * 60  # every 4 hours
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'gym_app.UpdateMembershipCsvCronJob'

    def do(self):
        try:
            # Read data from the Django model
            queryset = MembershipData.objects.all()

            # Convert queryset to DataFrame
            df = pd.DataFrame(list(queryset.values()))

            # Save the data to a CSV file
            csv_path = '/Users/ramahesh/Desktop/membership_data.csv'
            df.to_csv(csv_path, index=False)

            # Print success message
            print('Membership CSV file updated successfully.')
        except Exception as e:
            # Print error message
            print(f'Error: {e}')
