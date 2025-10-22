"""
Plantix - Custom Tools for AI Farming Assistant
Created by TejasS1233
"""

from crewai.tools import BaseTool
from typing import Type, Optional
from pydantic import BaseModel, Field
import json


class CropDiseaseKnowledgeInput(BaseModel):
    """Input schema for CropDiseaseKnowledgeTool."""
    disease_name: str = Field(..., description="Name of the crop disease or pest to lookup")
    crop_type: Optional[str] = Field(None, description="Type of crop (optional for more specific results)")


class CropDiseaseKnowledgeTool(BaseTool):
    name: str = "Crop Disease Knowledge Database"
    description: str = (
        "Access a comprehensive database of crop diseases, pests, and their characteristics. "
        "Use this tool to get detailed information about specific diseases including symptoms, "
        "causes, treatment options, and prevention methods. Provide the disease name and optionally the crop type."
    )
    args_schema: Type[BaseModel] = CropDiseaseKnowledgeInput

    def _run(self, disease_name: str, crop_type: Optional[str] = None) -> str:
        disease_db = {
            "late blight": {
                "scientific_name": "Phytophthora infestans",
                "crops_affected": ["tomato", "potato"],
                "symptoms": "Water-soaked spots on leaves, white fungal growth on undersides, rapid browning and death of foliage",
                "causes": "Fungal pathogen, thrives in cool humid conditions, spreads via wind and water",
                "treatment": "Copper-based fungicides, Mancozeb, remove infected plants",
                "prevention": "Use resistant varieties, improve air circulation, avoid overhead irrigation"
            },
            "powdery mildew": {
                "scientific_name": "Various Erysiphales species",
                "crops_affected": ["wheat", "cucumber", "grape", "tomato", "many vegetables"],
                "symptoms": "White powdery spots on leaves and stems, yellowing leaves, stunted growth",
                "causes": "Fungal disease, favored by warm days and cool nights, high humidity",
                "treatment": "Sulfur-based fungicides, neem oil, baking soda solution",
                "prevention": "Proper spacing, remove infected leaves, choose resistant varieties"
            },
            "bacterial wilt": {
                "scientific_name": "Ralstonia solanacearum",
                "crops_affected": ["tomato", "potato", "eggplant", "pepper"],
                "symptoms": "Sudden wilting of plants, vascular browning, bacterial ooze from cut stems",
                "causes": "Soil-borne bacteria, spreads through water and contaminated tools",
                "treatment": "Remove and destroy infected plants, soil solarization, crop rotation",
                "prevention": "Use disease-free seeds, improve drainage, practice crop rotation"
            },
            "aphids": {
                "scientific_name": "Aphidoidea",
                "crops_affected": ["most vegetables", "fruits", "ornamentals"],
                "symptoms": "Curled leaves, sticky honeydew, sooty mold, stunted growth, yellowing",
                "causes": "Small sap-sucking insects, reproduce rapidly in warm weather",
                "treatment": "Insecticidal soap, neem oil, introduce ladybugs, strong water spray",
                "prevention": "Encourage beneficial insects, use reflective mulches, remove weeds"
            },
            "leaf spot": {
                "scientific_name": "Various fungi and bacteria",
                "crops_affected": ["tomato", "pepper", "cucumber", "beans"],
                "symptoms": "Circular brown or black spots on leaves, yellowing around spots, leaf drop",
                "causes": "Fungal or bacterial pathogens, spread by water splash and wind",
                "treatment": "Remove infected leaves, apply copper fungicide, improve air circulation",
                "prevention": "Avoid overhead watering, space plants properly, practice crop rotation"
            },
            "root rot": {
                "scientific_name": "Various Phytophthora, Pythium, Fusarium species",
                "crops_affected": ["most crops"],
                "symptoms": "Yellowing leaves, wilting, brown mushy roots, plant death",
                "causes": "Soil-borne fungi, overwatering, poor drainage",
                "treatment": "Improve drainage, reduce watering, apply fungicides, remove affected plants",
                "prevention": "Ensure good drainage, avoid overwatering, use raised beds"
            },
            "mosaic virus": {
                "scientific_name": "Various viruses (TMV, CMV, etc.)",
                "crops_affected": ["tomato", "pepper", "cucumber", "tobacco"],
                "symptoms": "Mottled yellow-green pattern on leaves, distorted growth, reduced yield",
                "causes": "Viral infection spread by aphids, thrips, contaminated tools",
                "treatment": "No cure - remove infected plants, control insect vectors",
                "prevention": "Use virus-free seeds, control aphids, sanitize tools, use resistant varieties"
            }
        }
        
        disease_lower = disease_name.lower()
        
        # Search for disease
        result = None
        for key, value in disease_db.items():
            if disease_lower in key or key in disease_lower:
                result = value
                result["disease_name"] = key.title()
                break
        
        if result:
            output = f"Disease Information: {result.get('disease_name', disease_name)}\n"
            output += f"Scientific Name: {result['scientific_name']}\n"
            output += f"Crops Affected: {', '.join(result['crops_affected'])}\n"
            output += f"Symptoms: {result['symptoms']}\n"
            output += f"Causes: {result['causes']}\n"
            output += f"Treatment: {result['treatment']}\n"
            output += f"Prevention: {result['prevention']}\n"
            return output
        else:
            return f"Disease '{disease_name}' not found in database. Please check the spelling or provide more details."


