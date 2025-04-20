import os
import httpx
import asyncio
from dotenv import load_dotenv

load_dotenv()

async def test_openai_request():
    try:
        print("Sending request to OpenAI API")

        AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
        AIPROXY_BASE_URL = os.getenv("AIPROXY_BASE_URL")

        if not AIPROXY_TOKEN or not AIPROXY_BASE_URL:
            raise ValueError("API key or base URL is missing.")

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AIPROXY_TOKEN}"
        }

        request_data = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": "Hello, how are you?"}],
            "max_tokens": 50
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{AIPROXY_BASE_URL}/chat/completions",
                headers=headers,
                json=request_data
            )

        response.raise_for_status()
        response_data = response.json()
        print(f"Response: {response_data}")

        return response_data.get("choices", [{}])[0].get("message", {}).get("content", "No response")

    except Exception as e:
        print(f"Error during OpenAI response fetching: {e}")

# Run the test
asyncio.run(test_openai_request())
