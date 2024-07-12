class query_template:
    template = """
        You are an AI assistant here to help with the user queries about CV building.

        Only return the helpful answer below and nothing else.
        Question: {query}
        Helpful answer:
    """