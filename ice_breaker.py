from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_party.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

if __name__ == "__main__":
    print("Hello Langchain")
    
    linkedin_profile_url =linkedin_lookup_agent(name="Eden Marco Udemy") 
    
    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    # Chapter 2
    # linkedin_data = scrape_linkedin_profile(
    #     linkedin_profile_url="https://gist.githubusercontent.com/sonagihu/ab71ee6aee732110289da42be8331334/raw/69f06cfcfa75d8bc9593db06c47ddd3cb9a77f45/gistfile1.txt"
    # )
    
    # Chapter 3

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    
    print(chain.run(information=linkedin_data))
