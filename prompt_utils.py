import re
from langchain.prompts import PromptTemplate

GENERATE_CONFIRMATIONAL_QUESTION = ("""
            You are a teacher who is preparing an exam paper for their students. 
            Using the following text as context generate a confirmation Question [yes or no].
            Mark the question as "QUESTION: " and mark the answer as "ANSWER: ". 
            {context}
        """)



GENERATE_FACTOID_QUESTION = ("""
            You are a teacher who is preparing an exam paper and the solution key for their students. 
            Using the following text as context generate one Factoid-type Questions randomly from 
            [what, which, when, who, how].
            Higlight the part of context that corresponds to the answer as "CONTEXT : "
            and the part that corresponds to the question as "QUESTION :"..
            {context}
        """)

GENERATE_LIST_QUESTION = ("""
            You are a teacher who is preparing an exam paper for their students. 
            Using the following text as context generate one List-type Question
            Do not provide the answer: 
            {context}
        """)


GENERATE_CASUAL_QUESTION = ("""
            You are a teacher who is preparing an exam paper and the solution key for their students. 
            Using the following text as context and generate only one Causal Question [why or how].
            Higlight the part of context that corresponds to the answer as "CONTEXT : " 
            and the part that corresponds to the question as "QUESTION :".
            {context}
        """)


GENERATE_HYPOTHETICAL_QUESTION = ("""
            You are a teacher who is preparing an exam paper for their students. 
            Using the following text as context and generate only one Hypothetical Questions
            Do not provide the answer:
            {context}
        """)

