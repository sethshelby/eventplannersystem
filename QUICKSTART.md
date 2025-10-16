# Quick Start Guide - Working with Your Team 🚀

## 📝 TO-DO RIGHT NOW:

### Step 1: Add Your Friends on GitHub (2 minutes)
1. Open this link: https://github.com/sethshelby/eventplannersystem/settings/access
2. Click the green **"Add people"** button
3. Type your friends' GitHub usernames:
   - Friend 1: _____________
   - Friend 2: _____________
   - Friend 3: _____________
4. Click **"Add to this repository"**
5. Done! They'll get an email invitation

### Step 2: Tell Your Friends to Accept & Clone
Send them this message:

```
Hey! I added you to our Event Planner project on GitHub.

1. Check your email and accept the invitation
2. Clone the project:
   git clone https://github.com/sethshelby/eventplannersystem.git
   cd eventplannersystem

3. You're ready! Just remember:
   - BEFORE working: git pull origin main
   - AFTER changes: ./sync.sh (or manually commit and push)
```

---

## 🎯 Easy Sync Tool (USE THIS!)

I created a simple script for you. Just run:

```bash
cd /Users/nuonaron/Downloads/ravid
./sync.sh
```

This will:
- Pull latest changes from GitHub
- Show you what's changed
- Let you commit and push your changes easily

---

## ⚡ Quick Commands

### Start Working:
```bash
cd /Users/nuonaron/Downloads/ravid
git pull origin main
```

### Save & Share Your Work:
```bash
git add .
git commit -m "What you changed"
git push origin main
```

### Or Just Use:
```bash
./sync.sh
```

---

## 🎓 For Your Friends

After they clone the repo, they should:

1. **Before working each time:**
   ```bash
   cd eventplannersystem
   git pull origin main
   ```

2. **After making changes:**
   ```bash
   ./sync.sh
   ```
   Or manually:
   ```bash
   git add .
   git commit -m "Description"
   git push origin main
   ```

---

## ✅ You're All Set!

The only thing YOU need to do manually is:
**→ Go to GitHub and add your friends as collaborators (Step 1 above)**

Everything else is ready! 🎉

---

**Need help?** Check COLLABORATION.md for detailed instructions.

