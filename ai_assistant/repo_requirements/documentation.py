```python
import os
import pydoc

def generate_documentation():
    """
    This function generates documentation for all the modules in the AI assistant application.
    """
    modules = [
        "social_media", "learning_development", "network_data_management", "project_management", "sales_crm",
        "document_management", "conflict_resolution", "google_contacts", "email", "twilio", "eleven_labs",
        "self_evolution_api", "discord", "news_aggregation", "automated_calls", "subscription_management",
        "collaboration_tools", "analytics_reporting", "invoicing_payments", "hr", "inventory", "customer_support",
        "prompt_engineering", "dynamic_persona", "voice_selection", "entrepreneurial_skills", "negotiation_skills",
        "personal_assistant_tasks", "entertainment", "fitness_tracking", "recipe_suggestions", "financial_management",
        "shopping", "personal_growth", "mood_tracking_support", "personal_safety_alerts", "gift_management",
        "pet_care", "plant_care", "habit_building", "publicist_capabilities", "family_coordination", "ride_ordering",
        "food_delivery", "python_compatibility", "documentation", "onboarding", "code_modularity_quality"
    ]

    for module in modules:
        doc = pydoc.render_doc(module, "Help on %s")
        with open(f"documentation/{module}.txt", "w") as f:
            f.write(doc)

    print("Documentation generated successfully.")

if __name__ == "__main__":
    generate_documentation()
```