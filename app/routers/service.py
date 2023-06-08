# ---------------------------------------------------------------------------- #
#                      Manage Multiple Documents of Corpus                 #
# ---------------------------------------------------------------------------- #
# This section contains API entpoints for managing documents in a corpus.

from fastapi import APIRouter, Body, status, Depends, Header
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from app.schemas.mention import EntityMention, EntityDisambiguated
from app.model import model, tokenizer
from app.schemas.key import APIKey
from app.auth import get_api_key
from typing import Dict, Optional, List
import json


router = APIRouter(responses={404: {"description": "Not Found"}})

# ---------------------------- Fetch Documents --------------------------- #


@router.get(
    path="/info/model",
    summary="Returns model config",
    response_description="Model Config",
)
async def getModelInfo(api_key: APIKey = Depends(get_api_key)):
    """
    Returns model configuration of the model used for entity linking.
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
    summary="Returns a list of candidate entities.",
    response_description="List of candidate entities",
    # response_model=EntityDisambiguated,
)
async def generateResponse(api_key: APIKey = Depends(get_api_key), request=Body({"prompt": "This is a test"})):
    """
    Returns a list of candidate entities.
    """

    input_sequence = tokenizer(
        # , is_split_into_words=True
        request.get("prompt"), return_tensors="pt"
    )

    print(input_sequence)

#     # input_sequence.to("cuda")

    # Pass input sequence as list into the model
    outputs = model.generate(
        **input_sequence,
        num_beams=5,
        num_return_sequences=5,
        # prefix_allowed_tokens_fn=lambda batch_id, sent: trie.get(sent.tolist()),
    )

    print(outputs)
    # Decode model output to obtain entity candidates
    response = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    # result = jsonable_encoder(EntityDisambiguated(candidates=candidates))

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response,
    )
