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
    
    # linkedin_profile_url =linkedin_lookup_agent(name="Eden Marco Udemy") 
        # print("linkedin_url found: {0}".format(linkedin_profile_url))
    # linkedin_profile_url ='https://gist.githubusercontent.com/sonagihu/ab71ee6aee732110289da42be8331334/raw/69f06cfcfa75d8bc9593db06c47ddd3cb9a77f45/gistfile1.txt' 
    # print("linkedin_url redirect : {0}".format(linkedin_profile_url))
    # linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)    

    # 강의에서는 agent가 찾은 url에서 name을 가져오기 위해 시도하다가
    # 알아서 찾는다고 하는데, 테스트 시 계속 반복하다가 url에서 name을 추출하는 tool을 찾을 수 없다는 에러가 남
    # 그래서 uri를 가져오게 수정하고 (twitter_lookup_agent에서 수정) 자름
    # 가져온 uri를  짜름
    
    twitter_username = urlparse(twitter_lookup_agent(name=name)).path[1:]
    
    
    print(twitter_username)
    
    tweets = scrape_user_tweets(username=twitter_username, num_tweets=100)

    print(tweets)
        

