import os
import subprocess
import sys
import datetime

class QuickRestore:
    def __init__(self):
        self.system_restore_command = "rstrui.exe"
    
    def list_restore_points(self):
        try:
            print("Listing available restore points...")
            restore_points_output = subprocess.check_output(
                ["wmic", "/namespace:\\\\root\\default", "path", "SystemRestore", "get", "Description,CreationTime"],
                shell=True
            )
            print(restore_points_output.decode())
        except subprocess.CalledProcessError as e:
            print(f"Failed to list restore points: {e}")
    
    def create_restore_point(self, description="QuickRestore Point"):
        try:
            print(f"Creating restore point: {description}...")
            creation_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            subprocess.check_call(
                ["wmic", "/namespace:\\\\root\\default", "path", "SystemRestore", "call", "CreateRestorePoint",
                 f"\"{description}\"", "100", "7"],
                shell=True
            )
            print(f"Restore point '{description}' created successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create restore point: {e}")

    def restore_system(self):
        try:
            print("Launching System Restore...")
            subprocess.check_call([self.system_restore_command], shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to launch System Restore: {e}")

def main():
    print("QuickRestore - System Restore Utility")
    qr = QuickRestore()

    while True:
        print("\nOptions:")
        print("1. List restore points")
        print("2. Create a restore point")
        print("3. Restore system to a previous state")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            qr.list_restore_points()
        elif choice == '2':
            description = input("Enter a description for the restore point: ")
            qr.create_restore_point(description)
        elif choice == '3':
            qr.restore_system()
        elif choice == '4':
            print("Exiting QuickRestore.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()