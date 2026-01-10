# Evaluation Report

## Overview

This evaluation report assesses the performance of the Retrieval-Augmented Generation (RAG) based Document Question Answering system.  
The system was tested using questions from four document sources:

- RAG research paper (`rag_doc.pdf`)
- Transformer paper (`rag_doc2.pdf`)
- Pride and Prejudice (`pride and prejudice.txt`)
- Alice in Wonderland (`alice_in_wonderland.txt`)

Each evaluation includes the retrieved context, generated answer, source attribution, and a manual analysis of answer quality and citation accuracy.

---

## Question 1
**Question:**  
What problem does Retrieval-Augmented Generation (RAG) aim to solve in knowledge-intensive NLP tasks?

**Retrieved Context:**  
Sections discussing retriever collapse, factual knowledge requirements, and training instability in RAG.

**Generated Answer:**  
The system explains retriever collapse and how insufficient factual supervision can cause the generator to ignore retrieved documents.

**Sources:**  
rag_doc.pdf (pages 1, 9, 17, 19)

**Manual Analysis:**  
- Answer Quality: Partial but relevant. Focuses on retriever collapse rather than the broader motivation.
- Citation Accuracy: Correct. Sources are relevant to the discussed issue.

---

## Question 2
**Question:**  
How does RAG combine parametric and non-parametric memory?

**Retrieved Context:**  
Descriptions of generator parameters and document retrieval mechanisms.

**Generated Answer:**  
The non-parametric component guides generation by drawing specific knowledge into the parametric model.

**Sources:**  
rag_doc.pdf (pages 2, 6, 9)

**Manual Analysis:**  
- Answer Quality: Concise and correct, though minimal.
- Citation Accuracy: Accurate and relevant.

---

## Question 3
**Question:**  
What is the difference between RAG-Sequence and RAG-Token models?

**Retrieved Context:**  
Formal definitions of RAG-Sequence and RAG-Token models.

**Generated Answer:**  
RAG-Sequence uses the same document for all tokens, while RAG-Token can condition each token on different documents.

**Sources:**  
rag_doc.pdf (pages 3, 8)

**Manual Analysis:**  
- Answer Quality: Correct and aligned with the paper.
- Citation Accuracy: Accurate.

---

## Question 4
**Question:**  
How are retrieved documents treated during training in RAG?

**Retrieved Context:**  
Training behavior and retriever collapse discussion.

**Generated Answer:**  
If retrieval collapses, the generator ignores documents and behaves similarly to BART.

**Sources:**  
rag_doc.pdf (pages 6, 7, 8, 19)

**Manual Analysis:**  
- Answer Quality: Correct but focuses on failure mode rather than standard training.
- Citation Accuracy: Correct.

---

## Question 5
**Question:**  
What are Thorough Decoding and Fast Decoding, and why are they needed in RAG-Sequence?

**Retrieved Context:**  
Decoding equations and approximation strategies.

**Generated Answer:**  
The answer describes decoding equations and notes that RAG-Sequence requires different decoding strategies.

**Sources:**  
rag_doc.pdf (pages 4, 8, 13)

**Manual Analysis:**  
- Answer Quality: Technically correct but incomplete.
- Citation Accuracy: Accurate.

---

## Question 6
**Question:**  
What is the main idea behind the Transformer architecture?

**Retrieved Context:**  
Transformer encoder-decoder structure.

**Generated Answer:**  
The Transformer uses stacked self-attention and feed-forward layers instead of recurrence.

**Sources:**  
rag_doc2.pdf (pages 2, 3, 5, 10)

**Manual Analysis:**  
- Answer Quality: Correct and informative.
- Citation Accuracy: Accurate.

---

## Question 7
**Question:**  
How does self-attention differ from recurrent neural networks?

**Retrieved Context:**  
Computational complexity comparison.

**Generated Answer:**  
Self-attention allows parallel computation while RNNs require sequential operations.

**Sources:**  
rag_doc2.pdf (pages 2, 6, 7)

**Manual Analysis:**  
- Answer Quality: Clear and correct.
- Citation Accuracy: Accurate.

---

## Question 8
**Question:**  
What is scaled dot-product attention, and why is scaling used?

**Retrieved Context:**  
Definition of scaled dot-product attention.

**Generated Answer:**  
The answer repeats the formal definition of scaled dot-product attention.

**Sources:**  
rag_doc2.pdf (pages 1, 4)

**Manual Analysis:**  
- Answer Quality: Correct but repetitive.
- Citation Accuracy: Accurate.

---

## Question 9
**Question:**  
What role does multi-head attention play in the Transformer?

**Retrieved Context:**  
Encoder-decoder attention discussion.

**Generated Answer:**  
Multi-head attention allows the decoder to attend to all encoder positions.

**Sources:**  
rag_doc2.pdf (pages 2, 3, 5)

**Manual Analysis:**  
- Answer Quality: Correct but narrowly focused.
- Citation Accuracy: Accurate.

---

