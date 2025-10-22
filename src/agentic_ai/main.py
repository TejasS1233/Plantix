"""
Plantix - AI Farming Assistant
Created by TejasS1233
"""

import sys
import warnings
from datetime import datetime
from agentic_ai.crew import AgenticAi

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """Run the Plantix crop disease diagnosis and farming assistant crew."""
    
    print("=" * 70)
    print("🌱 PLANTIX - AI-based Crop Disease Diagnosis & Farming Assistant 🌱")
    print("=" * 70)
    print()
    inputs = {
        'crop_type': 'Tomato',
        'symptoms': 'Water-soaked spots on lower leaves, white powdery growth on leaf undersides, rapid browning and wilting of foliage, dark lesions on stems',
        'environment': 'High humidity (80%), temperature 18-22°C, recent heavy rains, poor air circulation in greenhouse',
        'growth_stage': 'Flowering stage, plants are about 60 days old',
        'location': 'Maharashtra, India (tropical/subtropical climate)'
    }
    
    print("📋 Crop Information Submitted:")
    print(f"   Crop Type: {inputs['crop_type']}")
    print(f"   Symptoms: {inputs['symptoms'][:80]}...")
    print(f"   Environment: {inputs['environment'][:60]}...")
    print(f"   Growth Stage: {inputs['growth_stage']}")
    print(f"   Location: {inputs['location']}")
    print()
    print("🔍 Analyzing crop condition...")
    print("=" * 70)
    print()

    try:
        result = AgenticAi().crew().kickoff(inputs=inputs)
        
        print()
        print("=" * 70)
        print("✅ Analysis Complete!")
        print("=" * 70)
        print()
        print("📄 A detailed farming report has been saved to 'plantix_farming_report.md'")
        print()
        
        return result
        
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def run_interactive():
    """
    Run the crew with interactive user input.
    """
    
    print("=" * 70)
    print("🌱 PLANTIX - AI-based Crop Disease Diagnosis & Farming Assistant 🌱")
    print("=" * 70)
    print()
    print("Please provide information about your crop issue:")
    print()
    
    crop_type = input("1. What crop are you growing? (e.g., Tomato, Rice, Wheat): ").strip()
    print()
    
    print("2. Describe the symptoms you're observing:")
    print("   (e.g., yellow leaves, spots, wilting, holes in leaves)")
    symptoms = input("   Symptoms: ").strip()
    print()
    
    print("3. Describe the environmental conditions:")
    print("   (e.g., temperature, humidity, recent weather)")
    environment = input("   Environment: ").strip()
    print()
    
    growth_stage = input("4. What growth stage is your crop in? (e.g., seedling, flowering, fruiting): ").strip()
    print()
    
    location = input("5. What is your location/region? (e.g., Punjab, Kerala, California): ").strip()
    print()
    
    inputs = {
        'crop_type': crop_type or 'General crop',
        'symptoms': symptoms or 'Yellowing leaves and stunted growth',
        'environment': environment or 'Normal conditions',
        'growth_stage': growth_stage or 'Mid-season',
        'location': location or 'General region'
    }
    
    print()
    print("🔍 Analyzing your crop condition...")
    print("=" * 70)
    print()
    
    try:
        result = AgenticAi().crew().kickoff(inputs=inputs)
        
        print()
        print("=" * 70)
        print("✅ Analysis Complete!")
        print("=" * 70)
        print()
        print("📄 A detailed farming report has been saved to 'plantix_farming_report.md'")
        print()
        
        return result
        
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "crop_type": "Tomato",
        "symptoms": "Yellow leaves with brown spots",
        "environment": "High humidity, warm temperature",
        "growth_stage": "Vegetative stage",
        "location": "Tropical region"
    }
    try:
        AgenticAi().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AgenticAi().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "crop_type": "Tomato",
        "symptoms": "Wilting and brown spots",
        "environment": "Moderate humidity",
        "growth_stage": "Flowering",
        "location": "Temperate region"
    }

    try:
        AgenticAi().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    # Extract crop info from trigger payload or use defaults
    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "crop_type": trigger_payload.get("crop_type", "General crop"),
        "symptoms": trigger_payload.get("symptoms", "Various symptoms"),
        "environment": trigger_payload.get("environment", "Normal conditions"),
        "growth_stage": trigger_payload.get("growth_stage", "Mid-season"),
        "location": trigger_payload.get("location", "General region")
    }

    try:
        result = AgenticAi().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")


if __name__ == "__main__":
    # If run directly, use interactive mode
    run_interactive()

