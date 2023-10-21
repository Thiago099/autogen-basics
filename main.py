from autogen import AssistantAgent, UserProxyAgent

config_list = [
    {
        'model': 'open_ai',
        'api_base': 'http://localhost:1234/v1',
        'api_key': 'null'
    }
]

llm_config={
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}


assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})

user_proxy.initiate_chat(assistant, message="Find the distance between two points in js")