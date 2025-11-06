# Career Advisor Deep Troubleshooting Guide

## Overview

If you're still seeing "No Insights Available" and "No trending data available yet", follow this step-by-step investigation to identify the exact problem.

## Diagnostic Tools Available

We've created three powerful debugging tools:

### 1. **debug_ai_advisor.py** - Comprehensive System Analysis
Analyzes the entire system state and identifies what's missing.

```bash
python backend/debug_ai_advisor.py
```

Features:
- Shows database statistics
- Analyzes project data
- Inspects skill trends
- Checks user profiles and skills
- Reviews career insights
- Examines recommendations
- Tests generation process
- Exports debug reports

### 2. **live_test_ai_advisor.py** - Interactive Testing
Interactive menu for testing specific components.

```bash
python backend/live_test_ai_advisor.py
```

Features:
- List all users
- Check individual user profiles
- Test insight generation
- Test recommendation generation
- Test trend generation
- Trigger auto-generate manually
- View statistics
- Export debug info

### 3. **verify_ai_advisor.py** - Quick Verification
Quick check and automatic fixes.

```bash
python backend/verify_ai_advisor.py
```

## Step-by-Step Investigation

### Step 1: Run Complete Diagnostic

```bash
cd backend
python debug_ai_advisor.py
```

**What to look for:**

