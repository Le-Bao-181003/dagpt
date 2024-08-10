from langchain_openai import ChatOpenAI
import os

def load_llm(model_name):
    """Load Large Language Model.

    Args:
        model_name (str): The name of the model to load.

    Raises:
        ValueError: If the model_name is not recognized.

    Returns:
        ChatOpenAI: An instance of ChatOpenAI configured for the specified model.
    """
    
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    if model_name == "gpt-3.5-turbo":
        return ChatOpenAI(
            model=model_name,
            temperature=0.0, # do sang tao cua mo hinh chatgpt
            max_tokens=1000,
            openai_api_key=openai_api_key
        )
    elif model_name == "gpt-4o-mini":
        return ChatOpenAI(
            model=model_name,
            temperature=0.0,
            max_tokens=1000,
            openai_api_key=openai_api_key
        )
    else:
        raise ValueError(
            "Unknown model.\
                Please choose from ['gpt-3.5-turbo', 'gpt-4', ...]"
        )
