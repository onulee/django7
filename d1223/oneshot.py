import openai
from environ import Env

env = Env()
env.read_env()  # .env 파일을 환경변수로서 로딩


def print_prices(input_tokens: int, output_tokens: int) -> None:
    input_price = (input_tokens * 0.150 / 1_000_000) * 1_500
    output_price = (output_tokens * 0.600 / 1_000_000) * 1_500
    print("input: tokens {}, krw {:.4f}".format(input_tokens, input_price))
    print("output: tokens {}, krw {:4f}".format(output_tokens, output_price))


def make_ai_message(question: str) -> str:
    client = openai.Client()  # OPENAI_API_KEY 환경변수를 디폴트로 참조

    res = client.chat.completions.create(
        messages=[
            { "role": "user", "content": question },
        ],
        model="gpt-4o-mini",
        temperature=0,
    )
    print_prices(res.usage.prompt_tokens, res.usage.completion_tokens)
    return res.choices[0].message.content


def main():
    question = "넌 AI Assistant. 모르는 건 모른다고 대답.\n\n빽다방 카페인이 높은 음료와 가격은?"
    ai_message = make_ai_message(question)
    print(ai_message)


if __name__ == "__main__":
    main()