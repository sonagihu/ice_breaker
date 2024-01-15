from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

information="""
Jordan Speith """

if __name__ == "__main__":
    print("Hello Langchain")
    
    # 먼저 summary_template(prompt template을 만들기 위한 사용자 정의 template)을 만들고
    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    # 만들어놓은 template을 이용해 prompt template을 생성함
    summary_prompt_template = PromptTemplate(input_variables=["information"], 
                                             template=summary_template)
    
    # 사용할 llm을 지정, gpt-3.5-turbo로 지정함 (API에 대한 결제가 선행되어야 동작 할 것임)
    # temperature가 0이면 창의적이지 않은 것
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # 작업을 실행할 chain 지정, 일단 어떤 llm에 어떤 prompt template으로 실행할 지 간단하게 정의
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    # 실행된 결과 print
    print(chain.run(information=information))