class WeatherConditionsInput(BaseModel):
    """Input schema for WeatherConditionsTool."""
    location: str = Field(..., description="Location or region to get weather information for")


class WeatherConditionsTool(BaseTool):
    name: str = "Weather and Climate Information"
    description: str = (
        "Get current weather conditions and climate information for a specific location. "
        "This is useful for understanding environmental factors affecting crop diseases and growth. "
        "Provide the location/region name."
    )
    args_schema: Type[BaseModel] = WeatherConditionsInput

    def _run(self, location: str) -> str:
        # Simulated weather data - in production, this would call a real weather API
        weather_patterns = {
            "tropical": {
                "temperature": "25-35°C",
                "humidity": "High (70-90%)",
                "rainfall": "Heavy seasonal rains",
                "disease_risk": "High risk for fungal diseases, bacterial infections due to humidity"
            },
            "temperate": {
                "temperature": "10-25°C",
                "humidity": "Moderate (50-70%)",
                "rainfall": "Moderate, well-distributed",
                "disease_risk": "Moderate risk, watch for cool-weather fungal diseases"
            },
            "arid": {
                "temperature": "20-40°C",
                "humidity": "Low (20-40%)",
                "rainfall": "Minimal",
                "disease_risk": "Lower disease pressure, but watch for stress-related issues and spider mites"
            },
            "subtropical": {
                "temperature": "20-30°C",
                "humidity": "Moderate to High (60-80%)",
                "rainfall": "Seasonal variation",
                "disease_risk": "Moderate to high risk for various fungal and bacterial diseases"
            }
        }
        
        output = f"Weather Information for {location}:\n\n"
        output += "Based on typical climate patterns for this region:\n"
        
        # Provide general climate info (in production, use real weather API)
        climate_type = "temperate"  # Default
        if any(word in location.lower() for word in ["india", "africa", "south", "tropical", "florida", "brazil"]):
            climate_type = "tropical" if "tropical" in location.lower() or "rain" in location.lower() else "subtropical"
        elif any(word in location.lower() for word in ["desert", "dry", "arid", "middle east"]):
            climate_type = "arid"
        
        pattern = weather_patterns[climate_type]
        output += f"Climate Type: {climate_type.title()}\n"
        output += f"Temperature Range: {pattern['temperature']}\n"
        output += f"Humidity: {pattern['humidity']}\n"
        output += f"Rainfall: {pattern['rainfall']}\n"
        output += f"Disease Risk Assessment: {pattern['disease_risk']}\n"
        
        return output


class SoilAnalysisInput(BaseModel):
    """Input schema for SoilAnalysisTool."""
    soil_type: str = Field(..., description="Type of soil (e.g., clay, sandy, loamy, etc.)")
    crop_type: str = Field(..., description="Type of crop to be grown")


class SoilAnalysisTool(BaseTool):
    name: str = "Soil Analysis and Recommendations"
    description: str = (
        "Get soil analysis information and recommendations for specific soil types and crops. "
        "Provides guidance on soil amendments, pH requirements, and nutrient management. "
        "Provide the soil type and crop type."
    )
    args_schema: Type[BaseModel] = SoilAnalysisInput

    def _run(self, soil_type: str, crop_type: str) -> str:
        soil_info = {
            "clay": {
                "characteristics": "Heavy, retains water, poor drainage, slow to warm",
                "advantages": "Nutrient-rich, good water retention",
                "challenges": "Compaction, poor aeration, waterlogging risk",
                "amendments": "Add organic matter, sand, gypsum for structure improvement",
                "suitable_crops": "Rice, wheat, cabbage, broccoli"
            },
            "sandy": {
                "characteristics": "Light, fast-draining, quick to warm",
                "advantages": "Good aeration, easy to work, warms quickly",
                "challenges": "Poor water retention, nutrient leaching",
                "amendments": "Add compost, peat moss, organic matter for water retention",
                "suitable_crops": "Carrots, potatoes, lettuce, radishes"
            },
            "loamy": {
                "characteristics": "Balanced mixture of sand, silt, and clay",
                "advantages": "Ideal soil, good drainage and water retention, fertile",
                "challenges": "May need nutrient replenishment",
                "amendments": "Regular compost addition, balanced fertilization",
                "suitable_crops": "Most vegetables and crops thrive"
            },
            "silt": {
                "characteristics": "Smooth, retains moisture, fertile",
                "advantages": "Good water retention, fertile, easy to work when dry",
                "challenges": "Compaction when wet, erosion prone",
                "amendments": "Add organic matter, avoid working when wet",
                "suitable_crops": "Vegetables, corn, wheat, soybeans"
            }
        }
        
        soil_lower = soil_type.lower()
        soil_data = None
        
        for key in soil_info:
            if key in soil_lower:
                soil_data = soil_info[key]
                break
        
        if not soil_data:
            soil_data = soil_info["loamy"]  # Default
        
        output = f"Soil Analysis for {soil_type.title()} Soil:\n\n"
        output += f"Characteristics: {soil_data['characteristics']}\n"
        output += f"Advantages: {soil_data['advantages']}\n"
        output += f"Challenges: {soil_data['challenges']}\n"
        output += f"Recommended Amendments: {soil_data['amendments']}\n"
        output += f"Naturally Suitable Crops: {soil_data['suitable_crops']}\n\n"
        
        output += f"Recommendations for growing {crop_type}:\n"
        output += f"1. Test soil pH - most crops prefer 6.0-7.0 range\n"
        output += f"2. Add organic matter (compost) 2-3 weeks before planting\n"
        output += f"3. Ensure proper drainage to prevent root diseases\n"
        output += f"4. Apply balanced NPK fertilizer based on soil test results\n"
        output += f"5. Consider raised beds if drainage is a concern\n"
        
        return output