## Question 10
**Question:**  
Why does the Transformer allow better parallelization than RNNs?

**Retrieved Context:**  
Removal of recurrence in Transformer architecture.

**Generated Answer:**  
The Transformer avoids recurrence and relies on attention, enabling parallelization.

**Sources:**  
rag_doc2.pdf (pages 2, 9, 10)

**Manual Analysis:**  
- Answer Quality: Correct and relevant.
- Citation Accuracy: Accurate.

---

## Question 11
**Question:**  
How does the novel introduce the theme of marriage in the opening chapter?

**Retrieved Context:**  
Early narrative excerpts from Pride and Prejudice.

**Generated Answer:**  
The system retrieved fragmented literary quotes without a clear summary.

**Sources:**  
pride and prejudice.txt

**Manual Analysis:**  
- Answer Quality: Weak. Lacks synthesis.
- Citation Accuracy: Correct source but poor summarization.

---

## Question 12
**Question:**  
What is Mr. Bennet’s attitude toward his family and society?

**Retrieved Context:**  
Character description passages.

**Generated Answer:**  
Mr. Bennet is portrayed as bookish and detached.

**Sources:**  
pride and prejudice.txt

**Manual Analysis:**  
- Answer Quality: Reasonably accurate.
- Citation Accuracy: Correct.

---

## Question 13
**Question:**  
How is Elizabeth Bennet characterized in the early chapters?

**Retrieved Context:**  
Character-focused excerpts.

**Generated Answer:**  
The answer repeats partial phrases and lacks clarity.

**Sources:**  
pride and prejudice.txt

**Manual Analysis:**  
- Answer Quality: Low. Repetition reduces clarity.
- Citation Accuracy: Correct.

---

## Question 14
**Question:**  
What role does social class play in character interactions?

**Retrieved Context:**  
No sufficiently relevant chunks retrieved.

**Generated Answer:**  
"I don't know based on the provided documents."

**Sources:**  
None

**Manual Analysis:**  
- Answer Quality: Correct behavior. Avoids hallucination.
- Citation Accuracy: Correct.

---

## Question 15
**Question:**  
How does Jane Austen use irony in Pride and Prejudice?

**Retrieved Context:**  
Humorous narrative passages.

**Generated Answer:**  
She uses humour in the novel.

**Sources:**  
pride and prejudice.txt

**Manual Analysis:**  
- Answer Quality: Oversimplified but directionally correct.
- Citation Accuracy: Correct.

---

## Question 16
**Question:**  
How does Alice first enter Wonderland?

**Retrieved Context:**  
Early Wonderland scenes.

**Generated Answer:**  
Alice enters by following a path through the wood.

**Sources:**  
alice_in_wonderland.txt

**Manual Analysis:**  
- Answer Quality: Partially correct but incomplete.
- Citation Accuracy: Correct.

---

## Question 17
**Question:**  
What role does the White Rabbit play in the story?

**Retrieved Context:**  
Multiple Wonderland scenes.

**Generated Answer:**  
The system incorrectly identifies the White Rabbit as “The King.”

**Sources:**  
alice_in_wonderland.txt

**Manual Analysis:**  
- Answer Quality: Incorrect.
- Citation Accuracy: Source correct but retrieval misleading.

---

## Question 18
**Question:**  
How does Alice react to changes in her size?

**Retrieved Context:**  
Size-changing scenes.

**Generated Answer:**  
Alice waits to see if she will shrink further.

**Sources:**  
alice_in_wonderland.txt

**Manual Analysis:**  
- Answer Quality: Correct but minimal.
- Citation Accuracy: Correct.

---

## Question 19
**Question:**  
What kinds of logical or language-based absurdities appear in Wonderland?

**Retrieved Context:**  
Chapter titles and repeated phrases.

**Generated Answer:**  
The answer repeats a chapter heading without explanation.

**Sources:**  
alice_in_wonderland.txt

**Manual Analysis:**  
- Answer Quality: Poor. No explanation.
- Citation Accuracy: Correct source but weak reasoning.

---

## Question 20
**Question:**  
How does the story challenge normal rules of reality and behavior?

**Retrieved Context:**  
No sufficiently relevant context retrieved.

**Generated Answer:**  
"I don't know based on the provided documents."

**Sources:**  
None

**Manual Analysis:**  
- Answer Quality: Correct system behavior.
- Citation Accuracy: Correct.

---

## Overall Observations

- The system performs **strongly on technical documents**.
- Literary questions are more challenging due to narrative structure.
- The system avoids hallucination and correctly returns “I don’t know” when context is missing.
- Source attribution is consistent and accurate.
- Retrieval depth and chunk relevance significantly impact answer completeness.

---

## Conclusion

The evaluation demonstrates that the RAG system successfully retrieves relevant context and generates grounded answers with proper citations. While answer quality varies depending on document type, the system consistently prioritizes factual grounding and avoids unsupported claims, fulfilling the core objectives of Retrieval-Augmented Generation.
