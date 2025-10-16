# Event Planner System 🎉

A Python-based event planning application with user authentication, store management, and smart scheduling features.

## 📋 Features

- **🔐 User Authentication**: Secure login and registration system with password masking using `getpass`
- **🏪 Store Management**: Manage event planner stores and inventory
- **📅 Smart Schedule**: Intelligent scheduling system for planning events
- **💰 Budget Tracking**: Budget management features (coming soon)
- **👤 Profile Management**: User profile management (coming soon)
- **👥 Customer Management**: Customer relationship management (coming soon)

## 🤝 Real-Time Collaboration

This project supports real-time collaboration with your friends! 

### Quick Setup (2 minutes):
1. **Add collaborators**: Go to [GitHub Settings](https://github.com/sethshelby/eventplannersystem/settings/access) → Add people
2. **Use sync tool**: Run `./sync.sh` to pull/push changes easily
3. **See [QUICKSTART.md](QUICKSTART.md)** for step-by-step instructions

### Basic Workflow:
**Before working:** `git pull origin main`  
**After changes:** `./sync.sh` or `git add . && git commit -m "message" && git push origin main`

📖 **Full guide:** [COLLABORATION.md](COLLABORATION.md)

## 🚀 Prerequisites

- Python 3.x (no external dependencies required)

## 📦 Installation

1. Clone this repository:
```bash
git clone https://github.com/sethshelby/eventplannersystem.git
cd eventplannersystem
```

2. Run the application:
```bash
python Login.py
```

Or use the App.py launcher:
```bash
python App.py
```

## 💻 Usage

1. **Start the application** by running `python Login.py` or `python App.py`
2. **Register a new account** or login with existing credentials
3. **Navigate through the menu** to access different features:
   - **Stores**: Manage event planner stores
   - **Smart Schedule**: Schedule and manage events
   - **Budget**: Track event budgets (coming soon)
   - **Profile**: Manage your user profile (coming soon)
   - **Customer**: Manage customer information (coming soon)

## 📁 Project Structure

```
eventplannersystem/
├── App.py                      # Application launcher
├── Login.py                    # Main entry point with authentication
├── Homepage.py                 # Homepage module
├── module.py                   # Core menu functions
├── users.json                  # User data storage (auto-generated)
├── tasks.json                  # Task data storage (auto-generated)
├── event_planner_stores.json   # Store data storage (auto-generated)
└── page/
    ├── Store.py                # Store management module
    └── SmartSchedule.py        # Smart scheduling module
```

## 📄 Data Files

The application automatically creates and manages the following JSON files:
- `users.json` - Stores user account information with timestamps
- `tasks.json` - Stores task and schedule data
- `event_planner_stores.json` - Stores event planner store information

## 🔒 Security

- Passwords are masked during input using Python's `getpass` module
- User data is stored locally in JSON format
- User passwords are stored with account creation and last login timestamps

## 🛠️ Main Menu Options

1. **Stores** - Access store management features
2. **Smart Schedule** - Plan and schedule events
3. **Budget** - Manage event budgets
4. **Profile** - View and edit your profile
5. **Customer** - Manage customer database
6. **Exit** - Logout and exit the application

## 📝 Notes

- All data is stored locally in JSON files
- The application uses only Python standard library (no pip packages required)
- First-time users need to register before logging in

## 👨‍💻 Contributing

Feel free to fork this repository and submit pull requests for new features or bug fixes.

## 📧 Support

For issues or questions, please open an issue on GitHub.

## 📜 License

This project is open source and available for personal and educational use.

---

**Made by Keo Ravit, Lonn Thou Piseth, San Risemoon**
