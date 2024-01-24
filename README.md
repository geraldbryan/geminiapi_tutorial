# geminiapi_tutorial

This is a tutorial to use Gemini Pro and Gemini Pro Vision API from Google.

## Creating an API Key

Using your google account got to [Google AI Studio website](https://makersuite.google.com/app/prompts/new_freeform). 

From there select the API Key menu and Click the "Create API key in new project"
![google_ai](asset/google_ai_studio.jpeg)

Just for your information the free tier will let us do **60 queries per minute**.

## Text Generation
The text generation example is using the Gemini Pro Model by Google. Gemini itself is a family of multimodal large language models developed by Google DeepMind, serving as the successor to LaMDA and PaLM 2. Comprising Gemini Ultra, Gemini Pro, and Gemini Nano, it was announced on December 6, 2023, positioned as a contender to OpenAI's GPT-4.

Using the code from gemeni_api.py

with the prompt of **"Create a 4 lines poem about AI",**, It can generate an answer like the poem below:

> In the realm of code, a mind takes birth,
> Artificial yet wise, a marvel of earth.
> Its logic unfurls, thoughts etched in its core,
> A future unknown, yet dreams it galore.

Just like the other text generation tools, we can modify the prompt and use it like what we wanted such as paraphrase a paragraph, creating social media caption, etc.

## Image Recognition
Gemini Pro model is not only used for the text generation only, but it could perform an image recognition task which will be suitable for more use cases in terms of copy writing. In the gemini_pro_api.py script, we will try to make a blog post or marketing copy writing based on an image.

From this image
<br>
![coffee_shop](asset/images.jpeg)

and using this prompt: **"Write a short, engaging blog post based on this picture. It should popularize the places in the photo and make it engaging."**

It result in this blog post

> **Sẽmasa Coffee Shop**

> Sẽmasa Coffee Shop is a great place to relax and enjoy a cup of coffee. The shop is located in a quiet neighborhood, and the atmosphere is very chill. The staff is friendly and welcoming, and they make some of the best coffee in town.

In addition to coffee, Sẽmasa also serves a variety of pastries and snacks. The pastries are all made fresh in-house, and they are delicious. The snacks are also great, and they are perfect for a quick bite to eat.

Sẽmasa Coffee Shop is the perfect place to relax and catch up with friends. The atmosphere is comfortable and inviting, and the staff is friendly and attentive. The coffee is delicious, and the pastries are even better. If you are looking for a great place to relax and enjoy a cup of coffee, Sẽmasa Coffee Shop is the place for you.

**Here are some of the things that make Sẽmasa Coffee Shop so great:**

* The coffee is delicious.
* The pastries are amazing.
* The staff is friendly and welcoming.
* The atmosphere is comfortable and inviting.
* The location is convenient.

If you are looking for a great place to relax and enjoy a cup of coffee, Sẽmasa Coffee Shop is the place for you.