1. **Database Statistics**
   - Users: Should be > 0 ✓
   - Freelancers: Should be > 0 ✓
   - Projects: Should be > 0 (if not, that's the problem!)
   - Open Projects: Should be > 0
   - Skills: Should be > 0 (if not, create sample data)
   - **Skill Trends: Should be > 0** ⚠️ (Problem area #1)
   - **Career Insights: Should be > 0** ⚠️ (Problem area #2)
   - **Recommendations: Should be > 0** ⚠️ (Problem area #3)

2. **Project Analysis**
   - Check if projects have required_skills
   - Verify skill names are valid

### Step 2: Identify Missing Data

Based on diagnostic results:

**If SkillTrend = 0:**
```
Problem: No skill trends have been generated
Solution: Go to Step 3a
```

**If CareerInsight = 0:**
```
Problem: No career insights generated for users
Solution: Go to Step 3b
```

**If Recommendations = 0:**
```
Problem: No recommendations generated for users
Solution: Go to Step 3c
```

**If Projects = 0:**
```
Problem: No projects in database to analyze
Solution: Go to Step 4
```

### Step 3: Regenerate Missing Data

#### 3a: Generate Skill Trends

Using interactive tool:
```bash
python backend/live_test_ai_advisor.py
# Select option 5: Test skill trend generation
```

Expected output:
```
ℹ Found X active projects
✓ Trends generated successfully
Total trends in database: Y
Top 10 Trending Skills:
  • Python: Demand 90%, $4000/proj, 8 projects
  • React: Demand 85%, $3500/proj, 7 projects
  ...
```

If this fails, check:
- Do projects exist? (must have required_skills)
- Are skills properly formatted?
- Check backend logs for errors

#### 3b: Generate Career Insights

Using interactive tool:
```bash
python backend/live_test_ai_advisor.py
# Select option 3: Test single user insight generation
# Enter user email
```

Expected output:
```
✓ Insight generated successfully
Generated Insight Details:
  Current Skills: [skill1, skill2, ...]
  Missing Trending: [skill3, ...]
  Current Rate: $3000
  Potential Rate: $4500
  Days Without Match: 5
  Next Steps: [...]
```

If returns "None", check:
- Does user have skills? (required)
- Are there any skill trends? (if not, generate first)
- Check backend logs

#### 3c: Generate Recommendations

Using interactive tool:
```bash
python backend/live_test_ai_advisor.py
# Select option 4: Test single user recommendation generation
# Enter user email
```

Expected output:
```
ℹ Testing recommendation generation for user@example.com (role: freelancer)
✓ Generated 2 recommendations
  Title: Learn Python - In High Demand
  Description: ...
  Type: trending_skill
  Confidence: 0.85
  Active: True
```

If returns "0 recommendations", check:
- User must have skills to get rate optimization
- Must have missing trending skills
- Check days_without_match threshold (>= 7 days)

### Step 4: Create Sample Projects

If no projects exist:

```bash
python backend/live_test_ai_advisor.py
# Select option 6: Trigger auto-generate
# This will create sample projects
```

Or manually:

```bash
python backend/init_ai_advisor.py
```

This will:
1. Create skill database
2. Generate sample projects
3. Calculate trends
4. Generate insights
5. Generate recommendations

### Step 5: Verify Frontend Integration

Open browser DevTools (F12) → Console and Network tabs.

1. **Navigate to Career Advisor** page
2. **Check Network requests:**
   - `/api/ai/recommendations` - Should return data
   - `/api/ai/career-insight` - Should return data
   - `/api/ai/trending-skills` - Should return data

3. **Check responses:**
   - Status should be 200
   - Response should have `status: "success"`
   - Data counts should be > 0

Example good response:
```json
{
  "status": "success",
  "recommendations": [
    {
      "id": "...",
      "title": "Learn Python - In High Demand",
      "confidence_score": 0.85,
      ...
    }
  ],
  "count": 2
}
```

Example bad response:
```json
{
  "status": "success",
  "recommendations": [],
  "count": 0
}
```

### Step 6: Check Backend Logs

Monitor backend logs while visiting Career Advisor:

```bash
# Terminal running backend should show:
[2024-01-10 15:30:45] Getting recommendations for user: 507f1f77bcf36cd799439011
[2024-01-10 15:30:45] Fetched 2 recommendations for user: 507f1f77bcf36cd799439011
[2024-01-10 15:30:46] Getting career insight for user: 507f1f77bcf36cd799439011
[2024-01-10 15:30:46] Found existing insight: True
[2024-01-10 15:30:46] Returning insight with rate: 3000
```

**No logs appearing?**
- Frontend not making requests
- Check browser console for errors
- Check backend is running

**Logs show error?**
- Get full error trace
- Search for error pattern below

## Common Issues & Solutions

### Issue 1: "No Insights Available" Despite Complete Profile

**Root Cause:** CareerInsight not generated for user

**Solution:**
```bash
python backend/live_test_ai_advisor.py
# Select: 3 (Test single user insight generation)
# Enter user email
```

If it generates successfully, frontend cache might be stale:
- Clear browser cache (Ctrl+Shift+Delete)
- Hard refresh (Ctrl+Shift+R)
- Try incognito window

### Issue 2: No Trending Skills Data

**Root Cause:** SkillTrend not generated from projects

**Check:**
1. Do projects exist?
   ```bash
   python backend/live_test_ai_advisor.py
   # Select: 7 (View database statistics)
   ```
   If Projects = 0, run `python init_ai_advisor.py`

2. Do projects have required_skills?
   ```bash
   python backend/debug_ai_advisor.py
   # Check "PROJECT ANALYSIS" section
   ```

3. Generate trends:
   ```bash
   python backend/live_test_ai_advisor.py
   # Select: 5 (Test skill trend generation)
   ```

### Issue 3: Slow Loading / Timeout

**Root Cause:** Auto-generation taking too long

**Solution:**
- Backend is generating in background (expected first time)
- Wait 20-30 seconds for generation to complete
- Refresh page after auto-generate completes
- Check backend logs for progress

### Issue 4: Empty Recommendations After Insight Exists

**Root Cause:** Insight exists but recommendations not generated

**Check what's blocking:**
```bash
python backend/live_test_ai_advisor.py
# Select: 4 (Test recommendation generation)
# Enter user email
```

Possible reasons:
- User has no skills (need at least 1)
- No trending skills exist (generate trends first)
- User was just created (>= 7 days check)

### Issue 5: API Returns Errors

**In browser Console:**
```
Error: Failed to fetch career insight
```

**Check backend logs:**
```bash
# Should show detailed error trace
ERROR: [error message]
Traceback: ...
```

If you see "Could not generate career insight":
1. Check if user has skills
2. Check if trends exist
3. Run: `python backend/debug_ai_advisor.py` → Test trend generation

### Issue 6: Data Shows for Some Users But Not Others

**Root Cause:** Selective generation or user-specific issue

**Check user profile:**
```bash
python backend/live_test_ai_advisor.py
# Select: 2 (Select and check user)
# Enter user email
```

**Compare with working user:**
- Both should have skills
- Both should be same role
- Check timestamps of insight generation

**Regenerate for specific user:**
```bash
python backend/live_test_ai_advisor.py
# Select: 6 (Trigger auto-generate)
# Enter specific user email
```

## Complete Fresh Start

If nothing works, complete reset:

```bash
# 1. Clear all AI data
python -c "
from models import SkillTrend, CareerInsight, UserRecommendation
SkillTrend.objects.delete()
CareerInsight.objects.delete()
UserRecommendation.objects.delete()
print('Cleared AI data')
"

# 2. Initialize everything
python backend/init_ai_advisor.py

# 3. Verify
python backend/verify_ai_advisor.py

# 4. Test
python backend/live_test_ai_advisor.py
```

## Manual API Testing

If frontend not triggering, test backend directly:

```bash
# Generate all data manually
curl -X POST http://localhost:5000/api/ai/auto-generate

# Should return:
# {
#   "status": "success",
#   "message": "All AI data generated successfully",
#   "summary": {
#     "skill_trends": 20,
#     "career_insights": 5,
#     "recommendations": 12
#   }
# }

# Test individual endpoints (with auth token)
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:5000/api/ai/trending-skills

curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:5000/api/ai/career-insight

curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:5000/api/ai/recommendations
```

## Debug Report Export

For support, export complete diagnostic data:

```bash
python backend/live_test_ai_advisor.py
# Select: 9 (Export full debug info)

# Creates file: ai_advisor_debug_TIMESTAMP.json
# Share this file for support analysis
```

## Validation Checklist

After fixes, verify:

```
☐ Database has skill trends (> 0)
☐ User has at least 1 skill
☐ Career insight generated for user
☐ Recommendations generated for user
☐ Frontend requests show 200 status
☐ Response data has count > 0
☐ Page displays recommendations and insights
☐ Trending skills section shows data
```

## Still Need Help?

Provide the following when seeking support:

1. **Debug Report:**
   ```bash
   python backend/live_test_ai_advisor.py
   # Select 9: Export debug info
   ```

2. **Backend Logs:**
   - Capture logs while visiting Career Advisor page
   - Export to file

3. **User Email:**
   - Provide test account email
   - Confirmation profile is complete

4. **Expected vs Actual:**
   - What should appear
   - What currently appears
   - Steps to reproduce

## Technical Architecture

For developers:

**Data Flow:**
```
User Profile Update
    ↓
[Frontend] Career Advisor page loaded
    ↓
[API] GET /api/ai/recommendations
[API] GET /api/ai/career-insight
[API] GET /api/ai/trending-skills
    ↓
[Service] generate_career_insight()
[Service] generate_recommendations()
[Service] update_skill_trends()
    ↓
[MongoDB] Store data
    ↓
[Frontend] Display insights
```

**Cache Strategy:**
- Recommendations: 30 minutes
- Career Insights: 1 hour
- Trending Skills: 5 minutes

Clear cache by restarting backend.

---

**Last Updated:** 2024
**Status:** Comprehensive debugging system available
