"""
Plantix - AI Farming Assistant Test Script
Created by TejasS1233
"""

from agentic_ai.crew import AgenticAi

def main():
    print("=" * 70)
    print("🌱 PLANTIX - AI Farming Assistant - Test Run 🌱")
    print("=" * 70)
    print()
    print("Testing with a sample crop disease scenario...")
    print()
    
    # Sample test case: Tomato Late Blight
    inputs = {
        'crop_type': 'Tomato',
        'symptoms': '''Water-soaked spots appearing on lower leaves, 
                      white powdery fungal growth on leaf undersides, 
                      rapid browning and wilting of foliage,
                      dark brown lesions on stems,
                      some fruits showing brown patches''',
        'environment': '''High humidity (around 80-90%), 
                         temperature range 18-22°C,
                         recent heavy rains for 3 days,
                         poor air circulation in greenhouse,
                         plants are densely planted''',
        'growth_stage': 'Flowering stage, plants are approximately 60 days old',
        'location': 'Maharashtra, India (subtropical monsoon climate)'
    }
    
    print("📋 Test Case Details:")
    print(f"   Crop: {inputs['crop_type']}")
    print(f"   Location: {inputs['location']}")
    print(f"   Stage: {inputs['growth_stage']}")
    print()
    print("🔍 Running Plantix AI Analysis...")
    print("   This may take 2-5 minutes as the AI agents work together...")
    print("=" * 70)
    print()
    
    try:
        result = AgenticAi().crew().kickoff(inputs=inputs)
        
        print()
        print("=" * 70)
        print("✅ Analysis Complete!")
        print("=" * 70)
        print()
        print("📄 A detailed farming report has been saved to:")
        print("   📁 plantix_farming_report.md")
        print()
        print("The report includes:")
        print("   ✓ Disease diagnosis with confidence level")
        print("   ✓ Treatment recommendations (organic & chemical)")
        print("   ✓ Prevention strategies")
        print("   ✓ General farming advice")
        print()
        print("You can now open the report file to view the complete analysis.")
        print()
        
        return result
        
    except Exception as e:
        print()
        print("❌ Error occurred during analysis:")
        print(f"   {str(e)}")
        print()
        print("Troubleshooting tips:")
        print("   1. Check your .env file has a valid API key")
        print("   2. Ensure you have internet connectivity")
        print("   3. Verify all dependencies are installed: pip install -e .")
        print()
        raise


if __name__ == "__main__":
    main()
