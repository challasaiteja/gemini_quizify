import streamlit as st
import json
from task_3 import DocumentProcessor
from task_4 import EmbeddingClient
from task_5 import ChromaCollectionCreator
from task_8 import QuizGenerator
from task_9 import QuizManager
from config import EMBED_CONFIG, print_config_status

if __name__ == "__main__":
    
    # Display configuration status
    print_config_status()
    
    embed_config = EMBED_CONFIG
    
    # Add Session State
    if 'question_bank' not in st.session_state or len(st.session_state['question_bank']) == 0:
        
        # Step 1: init the question bank list in st.session_state
        st.session_state['question_bank'] = []
    
        screen = st.empty()
        with screen.container():
            st.header("Quiz Builder")
            
            # Create a new st.form flow control for Data Ingestion
            with st.form("Load Data to Chroma"):
                st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")
                
                processor = DocumentProcessor()
                processor.ingest_documents()
            
                embed_client = EmbeddingClient(**embed_config) 
            
                chroma_creator = ChromaCollectionCreator(processor, embed_client)
                
                # Step 2: Set topic input and number of questions
                topic_input = st.text_input("Enter the topic for the quiz:")
                questions = st.number_input("Enter the number of questions:", min_value=1, max_value=10, step=1)
                    
                submitted = st.form_submit_button("Submit")
                
                if submitted:
                    chroma_creator.create_chroma_collection()
                        
                    if len(processor.pages) > 0:
                        st.write(f"Generating {questions} questions for topic: {topic_input}")
                    
                    # Step 3: Initialize a QuizGenerator class using the topic, number of questions, and the chroma collection
                    generator = QuizGenerator(topic_input, questions, chroma_creator)
                    question_bank = generator.generate_quiz()
                    # Step 4: Initialize the question bank list in st.session_state
                    st.session_state['question_bank'] = question_bank
                    # Step 5: Set a display_quiz flag in st.session_state to True
                    st.session_state['display_quiz'] = True
                    # Step 6: Set the question_index to 0 in st.session_state
                    st.session_state['question_index'] = 0
                    st.rerun()

    elif True:
        
        st.empty()
        with st.container():
            st.header("Generated Quiz Question: ")
            quiz_manager = QuizManager(st.session_state['question_bank'])
            
            # Format the question and display it
            with st.form("MCQ"):
                # Step 7: Set index_question using the Quiz Manager method get_question_at_index passing the st.session_state["question_index"]
                index_question = quiz_manager.get_question_at_index(st.session_state["question_index"])
                
                # Unpack choices for radio button
                choices = []
                for choice in index_question['choices']:
                    key = choice['key']
                    value = choice['value']
                    choices.append(f"{key}) {value}")
                
                # Display the Question
                st.write(f"{st.session_state['question_index'] + 1}. {index_question['question']}")
                answer = st.radio(
                    "Choose an answer",
                    choices,
                    index = None
                )
                
                answer_choice = st.form_submit_button("Submit")
                
                if answer_choice and answer is not None:
                    correct_answer_key = index_question['answer']
                    if answer.startswith(correct_answer_key):
                        st.success("Correct!")
                    else:
                        st.error("Incorrect!")
                    st.write(f"Explanation: {index_question['explanation']}")
            
            # Navigation buttons outside the form
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Next Question"):
                    quiz_manager.next_question_index(direction=1)
                    st.rerun()
            with col2:
                if st.button("Previous Question"):
                    quiz_manager.next_question_index(direction=-1)
                    st.rerun()
