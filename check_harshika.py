import sys
sys.path.insert(0, 'backend')
from app import create_app
from models import User, CareerInsight, SkillRecommendation
from ai_advisor_service import AIAdvisorService

app = create_app()

with app.app_context():
    user = User.objects(first_name__icontains='harshika', last_name__icontains='sri').first()
    
    if user:
        print(f"✓ Found user: {user.first_name} {user.last_name} (ID: {user.id})")
        print(f"  Email: {user.email}")
        print(f"  Role: {user.role}")
        
        insights = CareerInsight.objects(user=user)
        recommendations = SkillRecommendation.objects(user=user)
        
        print(f"\nCareer Insights: {insights.count()}")
        print(f"Recommendations: {recommendations.count()}")
        
        print("\n--- Triggering insight generation ---")
        service = AIAdvisorService()
        
        try:
            if insights.count() == 0:
                print("Generating career insights...")
                insights_result = service.generate_career_insight(str(user.id))
                print(f"✓ Insights generated")
        except Exception as e:
            print(f"✗ Error generating insights: {e}")
        
        try:
            if recommendations.count() == 0:
                print("Generating recommendations...")
                recs_result = service.generate_personalized_recommendations(str(user.id))
                print(f"✓ Recommendations generated: {len(recs_result) if recs_result else 0}")
        except Exception as e:
            print(f"✗ Error generating recommendations: {e}")
        
        print("\n--- Data after generation ---")
        insights = CareerInsight.objects(user=user)
        recommendations = SkillRecommendation.objects(user=user)
        print(f"Career Insights: {insights.count()}")
        print(f"Recommendations: {recommendations.count()}")
    else:
        print("✗ User 'harshika sri' not found")
        users = User.objects.only('first_name', 'last_name', 'email', 'role')
        print(f"\nTotal users in database: {users.count()}")
        print("\nSearching for similar names...")
        harshika_users = User.objects(first_name__icontains='harshika')
        if harshika_users:
            print(f"Found {harshika_users.count()} users with 'harshika':")
            for u in harshika_users:
                print(f"  - {u.first_name} {u.last_name} ({u.role})")
        else:
            print("No users with 'harshika' found. Showing first 10 users:")
            for u in users[:10]:
                print(f"  - {u.first_name} {u.last_name} ({u.role})")
