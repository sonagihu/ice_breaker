from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_party.linkedin import scrape_linkedin_profile
from third_party.twitter import scrape_user_tweets
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent

from urllib.parse import urlparse

name="Elon Musk"
def ice_break(name: str) -> str:
    
    linkedin_profile_url =linkedin_lookup_agent(name="Eden Marco Udemy") 
    print("linkedin_url found: {0}".format(linkedin_profile_url))
    linkedin_profile_url ='https://gist.githubusercontent.com/sonagihu/ab71ee6aee732110289da42be8331334/raw/69f06cfcfa75d8bc9593db06c47ddd3cb9a77f45/gistfile1.txt' 
    print("linkedin_url redirect : {0}".format(linkedin_profile_url))
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)    

    twitter_username = urlparse(twitter_lookup_agent(name=name)).path[1:]
    tweets = scrape_user_tweets(username=twitter_username, num_tweets=100)
        
    summary_template = """
        given the information {linkedin_information} and
        {twitter_information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], 
        template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    
    result = chain.run(linkedin_information=linkedin_data, twitter_information=tweets)
    print(result)
    
    return result
    
if __name__ == "__main__":
    print("Hello Langchain")
    result = ice_break(name="Harrison Chase")
