
#  Local AI 

Welcome to the Local AI project! This project uses a pre-trained language model to generate poems in the beautiful Persian language. 

##  Quick Start

To get started with this project, follow these simple steps:

1. **Install Prerequisites:** Make sure you have Python and pip installed on your system. Then, install the required libraries:

   ```bash
   pip install transformers
   ```

2. **Run the Code:** Execute the Python script:

   ```bash
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the actual name of your Python file.

##  Code Explanation

The core code utilizes the `transformers` library to load a pre-trained language model, specifically `gpt2`. This model has been trained on a massive dataset of text and can generate various forms of text, including poems.

```python
from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')  # Load a pre-trained language model

prompt = "Your Prompt"
result = generator(prompt, max_length=100)
print(result[0]['generated_text'])
```

   * The first line imports the `pipeline` function from the `transformers` library. This function is used to create a pipeline for text generation.
   * The second line creates a pipeline for text generation. The `gpt2` model is selected as the pre-trained model.
   * The third line sets a prompt for the model. This prompt can be any text that you want the model to base its poem on.
   * The fourth line calls the `generator` function to generate text. The `max_length` argument specifies the maximum length of the generated text.
   * The fifth line prints the generated text.

## ✨ Tips & Tricks ✨

   * Experiment with different prompts to generate a variety of poems.
   * Adjust the `max_length` argument to control the length of the poem.
   * You can also try other pre-trained language models by changing the model name in the second line of the code.

##  Contributing

Contributions to this project are welcome! Feel free to submit a pull request if you have any improvements or suggestions.

-----

## ⚙️ How to Run the Code ⚙️

1. **Install Python and pip:** If you don't have Python and pip installed, download and install them from the official Python website: [https://www.python.org/](https://www.python.org/)

2. **Install `transformers`:** Open your terminal and run the following command:

   ```bash
   pip install transformers
   ```

3. **Save the Code:** Copy the code provided above and save it in a file named `poem_generator.py` (or any name you prefer).

4. **Run the Script:** Navigate to the directory where you saved the file in your terminal and run the following command:

   ```bash
   python poem_generator.py
   ```

5. **View the Output:** The generated poem will be printed in your terminal.

## Example

For example, if you want to generate a poem about "love," you can modify the code like this:

```python
from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

prompt = "عشق"  # عشق means "love" in Persian
result = generator(prompt, max_length=100)
print(result[0]['generated_text'])
```

This will generate a poem related to the topic of "love" in Persian.

```