class PestIdentificationInput(BaseModel):
    """Input schema for PestIdentificationTool."""
    pest_description: str = Field(..., description="Description of the pest, including size, color, behavior")
    crop_affected: str = Field(..., description="The crop that is affected by this pest")


class PestIdentificationTool(BaseTool):
    name: str = "Pest Identification and Control"
    description: str = (
        "Identify pests based on description and get control recommendations. "
        "Useful for diagnosing insect pests, mites, and other crop predators. "
        "Provide a description of the pest and the affected crop."
    )
    args_schema: Type[BaseModel] = PestIdentificationInput

    def _run(self, pest_description: str, crop_affected: str) -> str:
        pest_db = {
            "aphid": {
                "description": "Small (1-3mm), soft-bodied insects, green/black/brown, cluster on stems and leaves",
                "damage": "Suck plant sap, cause curling, yellowing, transmit viruses, produce honeydew",
                "control_organic": "Spray with water, neem oil, insecticidal soap, introduce ladybugs/lacewings",
                "control_chemical": "Imidacloprid, Acetamiprid (use only if severe infestation)",
                "prevention": "Encourage beneficial insects, remove weeds, use reflective mulch"
            },
            "whitefly": {
                "description": "Tiny white flying insects (1-2mm), found on undersides of leaves",
                "damage": "Suck sap, secrete honeydew, cause yellowing, transmit viruses",
                "control_organic": "Yellow sticky traps, neem oil, insecticidal soap, introduce parasitic wasps",
                "control_chemical": "Spiromesifen, Buprofezin",
                "prevention": "Remove infected leaves, use fine mesh screens, crop rotation"
            },
            "caterpillar": {
                "description": "Larval stage of moths/butterflies, worm-like, various colors, actively feeding",
                "damage": "Chew holes in leaves, fruits, stems; can defoliate plants",
                "control_organic": "Hand-pick, Bacillus thuringiensis (Bt), neem oil, encourage birds",
                "control_chemical": "Chlorantraniliprole, Spinosad",
                "prevention": "Regular inspection, row covers, encourage natural predators"
            },
            "spider mite": {
                "description": "Very tiny (0.5mm), reddish/yellow, fine webbing on leaves",
                "damage": "Suck cell contents, cause stippling/bronzing of leaves",
                "control_organic": "Spray with water, neem oil, predatory mites, insecticidal soap",
                "control_chemical": "Abamectin, Spiromesifen",
                "prevention": "Maintain humidity, avoid drought stress, remove dusty conditions"
            },
            "thrips": {
                "description": "Very small (1mm), slender, yellow/brown/black, quick-moving",
                "damage": "Scrape and suck plant cells, cause silvery streaks, distorted growth",
                "control_organic": "Blue sticky traps, neem oil, spinosad, introduce predatory mites",
                "control_chemical": "Imidacloprid, Spinosad",
                "prevention": "Remove weeds, use reflective mulches, maintain plant health"
            }
        }
        
        desc_lower = pest_description.lower()
        identified_pest = None
        
        for pest_name, pest_info in pest_db.items():
            if pest_name in desc_lower or any(word in desc_lower for word in pest_name.split()):
                identified_pest = (pest_name, pest_info)
                break
        
        if identified_pest:
            name, info = identified_pest
            output = f"Pest Identified: {name.title()}\n\n"
            output += f"Description: {info['description']}\n"
            output += f"Damage Caused: {info['damage']}\n\n"
            output += f"Organic/Natural Control Methods:\n{info['control_organic']}\n\n"
            output += f"Chemical Control (if necessary):\n{info['control_chemical']}\n\n"
            output += f"Prevention Strategies:\n{info['prevention']}\n"
            return output
        else:
            return (f"Pest matching '{pest_description}' not definitively identified. "
                   f"Common pests affecting {crop_affected} include aphids, whiteflies, caterpillars, "
                   f"and mites. Please provide more specific details about size, color, and behavior.")

