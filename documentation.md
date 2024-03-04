
# Effect of chunking PUBMED abstracts in retreival and prediction using LLMs

Authors of Repo:

1.  ngmars - Nitish Gopinath 
	1.1 Matrikel Nr - 4738384  
	1.2 Course: Data and Computer Science, Master
	1.3 Email: nitish.gopinath@stud.uni-heidelberg.de
2.  Dilmukhammed - Turdimuratov Dilmukhammed 
	2.1 Matrikel Nr - 4738284
3.  Richa Garg
4.  Palkin Sing

#### Advisor:   John Ziegler

## Contributions
#### Nitish Gopinath 
- Data extraction
- Data Cleaning
- Vector DB Setup
- Vector DB indexing
- Gemini LLM setup
- Gradio UI setup
- Question-Answer Generation
- Evalutation
- Stress testing

#### Turdimuratov Dilmukhammed
- Data extraction
 
## Overview
This project showcases the development and implementation of a sophisticated text retrieval system utilizing the power of Google Cloud's Vertex AI and the OpenSearch engine. The primary focus of the project is to efficiently extract and query abstracts containing the word "intelligence" from the vast PUBMED database, a critical resource in the biomedical and life sciences domain.


## Objective
The goal of this project is to create a scalable and effective solution for researchers and professionals seeking specific insights related to "intelligence" within the biomedical field. By leveraging the advanced capabilities of Vertex AI for machine learning operations and OpenSearch for search and analytics, the project aims to facilitate a more intuitive and rapid retrieval of relevant information.

## Prior work
The current project significantly differs from prior research that primarily relies on GPT-3 for several key reasons:

1. **Focused Domain Expertise:**
   - While prior work focuses on the general domain of news articles, our project specifically targets the biomedical and life sciences domain.
   - The use of Gemini-pro as the language model, integrated with Gradio, demonstrates a commitment to domain-specific language processing for improved understanding and relevance in biomedicine.

2. **Customized OpenSearch Vector Database:**
   - Instead of solely relying on the inherent capabilities of GPT-3, our project integrates OpenSearch with a customized vector database.
   - The inclusion of different indexing strategies, such as chunking based on title, authors, and abstract, or abstract-only indexing, tailors the search experience to the specific requirements of biomedical researchers.

3. **Diverse Evaluation Metrics:**
   - While prior research evaluates model outputs using domain expert feedback, our project employs a comprehensive set of evaluation metrics, including Bertscore, Rouge score, and Bleu score.
   - This multifaceted approach ensures a more nuanced understanding of the system's performance, going beyond the limitations of single-axis evaluations.

4. **Machine Learning Operations with Vertex AI:**
   - The integration of Vertex AI for machine learning operations in the current project enhances scalability and optimization.
   - This approach ensures that the text retrieval system not only understands user queries but also efficiently processes and retrieves relevant information from the PUBMED database.

5. **OpenSearch for Evidence Synthesis:**
   - The project addresses the challenge of aggregating evidence from multiple biomedical articles, a task that GPT-3 struggles with in prior research.
   - The use of OpenSearch and customized indexing strategies facilitates the synthesis of information across multiple documents, addressing the limitations highlighted in the previous work.

By focusing on domain-specific challenges, utilizing a diverse set of evaluation metrics, and integrating advanced technologies like OpenSearch and Vertex AI, our project represents a significant advancement in the field of biomedical text retrieval and intelligence extraction compared to prior work predominantly relying on GPT-3.


## Approach

  The foundation of the project lies in the integration of cutting-edge technologies, including the use of the Gemini-pro language model, Gradio for an intuitive chatbot interface, and the strategic employment of OpenSearch for efficient text indexing and retrieval.

