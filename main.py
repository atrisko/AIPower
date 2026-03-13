import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompt import system_prompt
from call_function import available_functions




def main():
    print("Hello from AIpower!")
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set.")
    
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description='User prompt for Gemini API')
    parser.add_argument('prompt', type=str, nargs='+',help='The prompt to send to the Gemini')
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=" ".join(args.prompt))])]

    if args.verbose:
        print(f"User prompt: {" ".join(args.prompt)}\n")

    generate_content(client, messages, args.verbose)
    
def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[available_functions],),
        )
    
    if not response.usage_metadata:
        raise RuntimeError("Response is missing usage metadata.")
    
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")

        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    

    print("Response from Gemini:")
    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    if not response.function_calls:
        print(response.text)

    


if __name__ == "__main__":
    main()
