from model_loading import chatbot_response


def prediction(query):
    if query in ['quit', 'exit', 'bye']:
        start = False
    try:
        res = chatbot_response(query)
        return res
    except BaseException as e:
        print(str(e))
