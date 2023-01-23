import dotenv
import os
import openai

def get_token(file: str = ".env") -> str:
    dotenv.load_dotenv(file)
    return os.getenv("TOKEN")

def get_prompt(from_file: bool = False, file: str = "example-prompt.txt") -> str:
    if from_file:
        with open(file, "r") as f:
            return f.read()
    else:
        return input("Enter your prompt: ")
    
def generate_email(prompt: str, token: str) -> str:
    openai.api_key = token
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write a formal email based on the below prompt \n\n{prompt}",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response: str = response["choices"][0]["text"]

    return response

def main() -> None:
    token: str = get_token()
    prompt: str = get_prompt()

    response: str = generate_email(prompt, token)

    print(response)

if __name__ == "__main__":
    main()