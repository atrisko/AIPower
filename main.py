import os
import argparse
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompt import system_prompt
from call_function import available_functions, call_function




def main():
   

    parser = argparse.ArgumentParser(description='User prompt for Gemini API')
    parser.add_argument('prompt', type=str, help='The prompt to send to the Gemini')
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    print("Hello from AIpower!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set.")
    
    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]

    if args.verbose:
        print(f"User prompt: {args.prompt}")


    for _ in range(20):  # Limit to 20 iterations to prevent infinite loops
        final = generate_content(client, messages, args.verbose)
        if final:
            print("Final response:")
            print(final)
            return
        
    print("Reached maximum iterations without a final response.")
    sys.exit(1)
                     

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[available_functions],
            temperature=0),
        )
    
    if not response.usage_metadata:
        raise RuntimeError("Response is missing usage metadata.")
    
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")

        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    


    if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

    if response.function_calls:
        function_results = []
        for function_call in response.function_calls:
            try:
                function_call_result = call_function(function_call, verbose)
            except Exception as e:
                print(f"Error: {e}")
            if (
                not function_call_result.parts
                or not function_call_result.parts[0].function_response
                or not function_call_result.parts[0].function_response.response
            ):
                raise RuntimeError(f"Empty function response for {function_call.name}")
            function_results.append(function_call_result.parts[0])
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        messages.append(types.Content(role="user", parts=function_results))
       
        
    else:
        #print("Response from Gemini:")
        return response.text

    


if __name__ == "__main__":
    main()
