import os
import openai
import config

import os
import openai
openai.organization = "org-CRabOIXOc3YIcgWhE9lH78xH"
openai.api_key = os.getenv("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")
openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)
