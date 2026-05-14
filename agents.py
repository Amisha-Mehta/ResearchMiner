from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
import os

from dotenv import load_dotenv
load_dotenv()

#model setup
llm = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-1.5-flash"),
    temperature=0,
)

#1st agent
def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )

#2nd agent
def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )

#writer chain

writer_prompt=ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Produce high-quality, factual, well-structured reports in clean Markdown."),
    ("human","""Write a detailed research report on the topic below.
Topic: {topic}
Research Gathered:
{research}
Follow this exact structure and headings:
## Executive Summary
- 4-6 bullets with the most important takeaways
- Include a one-line bottom-line statement at the end

## Introduction
- Brief context, why the topic matters, and scope of this report

## Key Findings
### Finding 1
- Evidence:
- Why it matters:
### Finding 2
- Evidence:
- Why it matters:
### Finding 3
- Evidence:
- Why it matters:
- Add Finding 4 if enough evidence is available

## Risks and Limitations
- List uncertainties, data gaps, and possible bias in sources

## Conclusion
- Final synthesis in 5-8 lines with practical implications

## Sources
- List every usable URL you relied on (one per bullet)
- Mark low-confidence or indirect sources with "(use with caution)"

Rules:
- Keep claims factual and grounded in the given research.
- If information is missing or uncertain, explicitly say "Insufficient evidence in provided research".
- Do not invent sources or statistics.
- Keep writing professional, specific, and scannable.
- Prefer short paragraphs and bullets over long blocks of text."""),
])

writer_chain=writer_prompt | llm | StrOutputParser()

#critic_chain

critic_prompt=ChatPromptTemplate.from_messages([
     ("system", "You are a senior research evaluator. Be strict, specific, concise, and actionable."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format and keep it concrete:

## Overall Score
Score: X/10

## Rubric Breakdown
- Accuracy: X/10
- Completeness: X/10
- Clarity & Structure: X/10
- Evidence Quality: X/10
- Source Reliability: X/10

## Strengths
- ...
- ...

## Areas to Improve
- ...
- ...

## Missing Elements
- ...
- ...

## Priority Fixes (highest impact first)
1. [High] ...
2. [Medium] ...
3. [Medium] ...
4. [Low] ...

## Rewrite Suggestions
- Original issue: ...
- Better version: ...
- Original issue: ...
- Better version: ...

## One-Line Verdict
...

Rules:
- Do not use generic feedback. Reference specific weak patterns from the report.
- If sources are weak or absent, state that clearly and lower relevant rubric scores.
- Keep tone professional and direct."""),

])

critic_chain=critic_prompt | llm | StrOutputParser()