To enhance the understanding of user queries and improve response quality, the Gemini-pro language model is employed for advanced natural language processing. The chatbot UI, developed with Gradio, offers a seamless and interactive platform for users to engage with the system, providing a user-friendly experience.
The prompts have been engineered with great care, so as to ensure that no data outside the retreived context is utilised
```
- Use only the GIVEN research information above and answer the user question. Try to justify your answer using the research information and support with examples (attribute authors if present) from the context.

- Respond with the answer.

- If you cannot find the answer to the user question, ask user to rephrase or provide more context.
```
The core innovation lies in the integration of OpenSearch as the database engine, offering versatile indexing strategies tailored to biomedical intelligence extraction. Three distinctive indexing approaches have been implemented, including chunking based on title, authors, and abstract; abstract-only chunking; and no chunking. This customization ensures that the system caters to a wide array of user preferences and research requirements.

To evaluate the system's performance comprehensively, a diverse set of metrics, including Bertscore, Rouge score, and Bleu score, has been employed. These metrics provide a nuanced assessment of the system's ability to generate relevant and accurate responses.

## Experimental Setup

### Data
The dataset comprises abstracts extracted from the PUBMED database, specifically filtered to include only those texts that contain the word "intelligence." This criterion was chosen to target a niche yet significant area of research within the biomedical and life sciences community, encompassing topics such as artificial intelligence in diagnostics, cognitive intelligence in neurobiology, and more.

We utilised the Esearch utility from PUBMED to extract the required data. We ran the command ```esearch -db pubmed -query "("intelligence"[Title/Abstract]) AND ((fha[Filter]) AND (2014:2024[pdat]))" | efetch -format xml > pubmed_results.xml```  to save all data to the pubmed_results.xml file

### Chatbot UI with Gradio

The project incorporates a user-friendly chatbot interface created using Gradio. Gradio simplifies the interaction between users and the text retrieval system, providing an intuitive and accessible means for querying the indexed PUBMED abstracts related to "intelligence."

### Gemini-pro Language Model (LLM)

-   Advanced Language Processing: The Gemini-pro language model is utilized for natural language understanding, enabling the system to comprehend user queries effectively and generate coherent responses.
-   State-of-the-Art Capabilities: Gemini-pro is chosen for its cutting-edge features, enhancing the quality and relevance of the responses provided by the chatbot.

### OpenSearch Vector DB with Three Indexes

#### 1. Chunking - Title + Authors + Abstract

This index combines information from the title, authors, and abstract of the PUBMED abstracts. It allows users to perform comprehensive searches that consider multiple aspects of the research papers, providing a holistic view of the relevant literature.

#### 2. Chunking - Abstract

This index focuses solely on the abstracts of the research papers. It streamlines the search process for users who may be primarily interested in the core content and findings presented in the abstracts related to "intelligence."

#### 3. No Chunking

This index does not involve any specific chunking and indexes the entire content as a single unit. It provides a baseline for comparison against the chunked indexes, offering insights into the impact of different indexing strategies on search performance.

### Evaluation Metrics

The project's performance is evaluated using three key metrics:

#### Bertscore

Bertscore assesses the quality of text similarity between the retrieved documents and the ground truth. This metric leverages BERT embeddings to capture semantic similarity, providing a nuanced evaluation of the relevance of the retrieved abstracts.

#### Rouge Score

Rouge (Recall-Oriented Understudy for Gisting Evaluation) Score measures the overlap of n-grams between the retrieved documents and the ground truth. It provides insights into the recall of relevant information within the retrieved abstracts.

#### Bleu Score

Bleu (Bilingual Evaluation Understudy) Score evaluates the precision of the text retrieval system by comparing the n-grams in the retrieved documents with those in the ground truth. It quantifies how well the system captures the specific details present in the relevant abstracts.

---
## Result
Based on the obtained data, we can always witness that the data without chunking demonstrates a higher bleu score of 0.05, a higher overall roughe score and a higher bertscore precision, f1 and recall

## Conclusion

This project has successfully demonstrated a novel approach to intelligence extraction from biomedical literature by integrating advanced technologies such as the Gemini-pro language model, Gradio for an interactive UI, and OpenSearch for efficient text retrieval. The implementation of three distinct indexing strategies within OpenSearch ensures adaptability to diverse user preferences, enriching the search experience in the complex landscape of PUBMED abstracts.

The multifaceted evaluation using Bertscore, Rouge score, and Bleu score provides a comprehensive understanding of the system's performance, showcasing its ability to generate relevant and accurate responses. Additionally, addressing the challenge of synthesizing evidence across multiple articles through OpenSearch marks a significant advancement compared to previous limitations observed in GPT-3-based approaches.

