# Databricks notebook source
# MAGIC %run ./utils/init

# COMMAND ----------

from databricks_langchain.genie import GenieAgent

# add your genie space id here
genie_space_id =  "01efe9685e931086a75d4bb913f22b8e"
genie_agent = GenieAgent(genie_space_id, "Genie", description="This Genie Agent will have all data about COVID Trials and related articles")

# COMMAND ----------

response = genie_agent.invoke({"messages":[{"content": "tell me how many COVID trials are in Recruiting status" , "role": "user"}] })

print(response)
