from llm_api import gpt, prompts
from company_details import get_company_details



company_url = "https://www.myjar.app/"

company_details_dump = get_company_details.get_company_info(company_url)


gpt.set_system_prompt(prompts.COMPANY_DETAILS_PROMPT)
company_info = gpt.fetch_openai_response(company_details_dump)

gpt.set_system_prompt(prompts.MAIL_GEN_PROMPT)


# email_gen_prompt = {
#     {"role_applying": "Software Engineer",
#     "position": "Full Time",
#     "projects": "fullstack twitter clone"},
#     "company_inf": company_info
# }
email_gen_prompt = {
    "role_applying": "Software Engineer",
    "position": "Full Time",
    "projects": "fullstack twitter clone",
    "company_inf": company_info
    }





generated_email = gpt.fetch_openai_response(email_gen_prompt)






print("generated_email", generated_email)
