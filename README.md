Discord Account Balance Tracker Bot

A Discord bot for tracking Steam account balances with role-based access control

---

 Project Overview
A secure Discord bot that tracks user account balances via Steam hex identifiers, with granular control over:
- Bot operators (`BOTS` in config)
- Authorized channels (`CHANNELS` in config)
- Restricted command access using `!rep` prefix

---

 Key Features
🔹 Secure Command System  
- All commands require `!rep` prefix  
- Restricted to authorized channels specified in `config.json`  

🔹 Multi-Role Support  
- Separate permissions for:  
  - Main bot (`BOT`)  
  - Maintainers (`ME`, `MAIN`, `MAIN2`)  

🔹 Database Integration  
- MySQL backend with automatic schema creation  
- Password protection via `DATABASE_PASS` config  

---

 Configuration Schema
```json
{
  "TOKEN": "Discord bot token",
  "COMMAND": "!rep (command prefix)",
  "DATABASE_PASS": "MySQL root password",
  "BOTS": {
    "BOT": "Primary bot ID",
    "ME": "Your personal ID",
    "MAIN": "First maintainer ID",
    "MAIN2": "Second maintainer ID"
  },
  "CHANNELS": {
    "1": "Authorized channel 1",
    "2": "Authorized channel 2",
    "ME": "Your personal channel"
  }
}
```

---

 Setup Instructions

1. Create config.json  
   ```json
   {
     "TOKEN": "YOUR_DISCORD_BOT_TOKEN",
     "COMMAND": "!rep",
     "DATABASE_PASS": "your_database_password",
     "BOTS": {
       "BOT": "123456789012345678",
       "ME": "876543210987654321",
       "MAIN": "123456789012345678",
       "MAIN2": "876543210987654321"
     },
     "CHANNELS": {
       "1": "987654321098765432",
       "2": "234567890123456789",
       "ME": "345678901234567890"
     }
   }
   ```

2. Install Dependencies  
   ```bash
   pip install discord.py mysql-connector-python
   ```

3. Run the Bot  
   ```bash
   python bot.py
   ```

---

 Security Best Practices
⚠️ Critical Security Measures  
1. Add `config.json` to `.gitignore`  
2. Use environment variables for sensitive values in production:  
   ```python
   import os
   TOKEN = os.getenv('DISCORD_TOKEN')
   ```
3. Restrict bot permissions in Discord server settings

---

 Command Reference
```plaintext
!rep help        - Show command list
!rep money HEX   - Check account balance
!rep remoney HEX - Reset balance to $0
!rep allmoney    - List all tracked accounts
```

---

 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
