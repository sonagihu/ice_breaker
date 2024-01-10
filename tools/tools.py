from langchain_community.utilities import SerpAPIWrapper


def get_profile_url(text: str) -> str:
   """Searches for Linkedin Profile Page""" 
   
   # Langchain serpAPI wrapper
   # 1. convenient use of serapi key
   # 2. ouput data를 원하는 출력 결과물에 맞게 정리(heuristic)
   search = SerpAPIWrapper()
   res = search.run(f"{text}")
   print(f"========================={res}=================")

   return res
   