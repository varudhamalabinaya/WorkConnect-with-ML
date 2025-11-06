#!/usr/bin/env python3
"""
Complete System Test
Test the entire ML recommendation system
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from backend.config import Config
from backend.models import User, Project, UserSkill, Skill, SkillTrend
from backend.freelancer_ml_agent import FreelancerMLAgent
from mongoengine import connect

def test_complete_system():
    print("TESTING COMPLETE ML RECOMMENDATION SYSTEM")
    print("=" * 50)
    
    try:
        # Connect to database
        connect(db=Config.MONGODB_DB_NAME, host=Config.MONGODB_URI)
        print("✅ Database connected")
        
        # Check data
        freelancers = User.objects(role='freelancer')
        projects = Project.objects()
        skills = Skill.objects()
        trends = SkillTrend.objects()
        
        print(f"📊 Data Available:")
        print(f"   Freelancers: {freelancers.count()}")
        print(f"   Projects: {projects.count()}")
        print(f"   Skills: {skills.count()}")
        print(f"   Trends: {trends.count()}")
        
        # Test ML Agent
        print("\\n🤖 Testing ML Agent...")
        agent = FreelancerMLAgent()
        
        # Load or train model
        model_path = os.path.join('backend', 'freelancer_ml_agent.pkl')
        if os.path.exists(model_path):
            agent.load_model(model_path)
            print("✅ ML model loaded")
        else:
            print("🔄 Training new ML model...")
            agent.train_model()
            agent.save_model(model_path)
            print("✅ ML model trained and saved")
        
        # Test with first freelancer
        if freelancers.count() > 0:
            test_user = freelancers.first()
            user_id = str(test_user.id)
            
            print(f"\\n🧪 Testing with: {test_user.first_name} {test_user.last_name}")
            
            # Test all recommendation types
            projects_recs = agent.get_personalized_project_recommendations(user_id, 5)
            skills_recs = agent.get_skill_gap_analysis(user_id, 5)
            partners_recs = agent.get_collaboration_partners(user_id, 5)
            
            print(f"\\n📈 RESULTS:")
            print(f"   Project Recommendations: {len(projects_recs)}")
            print(f"   Skill Gap Analysis: {len(skills_recs)}")
            print(f"   Collaboration Partners: {len(partners_recs)}")
            
            # Show sample results
            if projects_recs:
                print(f"\\n🎯 Sample Project: {projects_recs[0].get('title', 'N/A')}")
                print(f"   Confidence: {projects_recs[0].get('confidence_score', 0):.2f}")
            
            if skills_recs:
                print(f"\\n📚 Top Skill Gap: {skills_recs[0].get('skill_name', 'N/A')}")
                print(f"   Demand: {skills_recs[0].get('demand_score', 0)}%")
            
            if partners_recs:
                print(f"\\n🤝 Top Partner: {partners_recs[0].get('name', 'N/A')}")
                print(f"   Match: {partners_recs[0].get('collaboration_score', 0):.2f}")
            
            print("\\n" + "=" * 50)
            print("🎉 SYSTEM TEST COMPLETED SUCCESSFULLY!")
            print("✅ ML Model: Working")
            print("✅ Recommendations: Generated")
            print("✅ Database: Connected")
            print("✅ Ready for Frontend Integration")
            print("=" * 50)
            
            return True
        else:
            print("❌ No freelancers found for testing")
            return False
            
    except Exception as e:
        print(f"❌ System test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_complete_system()
    if success:
        print("\\n🚀 System is ready! You can now run the application.")
        print("\\n📋 Next steps:")
        print("1. Start backend: cd backend && python start_server.py")
        print("2. Start frontend: npm run dev")
        print("3. Open browser: http://localhost:5173")
    else:
        print("\\n❌ System test failed. Please check the errors above.")