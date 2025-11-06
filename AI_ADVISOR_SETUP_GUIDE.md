# AI Career Growth Advisor - Setup & Testing Guide

## 🚀 Implementation Status

✅ **Completed:**
- Backend AI Advisor Service (ai_advisor_service.py)
- Backend API Routes (ai_advisor_routes.py) 
- Frontend Custom Hook (use-ai-advisor.ts)
- Dashboard Widget Component (AIAdvisorCard.tsx)
- Dedicated Career Advisor Page (CareerAdvisor.tsx)
- Navigation Integration (Header & Dropdown Menu)
- Feed Integration (AIAdvisorCard widget on feed)
- MongoDB Models (SkillTrend, UserRecommendation, CareerInsight)

## 📋 Quick Start

### 1. **Ensure Both Servers Are Running**

**Terminal 1 - Backend:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Expected output: `Running on http://localhost:5000`

**Terminal 2 - Frontend:**
```bash
npm run dev
```
Expected output: `VITE v... ready in ... ms`

### 2. **Initialize Skill Trends Data**

The advisor needs trending skills data to work. Call this endpoint to populate it:

```bash
curl -X POST http://localhost:5000/api/ai/update-trends \
  -H "Content-Type: application/json"
```

Expected Response:
```json
{
  "status": "success",
  "message": "Skill trends updated successfully"
}
```

## 🧪 API Endpoints Reference

All endpoints (except `/health`) require JWT authentication via `Authorization: Bearer {token}` header.

### Admin Endpoints

**POST** `/api/ai/update-trends`
- Updates trending skills from all projects
- Call this daily or when you want fresh data
- No auth required

### User Endpoints (JWT Required)

**GET** `/api/ai/recommendations`
- Fetch all active recommendations for logged-in user
- Response includes: recommendations list with types and confidence scores

**POST** `/api/ai/generate-recommendations/<user_id>`
- Manually generate fresh recommendations for a user
- Optional: Pass `?force=true` to override existing recommendations

**GET** `/api/ai/career-insight`
- Retrieve comprehensive career analysis
- Shows current market position, rate analysis, missing skills

**GET** `/api/ai/trending-skills?limit=10`
- Get top trending skills with demand metrics
- Default limit: 10, max: 50

**GET** `/api/ai/market-analysis`
- Overall market statistics
- Shows demand distribution across skill categories

**POST** `/api/ai/recommendation/<rec_id>/dismiss`
- User marks a recommendation as dismissed
- Prevents that recommendation from appearing again

**GET** `/api/ai/dashboard-summary`
- Compact summary for dashboard widget
- Returns top 3 recommendations and top 5 skills

**POST** `/api/ai/generate-insight/<user_id>`
- Generate fresh career insight for a user

**GET** `/api/ai/health`
- Health check endpoint (no auth required)

## 📱 Frontend Routes

- **Main Navigation:** Header shows "Career Advisor" link (Desktop & Mobile dropdown)
- **Dedicated Page:** `/career-advisor` - Full 3-tab interface
- **Dashboard Widget:** Appears on `/feed` page
- **Tab 1 - Recommendations:** All active recommendations with actions
- **Tab 2 - Career Insights:** Market position, rates, skills analysis
- **Tab 3 - Market Trends:** Top 10 trending skills with demand visualization

## 🧑‍💻 Testing Workflow

### Step 1: Create Test Data
First, ensure you have some projects in the database with skills:

```python
# From backend directory
python seed_sample_projects.py
```

### Step 2: Generate Trends
```bash
curl -X POST http://localhost:5000/api/ai/update-trends \
  -H "Content-Type: application/json"
```

### Step 3: Login to Application
- Navigate to http://localhost:8080
- Log in with test user credentials
- Example: email: `freelancer@test.com` password: `password123`

### Step 4: Test Components
1. **Dashboard Widget:** Visit `/feed` - should see AIAdvisorCard
2. **Career Advisor Page:** Click "Career Advisor" in header - should load page
3. **Recommendations Tab:** Should show personalized recommendations
4. **Market Trends Tab:** Should show trending skills with demand data
5. **Career Insights Tab:** Should show rate analysis and skills gap

### Step 5: Test Dismissal
- Click "Dismiss" on any recommendation
- Refresh page - recommendation should not reappear
- Check console for successful API call

