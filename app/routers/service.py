# ---------------------------------------------------------------------------- #
#                      Language Model Service                 #
# ---------------------------------------------------------------------------- #
# This section contains API entpoints for generating responses from the model.

from fastapi import APIRouter, Body, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from app.schemas.userRequest import UserRequest, SystemResponse
from app.model import model, tokenizer
from app.schemas.key import APIKey
from app.auth import get_api_key


router = APIRouter(responses={404: {"description": "Not Found"}})

# ---------------------------- Fetch Documents --------------------------- #


@router.get(
    path="/info/model",
    summary="Returns model config",
    response_description="Model Config",
)
async def getModelInfo(api_key: APIKey = Depends(get_api_key)):
    """
    Returns model configuration of the model.
    """

    result = model.config.to_dict()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=result,
    )


@router.get(
    path="/info/tokenizer",
    summary="Returns tokenizer config.",
    response_description="Tokenizer Config",
)
async def getTokenizerInfo(api_key: APIKey = Depends(get_api_key)):
    """
    Returns tokenizer configuration used to preprocess the input.
    """

    result = {"all_special_tokens": tokenizer.all_special_tokens,
              "all_special_ids": tokenizer.all_special_ids,
              "vocab_size": tokenizer.vocab_size,
              "model_max_length": tokenizer.model_max_length,
              "max_len_sentences_pair": tokenizer.max_len_sentences_pair,
              # "sos_token": tokenizer.sos_token, "sos_token_id": tokenizer.sos_token_id,
              "eos_token": tokenizer.eos_token, "eos_token_id": tokenizer.eos_token_id,
              "unk_token": tokenizer.unk_token, "unk_token_id": tokenizer.unk_token_id,
              "mask_token": tokenizer.mask_token, "mask_token_id": tokenizer.mask_token_id,
              "pad_token": tokenizer.pad_token, "pad_token_id": tokenizer.pad_token_id}

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=result,
    )


@router.put(
    path="/generate",
    summary="Returns generated response.",
    response_description="Returns generated response from the model given the input prompt.",
    response_model=SystemResponse,
)
async def generateResponse(api_key: APIKey = Depends(get_api_key), request: UserRequest = Body(...)):
    """
    Returns generated response from the model given the input prompt.
    """

    # Tokenize input sequence
    input_sequence = tokenizer(
        request.prompt, return_tensors="pt"
    )

    # Pass input sequence as list into the model
    output = model.generate(**input_sequence, max_new_tokens=request.max_new_tokens, typical_p=request.typical_p, 
                            temperature=request.temperature, pad_token_id=tokenizer.eos_token_id,
                            num_beams=request.num_beams, num_return_sequences=request.num_return_sequences)

    # Decode model output to obtain entity candidates
    sequences = tokenizer.batch_decode(output, skip_special_tokens=False)
    response = jsonable_encoder(SystemResponse(sequences=sequences))

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response,
    )
