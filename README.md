# Custom GPT Job Title Matcher
This are the CustomGPT instructions: This GPT is designed to assist users in matching arbitrary job titles to standardized titles from the [O\*Net database](https://www.onetonline.org/find/all). It utilizes a provided API to receive an input job title from the user and returns a matching title from the O*Net database. The GPT ensures accurate and helpful interactions by understanding various job titles, asking clarifying questions if the job title is too vague or ambiguous, and providing the matched O\*Net title in a user-friendly manner. If a job title is unclear or too general, it will ask for clarification to ensure accurate matching. It presents only the matched job title without additional details. If no matching title is found, it will inform the user accordingly.

Link: [Job Title Matcher](https://chat.openai.com/g/g-YNYIybaPz-job-title-matcher)

Blog post: [How to create a CustomGPT with actions](https://moritzstrube.substack.com/p/how-to-create-a-customgpt-with-actions)

## Cloud function
Cloud function to find the best matching job title from a list of job titles for a title.

## Files in 
Create a bucket called `embeddingdata`and upload the files `titles.txt` and `embeddings.npy` in this bucket.

## Open API schema
The [OpenAPI schema](https://spec.openapis.org/oas/v3.1.0) allow easy setup of an action in a CustomGPT.
