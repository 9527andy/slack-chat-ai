from .geminiai import GeminiAI

def _get_gemini_prodiver():
    return GeminiAI()


def get_gemini_prodiver_response(user_input):
    try:
        prodiver = _get_gemini_prodiver()
        response = prodiver.generate_ai_response(user_input)
        return response
    except Exception as e:
        raise e
