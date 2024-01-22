from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_party.linkedin import scrape_linkedin_profile
from third_party.twitter import scrape_user_tweets
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent

from urllib.parse import urlparse

name="Elon Musk"
if __name__ == "__main__":
    print("Hello Langchain")
    
    linkedin_profile_url =linkedin_lookup_agent(name="Eden Marco Udemy") 
    print("linkedin_url found: {0}".format(linkedin_profile_url))
    linkedin_profile_url ='https://gist.githubusercontent.com/sonagihu/ab71ee6aee732110289da42be8331334/raw/69f06cfcfa75d8bc9593db06c47ddd3cb9a77f45/gistfile1.txt' 
    print("linkedin_url redirect : {0}".format(linkedin_profile_url))
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)    

    # 강의에서는 agent가 찾은 url에서 name을 가져오기 위해 시도하다가
    # 알아서 찾는다고 하는데
    # 나는 계속 반복하다가 에러가 남
    # 그래서 uri를 가져오게 수정하고
    # 가져온 uri를 내가 짜름
    twitter_username = urlparse(twitter_lookup_agent(name=name)).path[1:]
     
    # 여기도 gist에서   
    tweets = scrape_user_tweets(username=twitter_username, num_tweets=100)
        
    summary_template = """
        given the information {linkedin_information} and
        {twitter_information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    
    print(chain.run(linkedin_information=linkedin_data, twitter_information=tweets))
