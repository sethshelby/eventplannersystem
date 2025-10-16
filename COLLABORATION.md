# Git Collaboration Guide 🤝

## For the Project Owner (You)

### 1. Add Your Friends as Collaborators
1. Go to your GitHub repository: https://github.com/sethshelby/eventplannersystem
2. Click on **Settings** tab
3. Click on **Collaborators** in the left sidebar
4. Click **Add people**
5. Enter your friend's GitHub username or email
6. They will receive an invitation email

### 2. Working on the Project

#### Making Changes
```bash
# Always pull the latest changes before working
cd /Users/nuonaron/Downloads/ravid
git pull origin main

# Make your changes to the code
# ...

# Stage your changes
git add .

# Commit with a descriptive message
git commit -m "Description of what you changed"

# Push to GitHub
git push origin main
```

---

## For Your Friends

### 1. Accept Collaboration Invitation
- Check your email for the GitHub invitation
- Click **Accept Invitation**

### 2. Clone the Repository (First Time Only)
```bash
git clone https://github.com/sethshelby/eventplannersystem.git
cd eventplannersystem
```

### 3. Working on the Project

#### Before Starting Work
```bash
# Always pull the latest changes first
git pull origin main
```

#### After Making Changes
```bash
# Check what files you changed
git status

# Stage your changes
git add .

# Commit with a clear message
git commit -m "Added new feature: [describe what you did]"

# Push your changes
git push origin main
```

---

## 🔄 Real-Time Collaboration Workflow

### Best Practices

1. **Always Pull Before You Start Working**
   ```bash
   git pull origin main
   ```

2. **Commit Often with Clear Messages**
   ```bash
   git commit -m "Fixed login bug"
   git commit -m "Added new store feature"
   git commit -m "Updated schedule display"
   ```

3. **Push Regularly**
   ```bash
   git push origin main
   ```

4. **Communicate with Your Team**
   - Tell others what you're working on
   - Avoid working on the same file at the same time
   - Use descriptive commit messages

### Handling Merge Conflicts

If you and a friend edit the same file, you might get a merge conflict:

```bash
# Pull the latest changes
git pull origin main

# If there's a conflict, Git will tell you which files
# Open the conflicted files and look for:
<<<<<<< HEAD
Your changes
=======
Their changes
>>>>>>> main

# Edit the file to keep what you want
# Remove the conflict markers (<<<, ===, >>>)

# Stage the resolved files
git add .

# Commit the merge
git commit -m "Resolved merge conflict"

# Push
git push origin main
```

---

## 📱 Staying in Sync

### Quick Sync Command
Create an alias to make syncing easier:

```bash
# Pull latest changes, then push your changes
git pull origin main && git add . && git commit -m "Update" && git push origin main
```

### Check Status Anytime
```bash
# See what's changed locally
git status

# See commit history
git log --oneline -10

# See what others have done
git pull origin main --dry-run
```

---

## 🚨 Emergency Commands

### Undo Last Commit (Before Push)
```bash
git reset --soft HEAD~1
```

### Discard All Local Changes
```bash
git reset --hard origin/main
```

### See What Changed in Last Commit
```bash
git show
```

---

## 💡 Pro Tips

1. **Pull before every work session**
2. **Commit small, logical changes**
3. **Write clear commit messages**
4. **Push at the end of your work session**
5. **Use branches for big features** (advanced)

---

## 🔧 Useful Git Commands Cheat Sheet

| Command | What It Does |
|---------|-------------|
| `git status` | See what files have changed |
| `git pull origin main` | Get latest changes from GitHub |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Save changes with a message |
| `git push origin main` | Upload changes to GitHub |
| `git log` | See commit history |
| `git diff` | See what changed in files |

---

## Need Help?

If you're stuck:
1. Run `git status` to see what's happening
2. Google the error message
3. Ask in your team chat
4. Check GitHub's help: https://docs.github.com

**Remember:** The key to real-time collaboration is **communication** and **frequent pulls/pushes**! 🚀