This project lays a foundation for enhanced biomedical text retrieval, offering a specialized tool for researchers and professionals seeking intelligence-related abstracts. The collaboration of Gemini-pro, Gradio, and OpenSearch not only improves the quality of responses but also enhances the overall user experience, promoting efficient exploration of intelligence within the biomedical domain.

## Future Work

The project's success opens avenues for exciting future enhancements and expansions:

1.  **Dataset Enrichment:**
    
    -   Continual expansion of the dataset to encompass a broader range of biomedical and life sciences topics, ensuring the system remains relevant and adaptable to emerging research areas.
2.  **Algorithm Refinement:**
    
    -   Ongoing refinement of search algorithms within OpenSearch to improve result relevance, incorporating user feedback to enhance the system's intelligence extraction capabilities.
3.  **UI Design Improvements:**
    
    -   Iterative improvements to the Gradio-based chatbot UI for a more seamless and enjoyable user experience, ensuring accessibility and ease of use for a wider audience.
4.  **Integration of Emerging Models:**
    
    -   Exploration and integration of emerging language models and technologies to further enhance the system's natural language understanding capabilities and overall performance.
5.  **Community Collaboration:**
    
    -   Encouraging collaboration with the biomedical research community to gather insights, feedback, and suggestions for continuous improvement, fostering a community-driven approach to refining the system.

This project serves as a stepping stone toward a more intelligent and adaptive platform for biomedical text retrieval, laying the groundwork for a future where researchers can seamlessly navigate and extract valuable insights from the ever-expanding realm of biomedical literature.
  

## Reference 

- Wang  S,  Scells  H,  Koopman  B,  Zuccon  G.  Can  chatgpt  write  a  good boolean  query  for  systematic  review  literature  search?  arXiv  preprint arXiv.  2023.  https://doi.org/10.48550/arXiv.2302.03495.

- Shaib  C,  Li  M,  Joseph  S,  Marshall  I,  Li  JJ,  Wallace  B.  Summarizing, simplifying,  and  synthesizing  medical  evidence  using  GPT-3  (with varying  success).  Toronto,  Canada:  Association  for  Computational Linguistics;  2023:1387–1407.

- Tang  L,  Sun  Z,  Idnay  B,  et  al.  Evaluating  large  language  models  on medical  evidence  summarization.  NPJ  Digit  Med.  2023;6:158.

- Peng  Y,  Rousseau  JF,  Shortliffe  EH,  Weng  C.  AI-generated  text  may have  a  role  in  evidence-based  medicine.  Nat  Med.  2023;29:1593–1594.

- Wadhwa  S,  DeYoung  J,  Nye  B,  Amir  S,  Wallace  BC.  Jointly  extracting interventions,  outcomes,  and  ﬁndings  from  RCT  reports  with  LLMs. arXiv.  2023.  https://doi.org/10.48550/arXiv.2305.03642.

- Jin  Q,  Yang  Y,  Chen  Q,  Lu  Z.  GeneGPT:  Augmenting  large  language  models  with  domain  tools  for  improved  access  to  biomedical information.  arXiv  preprint  arXiv.  2023.  https://doi.org/10.48550/arXiv.2304.09667.

- Jin  Q,  Leaman  R,  Lu  Z.  Retrieve,  summarize,  and  verify:  how  will ChatGPT  affect  information  seeking  from  the  medical  literature? J  Am  Soc  Nephrol.  2023;34(8):1302–1304.

- Gutiérrez  BJ,  McNeal  N,  Washington  C,  et  al.  Thinking  about  GPT-3  in-context  learning  for  biomedical  IE?  Think  again.  Findings  of the  association  for  computational  linguistics.  EMNLP.  2022.

- Coppola  F,  Faggioni  L,  Gabelloni  M,  et  al.  Human,  all  too  human? An  all-around  appraisal  of  the  “artiﬁcial  intelligence  revolution”in medical  imaging.  Front  Psychol.  2021;12:710982.

