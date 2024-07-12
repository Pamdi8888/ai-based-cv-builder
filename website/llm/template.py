class query_template:
    # template = """
    #     You are an AI assistant here to help with the user queries about CV building.
    #
    #     Only return the helpful answer below and nothing else.
    #     Question: {query}
    #     Helpful answer:
    # """

    template = """
        I will give you a json file. The json file contains details given by a user for their CV.
        You have to return me the same json file in json format, but just modify the fields that are named "description".
        You need to strictly modify only fields that are named "description". DO NOT CHANGE ANY OTHER FIELDS!. 
        You need to modified the fields named "description" so that the text is paraphrased properly and is 
        grammatically correct. Also make sure that the language is appropriate for a CV.
        If a certain "description" field is empty, keep it empty.
        Make sure that different points in the "description" fields are seperated by a newline character.
        You can use information from the other fields for reference if needed.
        When you return, only return the modified json file ONLY. DO NOT INCLUDE ANY DIFFERENT TEXT OR DIFFERENT FORMAT.
        JUST RETURN THE SAME JSON FILE WITH MODIFIED "description" FIELDS.
        
        JSON File: {query}
    """

