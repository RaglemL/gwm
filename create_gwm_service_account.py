import subprocess
import time

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr}")

# Create a new Google Cloud project
print("[Creating GCP Project...]")
run_command('gcloud projects create goamericancustomcon-source --name="Goamericancustomcon-Source"')
time.sleep(5)

# Set the current Google Cloud project
print("[Setting up GCP Project...]")
run_command('gcloud config set project goamericancustomcon-source')
time.sleep(5)

# Provide yourself Organization Policy Administrator and Project Creator roles
print("[Assigning Roles...]")
run_command('gcloud organizations add-iam-policy-binding 803688195524 --member="user:cloudasta@archive.goamericancustomcontractors.com" --role="roles/orgpolicy.policyAdmin"')
time.sleep(5)
run_command('gcloud organizations add-iam-policy-binding 803688195524 --member="user:cloudasta@archive.goamericancustomcontractors.com" --role="roles/resourcemanager.projectCreator"')
time.sleep(5)

# Disable the constraint iam.disableServiceAccountKeyCreation enforcement
print("[Disabling Policy Enforcement...]")
run_command('gcloud resource-manager org-policies disable-enforce iam.disableServiceAccountKeyCreation --organization=803688195524')
time.sleep(60)

# Create a new service account
print("[Creating Service Account...]")
run_command('gcloud iam service-accounts create Goamericancustomcon-Source --project=goamericancustomcon-source')
time.sleep(5)

# Add IAM policy binding to the project
print("[Adding Policies...]")
run_command('gcloud projects add-iam-policy-binding goamericancustomcon-source --member="serviceAccount:Goamericancustomcon-Source@goamericancustomcon-source.iam.gserviceaccount.com" --role="roles/editor"')
time.sleep(5)

# Get the unique ID of the service account
print("[Obtaining Unique ID...]")
run_command('gcloud iam service-accounts describe Goamericancustomcon-Source@goamericancustomcon-source.iam.gserviceaccount.com --project=goamericancustomcon-source --format="value(uniqueId)"')
time.sleep(5)

# Create a service account key and save it to a JSON file
print("[Creating JSON Key...]")
run_command('gcloud iam service-accounts keys create Goamericancustomcon-Source.json --iam-account=Goamericancustomcon-Source@goamericancustomcon-source.iam.gserviceaccount.com --project=goamericancustomcon-source')
time.sleep(5)

# Enable necessary Google services
print("[Enabling APIs...]")
run_command('gcloud services enable drive.googleapis.com sheets.googleapis.com admin.googleapis.com people.googleapis.com contacts.googleapis.com migrate.googleapis.com gmail.googleapis.com calendar-json.googleapis.com groupsmigration.googleapis.com groupssettings.googleapis.com tasks.googleapis.com forms.googleapis.com vault.googleapis.com storage-component.googleapis.com --project=goamericancustomcon-source')
time.sleep(5)

# Download the service account key JSON file
print("[Downloading JSON Key...]")
run_command('cloudshell download Goamericancustomcon-Source.json')
time.sleep(5)

# Enable the constraint iam.disableServiceAccountKeyCreation enforcement
print("[Re-enabling Policy Enforcement...]")
run_command('gcloud resource-manager org-policies enable-enforce iam.disableServiceAccountKeyCreation --organization=803688195524')
time.sleep(5)

# Tasks completed confirmation
print("[All tasks completed.]")
time.sleep(5)
print("Script created by Luis Melgar.")