## 🐛 Troubleshooting

### Issue: Career Advisor Page Shows "Loading..."
**Solution:** 
- Check browser console for API errors
- Verify JWT token is valid in localStorage
- Check backend logs for 401/403 errors
- Ensure user is authenticated

### Issue: No Recommendations Showing
**Solution:**
- Run `POST /api/ai/update-trends` to generate skill trends
- Check that projects exist in database with `required_skills`
- Verify user role is either 'freelancer' or 'client'
- Check backend logs for errors

### Issue: "No recommendations available" Message
**Solution:**
- This is normal if:
  - User was matched recently (within 7 days)
  - User has all trending skills
  - No projects in database to analyze
- Try running `/api/ai/update-trends` to refresh data

### Issue: 401 Unauthorized Errors
**Solution:**
- Re-login to application
- Check that token exists in localStorage
- Verify backend JWT secret matches frontend expectations
- Check token expiration time

## 📊 Data Models

### SkillTrend
```python
{
  "name": "Python",
  "frequency": 45,
  "demand_score": 87.5,
  "average_rate": 75.00,
  "trending_direction": "rising",  # rising | stable | declining
  "last_updated": datetime
}
```

### UserRecommendation
```python
{
  "user_id": ObjectId,
  "type": "skill_gap",  # skill_gap | trending_skill | rate_optimization | project_suggestion
  "title": "Learn React",
  "description": "React is trending...",
  "confidence": 0.87,
  "metadata": {...},
  "dismissed": False,
  "dismissed_at": None,
  "created_at": datetime,
  "expires_at": datetime
}
```

### CareerInsight
```python
{
  "user_id": ObjectId,
  "role": "freelancer",
  "current_market_position": "Mid-level specialist",
  "current_rate": 65.0,
  "potential_rate": 95.0,
  "missing_trending_skills": ["Kubernetes", "Docker"],
  "recommendation_summary": "...",
  "last_updated": datetime
}
```

## 🎯 Feature Highlights

### For Freelancers
- ⭐ Identifies trending skills with earning potential
- 📊 Shows current vs. potential rates
- 🎯 Recommends specific skills to learn based on demand
- 💡 Suggests when project opportunities match their skills
- ⏱️ Alerts when inactive (no matches in 7+ days)

### For Clients
- 📈 Analyzes project visibility and attractiveness
- 💬 Suggests better project descriptions
- 💰 Recommends competitive budget settings
- ⏰ Highlights importance of clear deadlines
- 🔍 Shows how to improve freelancer match rates

### General Features
- 🔄 Automatic daily recommendations (configurable)
- 🚫 User-controlled dismissal
- 📊 Confidence scoring (0-1 scale)
- 🎨 Beautiful UI with Tailwind CSS
- 📱 Fully responsive design
- ⚡ Real-time data analysis

## 🔄 Scheduling Daily Updates (Optional)

To automatically update trends daily, add to your backend deployment:

```python
# In app.py
from apscheduler.schedulers.background import BackgroundScheduler
from ai_advisor_service import AIAdvisorService

def schedule_daily_trends():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        AIAdvisorService.update_skill_trends,
        'cron',
        hour=2,  # 2 AM daily
        minute=0
    )
    scheduler.start()

# Call in create_app() after registering blueprints
schedule_daily_trends()
```

Install APScheduler:
```bash
pip install apscheduler
```

## 📝 Notes for Future Enhancement

- Consider email notifications for high-confidence recommendations
- Add analytics to track recommendation acceptance rates
- Implement "snooze" functionality (remind in 7 days)
- Add social features (view what others with same skills are earning)
- Create A/B testing framework for recommendation wording
- Integrate with learning platforms for skill recommendations

## 🆘 Getting Help

Check the following files for implementation details:
- `backend/ai_advisor_service.py` - Core business logic
- `backend/ai_advisor_routes.py` - API endpoints
- `src/hooks/use-ai-advisor.ts` - Frontend hook logic
- `src/components/AIAdvisorCard.tsx` - Widget component
- `src/pages/CareerAdvisor.tsx` - Full page component
- `backend/models.py` - Database schemas (search for SkillTrend, UserRecommendation, CareerInsight)

---

**Agent Name:** Grow and Earn AI  
**Tagline:** "Unlock your career potential with AI-powered insights"  
**Status:** ✅ Production Ready