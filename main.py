from langchain_community.document_loaders import PyPDFLoader
import os
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from serpapi import Client
import csv


class SkillsSchema(BaseModel):
    skills : list[str] = Field(description="Skills of the candidate.")

def get_pdf_file_content():
    file_path = "Untitled document.pdf"
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs[0].page_content

def get_skills_from_content(description):
    llm = init_chat_model("gpt-4.1-mini", model_provider='openai')
    structured_output = llm.with_structured_output(SkillsSchema)
    output = structured_output.invoke("Fetch the skills required to hire the candidate from the below job desccription."
                             "Make sure to include relevant skills only. Do not include unnecessary skills."
                                      f"{description}")
    return output.skills


def find_candidates(jd_skills):
    query = f"site:linkedin.com/in {' '.join(jd_skills)}"
    client = Client(api_key="52206166ba948060a811f8dc7813015a6d781c13b2f6d703698bc6d578c715d0")
    search = client.search({
        "q": query
    })
    results = search.data
    profiles = []

    for result in results.get("organic_results", []):
        profiles.append({
            "name": result.get("title"),
            "link": result.get("link"),
            "description": result.get("snippet")
        })
    return profiles


class CandidateSchema(BaseModel):
    name: str = Field(description="Name of the candidate")
    description: str = Field(description=" Description of the candidate")
    link: str = Field(description="Linkedin url of the candidate")
    skills: list[str] = Field(description="List of skills of the candidate")
    score: float = Field(description="Match score out of 100 based on candidate skills and require skills")


class CandidatesSchema(BaseModel):
    candidates: list[CandidateSchema]

def get_matching_score(jd_skills,found_candidates):

    llm = init_chat_model("gpt-4.1-mini", model_provider='openai')
    structured_output = llm.with_structured_output(CandidatesSchema)
    output = structured_output.invoke(f"""you need to calculate the skills score based on the required skills and the skills that candidate have.
                                the candidates details are as below in json format: {jd_skills}. the list of the candidates are as below.
                                {found_candidates}""")

    return output.candidates

def store_in_csv(found_candidates):
    file_name = "output.csv"

    file_exists = os.path.exists(file_name)
    found_candidates =  [found_candidate.model_dump() for found_candidate in found_candidates]
    with open(file_name, 'a', newline='',  encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=found_candidates[0].keys())
        if not file_exists or os.path.getsize(file_name) == 0:
            writer.writeheader()
        writer.writerows(found_candidates)


if __name__ == "__main__":
    job_description = get_pdf_file_content()
    skills  = get_skills_from_content(job_description)
    candidates = find_candidates(skills)

    candidates = get_matching_score(skills, candidates)
    store_in_csv(candidates)