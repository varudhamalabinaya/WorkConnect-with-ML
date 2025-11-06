# Career Advisor - Quick Debug Start Guide

## 🚀 Start Here - Immediate Steps

### Step 1: Run Comprehensive Diagnostic (2 minutes)

```bash
cd backend
python debug_ai_advisor.py
```

This will show you:
- ✓ What data exists in database
- ✓ What's missing
- ✓ Whether generation works

### Step 2: Interactive Testing (5 minutes)

```bash
python live_test_ai_advisor.py
```

Then select from menu:
- **Option 7** - View all statistics
- **Option 3** - Test insight for specific user
- **Option 5** - Test trend generation
- **Option 6** - Manually trigger auto-generate

### Step 3: Frontend Verification (2 minutes)

1. Open Career Advisor page in browser
2. Press F12 → Console tab
3. Check for error messages
4. Press F12 → Network tab
5. Reload page
6. Look for requests:
   - `/api/ai/recommendations` → Should show data
   - `/api/ai/career-insight` → Should show data
   - `/api/ai/trending-skills` → Should show data

## 🎯 Common Quick Fixes

### "No Insights Available"

**Quick Fix:**
```bash
python backend/live_test_ai_advisor.py
# Select 6: Trigger auto-generate
# Enter your user email
```

Wait 10-20 seconds, then refresh Career Advisor page.

### "No Trending Data Available"

**Check if projects exist:**
```bash
python backend/live_test_ai_advisor.py
# Select 7: View statistics
# Look for "Projects: X"
```

If 0 projects:
```bash
python backend/init_ai_advisor.py
```

If projects exist, regenerate trends:
```bash
python backend/live_test_ai_advisor.py
# Select 5: Test skill trend generation
```

### Still Broken After All Steps?

Run full diagnostic and save output:
```bash
cd backend
python debug_ai_advisor.py > debug_output.txt 2>&1
python live_test_ai_advisor.py > test_output.txt 2>&1
```

Share these files for support.

## 🔍 Advanced Diagnostics

### Check Specific User

```bash
python backend/live_test_ai_advisor.py
# Select 2: Select and check user
# Enter: your_email@example.com
```

Shows:
- Skills count
- Whether insight exists
- Number of recommendations

### Manually Regenerate Everything

```bash
python backend/live_test_ai_advisor.py
# Select 6: Trigger auto-generate
# Press Enter (empty) for all users
```

### Export Debug Report

```bash
python backend/live_test_ai_advisor.py
# Select 9: Export debug info
# Creates: ai_advisor_debug_TIMESTAMP.json
```

## 📊 What Should Exist in Database

Run this to check:
```bash
python backend/live_test_ai_advisor.py
# Select 7: View statistics

# Should show:
✓ Users: > 0
✓ Freelancers: > 0
✓ Projects: > 0
✓ Skills: > 0
✓ Skill Trends: > 0 (if not, run debug_ai_advisor.py)
✓ Career Insights: > 0 (if not, trigger auto-generate)
✓ Recommendations: > 0 (if not, trigger auto-generate)
```

## 🚨 If Nothing Works

Complete reset:

```bash
# 1. Run diagnostic
python backend/debug_ai_advisor.py

# 2. Run initialization
python backend/init_ai_advisor.py

# 3. Verify everything
python backend/verify_ai_advisor.py

# 4. Visit Career Advisor page
# Should now show data
```

## 📱 Frontend Checks

1. **Clear browser cache:**
   - Chrome: Ctrl+Shift+Delete
   - Firefox: Ctrl+Shift+Delete

2. **Hard refresh:**
   - Ctrl+Shift+R or Cmd+Shift+R

3. **Incognito window:**
   - Ctrl+Shift+N (Chrome) or Ctrl+Shift+P (Firefox)

4. **Check browser console for errors:**
   - F12 → Console → Look for red errors

## ✅ Success Indicators

✓ Career Advisor page loads in < 2 seconds
✓ "Your Position" card shows market standing
✓ "Rate Analysis" shows current and potential rate
✓ "Skills Analysis" shows current and missing skills
✓ "Next Career Steps" shows 3+ recommendations
✓ "Market Trends" shows 5+ trending skills
✓ "Recommendations" tab shows 1+ recommendations

## 🔧 Key Files

- **debug_ai_advisor.py** - Full system analysis
- **live_test_ai_advisor.py** - Interactive testing
- **verify_ai_advisor.py** - Quick fixes
- **init_ai_advisor.py** - Initialize data
- **CAREER_ADVISOR_DEEP_TROUBLESHOOTING.md** - Detailed guide

## 📞 Need Help?

Provide:
1. Output from `python debug_ai_advisor.py`
2. Your user email
3. Screenshot of Career Advisor page
4. Browser console errors (if any)

---

**Start with Step 1 above and follow the prompts. Usually fixed in 5-10 minutes.**
