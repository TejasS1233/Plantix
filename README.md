# 🌱 Plantix - AI Farming Assistant

Multi-agent AI system for crop disease diagnosis and farming guidance, built with CrewAI.

## 🤖 AI Agents

**4 specialized agents** collaborate to provide comprehensive farming solutions:

### 1. Disease Diagnostician 🔬
Expert plant pathologist that analyzes symptoms and environmental conditions to identify diseases with high accuracy using the Crop Disease Knowledge Database.

### 2. Treatment Specialist 💊
Creates immediate action plans with organic and chemical treatment options, considers budget constraints, and provides step-by-step implementation guidance.

### 3. Prevention Advisor 🛡️
Develops long-term prevention strategies including crop rotation, soil management, resistant varieties, and seasonal farming calendars tailored to your region.

### 4. Farming Consultant 🌾
Provides complete cultivation guides covering optimal growing conditions, soil prep, irrigation, fertilization schedules, harvest timing, and market strategies.

## 🛠️ Tools

- **Crop Disease Knowledge Database** - Disease info, symptoms, treatments
- **Soil Analysis** - Soil type recommendations and amendments  
- **Weather & Climate** - Regional climate data for risk assessment

## 📋 Features

- ✅ Multi-agent collaboration for comprehensive analysis
- ✅ Context-aware recommendations based on location and climate
- ✅ Both organic and chemical treatment options
- ✅ Preventive measures and long-term strategies
- ✅ Interactive and batch processing modes
- ✅ Detailed reports saved as markdown files

## 🚀 Installation

1. **Install dependencies:**

```bash
pip install -e .
```

2. **Set up environment variables:**
   Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_key_here
# Or use other LLM providers supported by CrewAI
```

## 💻 Usage

### Method 1: Interactive Mode (Recommended for farmers)

Run with user prompts to input crop information:

```bash
python -m agentic_ai.main
```

Or use the script command:

```bash
run_crew
```

You'll be prompted to enter:

- Crop type (e.g., Tomato, Rice, Wheat)
- Symptoms observed
- Environmental conditions
- Growth stage
- Location/region

### Method 2: Pre-configured Run

Use the default `run()` function with example data:

```bash
agentic_ai
```

### Method 3: Custom Script

Create your own Python script:

```python
from agentic_ai.crew import AgenticAi

inputs = {
    'crop_type': 'Tomato',
    'symptoms': 'Yellow leaves with brown spots, wilting',
    'environment': 'High humidity, warm temperature',
    'growth_stage': 'Flowering stage',
    'location': 'Maharashtra, India'
}

result = AgenticAi().crew().kickoff(inputs=inputs)
```

## 📊 Example Input

```python
inputs = {
    'crop_type': 'Tomato',
    'symptoms': 'Water-soaked spots on leaves, white fungal growth on undersides, rapid browning',
    'environment': 'High humidity (80%), temperature 18-22°C, recent heavy rains',
    'growth_stage': 'Flowering stage, 60 days old',
    'location': 'Maharashtra, India'
}
```

## 📄 Output

The system generates a comprehensive report (`plantix_farming_report.md`) containing:

1. **Disease Diagnosis**

   - Disease identification (common and scientific names)
   - Confidence level
   - Symptom analysis
   - Severity assessment
   - Yield impact prediction

2. **Treatment Recommendations**

   - Immediate action plan
   - Organic treatment options
   - Chemical treatment options (if necessary)
   - Application methods and dosages
   - Safety precautions
   - Cost estimates

3. **Prevention Strategies**

   - Long-term preventive measures
   - Crop rotation recommendations
   - Soil management tips
   - Disease-resistant varieties
   - Monitoring guidelines

4. **General Farming Advice**
   - Optimal growing conditions
   - Seasonal calendar
   - Soil and nutrient management
   - Irrigation schedule
   - Harvest and post-harvest handling

## 🔧 Advanced Usage

### Training the Model

```bash
train <n_iterations> <filename>
```

### Testing

```bash
test <n_iterations> <eval_llm>
```

### Replay Previous Run

```bash
replay <task_id>
```

### Trigger-based Execution

```bash
run_with_trigger '{"crop_type": "Rice", "symptoms": "Brown spots", ...}'
```

## 📁 Project Structure

```
agentic_ai/
├── src/agentic_ai/
│   ├── config/
│   │   ├── agents.yaml          # Agent configurations
│   │   └── tasks.yaml           # Task definitions
│   ├── tools/
│   │   ├── custom_tool.py       # Custom tools implementation
│   │   └── __init__.py
│   ├── crew.py                  # Crew orchestration
│   ├── main.py                  # Entry points
│   └── __init__.py
├── knowledge/
│   └── user_preference.txt      # User preferences
├── tests/
├── pyproject.toml
└── README.md
```

## 🌾 Supported Crops

The system has knowledge of major crops including:

- Vegetables: Tomato, Potato, Cucumber, Pepper, Eggplant
- Grains: Rice, Wheat, Corn
- Commercial crops: Cotton, Sugarcane
- And many more...

## 🐛 Common Diseases Covered

- Late Blight
- Powdery Mildew
- Bacterial Wilt
- Leaf Spots
- Root Rot
- Mosaic Viruses
- And various pest infestations

## 🤝 Contributing

This is a CrewAI-based project. To contribute:

1. Add new tools in `tools/custom_tool.py`
2. Extend agent capabilities in `config/agents.yaml`
3. Add new tasks in `config/tasks.yaml`
4. Update crew orchestration in `crew.py`

## 📝 License

This project is built using CrewAI framework.

## Author

Created by **TejasS1233**

## 🙏 Acknowledgments

- Built with [CrewAI](https://www.crewai.com/)
- Powered by Large Language Models
- Designed to help farmers worldwide
