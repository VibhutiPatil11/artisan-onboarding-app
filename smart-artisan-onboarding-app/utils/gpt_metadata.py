import openai

def generate_listing(description, category):
    prompt = f"""
    Generate an artisan product listing:
    Category: {category}
    Description: {description}

    Provide:
    - Title
    - Short description (2 lines)
    - 5 keywords
    - Suggested price (INR)
    """

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
