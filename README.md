# OpenAssistant API

## Installation

To set up this application and create a virtual environment, follow these steps:

1. Install `pyenv` by following the instructions in the [official documentation](https://github.com/pyenv/pyenv#installation).

2. Create a virtual environment for this application using `pyenv`. Open your terminal and execute the following commands:

   ```bash
   pyenv install 3.11
   pyenv virtualenv 3.11 openassistant-api
   pyenv activate openassistant-api
   ```

3. Install the required dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

## Run for Development

Run with reload enables

```
uvicorn app.api:app --reload --port 8080
```

or

```
python main.py
```

## Additional Resources

- Github: https://github.com/LAION-AI/Open-Assistant
- Huggigface: https://huggingface.co/OpenAssistant
- Model: https://huggingface.co/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5
- Base Model: https://huggingface.co/andreaskoepf/pythia-12b-pre-2000
- Webpage: https://open-assistant.io/dashboard
- Documentation: https://projects.laion.ai/Open-Assistant/docs/guides/developers
- API: https://projects.laion.ai/Open-Assistant/api
