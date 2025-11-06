# Top Trending Skills Feature - Quick Start Guide

## ✅ Feature Status: ENABLED & OPERATIONAL

---

## 🚀 Get Started in 3 Steps

### Step 1: Ensure Backend is Running
```bash
cd backend
python app.py
```

### Step 2: Populate Trending Skills Data
```bash
cd backend
python populate_trending_skills.py
```

### Step 3: View Trending Skills
1. Open WorkConnect platform
2. Login
3. Navigate to **Grow and Earn AI** (Career Advisor)
4. Click **Market Trends** tab
5. See trending skills with demand scores!

---

## 📊 What You'll See

**Top Trending Skills Card** displays:
- **Skill Ranking** (1, 2, 3...)
- **Skill Name** with category
- **Trend Indicator**: 
  - 📈 Rising demand
  - ➡️ Stable demand  
  - 📉 Declining demand
- **Demand Score**: 0-100% bar chart
- **Average Project Rate**: $/project
- **Project Count**: How many projects need this skill

---

## 🔄 How It Works

1. **Collects**: All OPEN and IN_PROGRESS projects
2. **Extracts**: Required skills + project budgets
3. **Calculates**: Demand score, average rate, trend
4. **Updates**: SkillTrend database in real-time
5. **Serves**: Via `/api/ai/trending-skills` API
6. **Displays**: In CareerAdvisor UI with visualizations

---

## 📈 Example Output

```
Top Trending Skills

1. React 📈
   Demand Score: ████████████████████ 100%
   Average Rate: $5,167/proj
   8 open projects requiring this skill

2. Node.js ➡️
   Demand Score: ██████████████░░░░░░ 67%
   Average Rate: $5,500/proj
   6 open projects requiring this skill

3. Python ➡️
   Demand Score: ██████████░░░░░░░░░░ 50%
   Average Rate: $4,500/proj
   5 open projects requiring this skill
```

---

## 🎯 Use Cases

**For Freelancers:**
- Identify high-demand skills in your market
- See what competitors are building
- Plan skill development strategy
- Understand fair market rates

**For Clients:**
- Discover available skill supply
- Plan project requirements
- Benchmark against market rates

**For Platform:**
- Show real market intelligence
- Provide data-driven guidance
- Competitive differentiation

---

## 🔧 Verify It's Working

### Check API Directly
```bash
curl http://localhost:5000/api/ai/trending-skills?limit=10
```

Expected response:
```json
{
  "status": "success",
  "skills": [
    {
      "skill_name": "React",
      "demand_score": 100.0,
      "frequency": 8,
      "average_rate": 5167.0,
      "trending_direction": "rising"
    }
  ],
  "count": 8
}
```

### Check Database
```bash
cd backend
python -c "
from models import SkillTrend
from mongoengine import connect
from config import Config

connect(db=Config.MONGODB_DB_NAME, host=Config.MONGODB_URI)
trends = SkillTrend.objects.order_by('-demand_score')[:5]
for t in trends:
    print(f'{t.skill_name}: {t.demand_score:.1f}% (Freq: {t.frequency})')
"
```

---

## 🆘 Troubleshooting

### No Trending Data Showing?

1. **Check Projects Exist**
   ```bash
   python -c "
   from models import Project, ProjectStatus
   from mongoengine import connect
   from config import Config
   
   connect(db=Config.MONGODB_DB_NAME, host=Config.MONGODB_URI)
   active = Project.objects(status__in=['OPEN', 'IN_PROGRESS']).count()
   print(f'Active projects: {active}')
   "
   ```

2. **Run Population Script**
   ```bash
   python populate_trending_skills.py
   ```

3. **Restart Backend**
   ```bash
   # Kill existing process and restart
   python app.py
   ```

4. **Clear Cache**
   - Backend caches for 5 minutes
   - Use `Ctrl+F5` to clear browser cache
   - Wait a moment and refresh

### Still Not Working?

1. Check MongoDB connection in `.env`
2. Verify `SkillTrend` collection exists
3. Run verification script:
   ```bash
   python verify_trending_and_start.py
   ```

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| `backend/models.py:616` | SkillTrend database model |
| `backend/ai_advisor_routes.py:236` | Trending skills API endpoint |
| `backend/ai_advisor_service.py:22` | Trend calculation logic |
| `src/pages/CareerAdvisor.tsx:417` | UI display component |
| `src/hooks/use-ai-advisor.ts:109` | API integration hook |
| `backend/populate_trending_skills.py` | Data population script |
| `TRENDING_SKILLS_IMPLEMENTATION.md` | Full technical documentation |

---

## 📞 API Reference

### Get Trending Skills
```
GET /api/ai/trending-skills?limit=10
```

**Parameters:**
- `limit` (optional): Number of skills to return (default: 10, max: 100)

**Response:**
```json
{
  "status": "success",
  "skills": [
    {
      "id": "mongo_id",
      "skill_name": "React",
      "category": "Frontend",
      "demand_score": 100.0,
      "frequency": 8,
      "average_rate": 5167.0,
      "trending_direction": "rising",
      "last_updated": "2025-10-28T10:00:00"
    }
  ],
  "count": 8,
  "cached": true
}
```

---

## 🎉 Success Checklist

- [ ] Backend is running
- [ ] Projects exist with required_skills
- [ ] Trending skills populated in database
- [ ] API endpoint responds with data
- [ ] CareerAdvisor page loads without errors
- [ ] Market Trends tab shows skills
- [ ] Demand scores are visible
- [ ] Trend indicators display correctly

---

## 📝 Notes

- **Cache Duration**: 5 minutes per API call
- **Auto-Update**: When projects are created/modified
- **Real Data**: Uses actual project requirements + budgets
- **No Manual Entry**: Fully automated aggregation
- **Scalable**: Handles 1000+ projects efficiently

---

**Status**: ✅ **FULLY ENABLED & READY TO USE**
