# QuickRestore

QuickRestore is a Python-based utility designed to help Windows users easily manage and utilize system restore points. This program allows you to list available restore points, create new restore points, and restore the system to a previous state, facilitating recovery from errors or system failures.

## Features

- **List Restore Points:** View all available restore points along with descriptions and creation times.
- **Create Restore Point:** Generate a new restore point with a custom description to safeguard your current system state.
- **Restore System:** Launch the Windows System Restore utility to return the system to a selected previous state.

## Requirements

- Windows Operating System
- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/quickrestore.git
   ```
2. Navigate into the directory:
   ```bash
   cd quickrestore
   ```

## Usage

Run the program using Python:

```bash
python quick_restore.py
```

Follow the on-screen instructions to choose an action:

1. **List restore points**: Displays all available restore points.
2. **Create a restore point**: Prompts for a description and creates a new restore point.
3. **Restore system**: Opens the Windows System Restore interface.
4. **Exit**: Closes the program.

## Important Notes

- **Administrator Privileges**: For creating restore points or launching the System Restore utility, administrator privileges may be required. Ensure you run the script with appropriate permissions.
- **System Restore Configuration**: Ensure that System Restore is enabled on your Windows system for this utility to function correctly.

## Disclaimer

QuickRestore is provided "as is" without warranty of any kind. Use this tool at your own risk. The author is not responsible for any damage or data loss resulting from the use of this tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.