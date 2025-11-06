#!/usr/bin/env python
import os
import sys
from pathlib import Path

os.chdir(Path(__file__).parent)
sys.path.insert(0, 'backend')

try:
    from app import create_app
    from models import User, CareerInsight, SkillRecommendation
    from ai_advisor_service import AIAdvisorService
    
    app = create_app()
    
    with app.app_context():
        print("Searching for 'harshika sri'...")
        user = User.objects(first_name__icontains='harshika', last_name__icontains='sri').first()
        
        if not user:
            print("Not found with exact match. Searching for variations...")
            user = User.objects(first_name__icontains='harshika').first()
            if not user:
                print("No users with 'harshika' in first name.")
                all_users = User.objects.limit(5)
                print(f"Sample users in DB: {all_users.count()}")
                for u in all_users:
                    print(f"  - {u.first_name} {u.last_name}")
                sys.exit(1)
        
        print(f"\nUser found: {user.first_name} {user.last_name}")
        print(f"Role: {user.role}")
        
        insights = CareerInsight.objects(user=user).count()
        recommendations = SkillRecommendation.objects(user=user).count()
        print(f"Career Insights: {insights}")
        print(f"Recommendations: {recommendations}")
        
        if insights == 0 or recommendations == 0:
            print("\nGenerating missing data...")
            service = AIAdvisorService()
            
            if insights == 0:
                try:
                    service.generate_career_insight(str(user.id))
                    print("✓ Career insights generated")
                except Exception as e:
                    print(f"✗ Error: {e}")
            
            if recommendations == 0:
                try:
                    service.generate_personalized_recommendations(str(user.id))
                    print("✓ Recommendations generated")
                except Exception as e:
                    print(f"✗ Error: {e}")
            
            # Verify
            insights = CareerInsight.objects(user=user).count()
            recommendations = SkillRecommendation.objects(user=user).count()
            print(f"\nAfter generation:")
            print(f"Career Insights: {insights}")
            print(f"Recommendations: {recommendations}")
        else:
            print("\n✓ User already has insights and recommendations")

except Exception as e:
    import traceback
    print(f"Error: {e}")
    traceback.print_exc()
