# Trending Skills Setup Guide

## ✅ Setup Complete

Your WorkConnect platform now has default trending skills data that will be displayed for all user roles.

### Default Trending Skills Data

| Rank | Skill | Demand Score | Category |
|------|-------|--------------|----------|
| 1 | Python | 95% | Programming |
| 2 | Machine Learning | 90% | AI/ML |
| 3 | Web Development | 85% | Development |
| 4 | JavaScript | 83% | Programming |
| 5 | Data Analysis | 80% | Analytics |
| 6 | Cloud Computing | 78% | Infrastructure |
| 7 | Django | 75% | Framework |
| 8 | ReactJS | 73% | Frontend |
| 9 | AI & Deep Learning | 70% | AI/ML |
| 10 | UI/UX Design | 68% | Design |

## How to Start the Platform

1. **Start Backend with Trending Skills:**
   ```bash
   # Run this from the project root
   start_with_trending_skills.bat
   ```

2. **Start Frontend:**
   ```bash
   npm run dev
   ```

3. **Access Career Advisor:**
   - Login with any user account
   - Navigate to Career Advisor page
   - Click on "Market Trends" tab
   - View the trending skills data

## API Endpoints

- `GET /api/ai/trending-skills?limit=10` - Get trending skills (no auth required)
- `POST /api/ai/update-trends` - Update trends from project data
- `GET /api/ai/health` - Health check

## Future Dynamic Data Integration

To transition from static to dynamic data:

1. **Real-time Updates:** The system will automatically analyze project postings and update skill demand scores
2. **API Integration:** Connect external job market APIs for broader industry data
3. **Machine Learning:** Implement ML models to predict trending skills
4. **Automated Refresh:** Set up scheduled tasks to refresh data periodically

## Troubleshooting

If trending skills don't appear:

1. **Re-seed Data:**
   ```bash
   cd backend
   python seed_default_trending_skills.py
   ```

2. **Verify Data:**
   ```bash
   python verify_trending_skills.py
   ```

3. **Check API:**
   ```bash
   python test_api_endpoints.py
   ```

## Files Modified

- `backend/seed_default_trending_skills.py` - Seeds default data
- `backend/ai_advisor_routes.py` - Updated trending skills endpoint
- `src/pages/CareerAdvisor.tsx` - Enhanced UI for trending skills
- `start_with_trending_skills.bat` - Startup script

The trending skills data is now available to all user roles and will display consistently across the platform.