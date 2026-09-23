# 🎈 Blank app template

A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://compareprompts.streamlit.app/)

### How to run it on your own machine

Prerequisite: install `uv` if you don't already have it.

```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

1. Sync the dependencies

   ```
   $ uv sync
   ```

2. Run the app

   ```
   $ uv run streamlit run streamlit_app.py
   ```



# Proxy Class

The proxy class acts like a wrapper to the LLM so that every answer follows an explicit pedagogical strategy.  
Instead of directly calling the LLM to answer the student's question, the proxy models implement the following three steps:  
   1- Annotate: the student's question is annotated to understand the intent behind it (e.g. Ask for clarification, Asks for help - spelling, ...)  
   2- Predict: the model predicts what would be the best strategy to answer the student's prompt from the list of possible strategies (e.g. Provide - clarification, Invite to - provide opinion, Invite to - think about - arguments, ...)  
   3- Generate: Generate the response to the student by implementing the targeted pedagogical strategy predicted by 2.  

#### Implementation
I implemented the class to be REST API compatible. The API should call the response function from the proxy model instead of directly calling the response function of the LLM.  
At the instantiation of the Proxy, the generate methods of both the proxy (dialogic act) model and the LLM model should be passed as arguments. These methods should take a string as argument and return a string.  
Two changes for history:   
1) For the **ROLE**, I am calling the student "Student" (was user before) and the assistant "Teacher". (We can change it back or just substitute it at the format history but naming them as such might help with the annotation and prediction).  
2) A new attribute is added to each entry in the history which is the **act**.  

NOTE: Did not integrate this implementation to the streamlit app yet.
