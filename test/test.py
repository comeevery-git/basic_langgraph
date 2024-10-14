import unittest
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from rapidfuzz import fuzz


class TestChat(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.input_data = "주말은 언제나 순식간에 지나가네."
        self.prompt = ChatPromptTemplate.from_template("""
너는 한국의 번역가야. input 내용을 {language}로 번역해줘.
[INPUT]
{input}
        """)
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.")
        self.llm = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=self.api_key)
        self.output_parser = StrOutputParser()
        self.chain = self.prompt | self.llm | self.output_parser

    def test_translation(self):
        result = self.chain.invoke(
            {
                "input": self.input_data,
                "language": "en"
            }, verbose=True
        )
        expected_output = "The weekend always passes in the blink of an eye."

        # rapidfuzz: 유사성 조회
        similarity_ratio = fuzz.ratio(result, expected_output)
        self.assertGreater(similarity_ratio, 90)  # 90% 이상 통과


if __name__ == "__main__":
    unittest.main()
