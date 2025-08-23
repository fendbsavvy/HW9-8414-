# Filename: 4_generate_prescriptive_playbook.py
import json
import asyncio
import aiohttp
import os


async def generate_playbook(xai_findings, api_key):
    """
    Creates a simple, step-by-step incident response playbook using the Gemini API.
    """
    prompt = f"""
    As a SOC Manager, your task is to create a simple, step-by-step incident response playbook for a Tier 1 analyst.
    The playbook should be based on the provided alert details and the explanation from our AI model.

    Do not explain the AI model; only provide the prescriptive actions. The playbook must be a numbered list of 3-4 clear, concise steps.

    **Alert Details & AI Explanation:**
    - **Domain:** {xai_findings['domain']}
    - **AI Prediction:** {xai_findings['prediction']}
    - **Model Confidence:** {xai_findings['confidence']:.2f}%
    - **Entropy:** {xai_findings['entropy']:.2f}
    - **Length:** {xai_findings['length']}
    """

    apiUrl = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"
    payload = {"contents": [{"role": "user", "parts": [{"text": prompt}]}]}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(apiUrl, json=payload) as response:
                result = await response.json()

                if response.status != 200:
                    return f"Error: API returned status {response.status}. Response: {json.dumps(result)}"

                if result.get('candidates'):
                    return result['candidates'][0]['content']['parts'][0]['text']
                else:
                    return "Error: Could not generate playbook. Response was: " + json.dumps(result)

    except aiohttp.ClientConnectorError as e:
        return f"An error occurred: Could not connect to the API endpoint. {e}"
    except Exception as e:
        return f"An error occurred: {e}"


async def main(findings):
    api_key = os.environ.get("GOOGLE_API_KEY")

    if not api_key:
        print("🚨 Error: GOOGLE_API_KEY environment variable not set.")
        return

    print("Generating playbook based on prediction...")
    playbook = await generate_playbook(findings, api_key)
    print("\n--- AI-Generated Playbook ---")
    print(playbook)


if __name__ == "__main__":

    findings_example = {
        "domain": "kq3v9z7j1x5f8g2h.info",
        "prediction": "dga",
        "confidence": 96.81,
        "entropy": 4.3,
        "length": 21
    }
    asyncio.run(main(findings_example))
