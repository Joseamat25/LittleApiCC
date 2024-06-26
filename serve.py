import requests
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import CrossEncoder

from src.chunk_splitting import split_chunk

app = FastAPI()

MODEL_ID = "cross-encoder/ms-marco-MiniLM-L-12-v2"
model_cross_encoder = CrossEncoder(MODEL_ID)

class QuestionRanker(BaseModel):
    question: str
    total_chunks: list[str]

# class ModelInference():
#     def __init__(self, path_to_model):
#         self.model = CrossEncoder(path_to_model)

# @app.on_event("startup")
# def setup_model():
#     model_cross_encoder = CrossEncoder(MODEL_ID)

@app.get("/")
def home():
    return {"message": "Cross Encoder Model - Local Inference"}

@app.post("/inference_cross_encoder")
def re_rank(inputs: QuestionRanker):
    question = inputs.question
    total_chunks = inputs.total_chunks
    question_chunks_pairs = [(str(question), str(total_chunks[index])) for index in range(len(total_chunks))]
    list_scores = []
    for chunk in total_chunks:
        print(chunk)
        list_split_chunk = split_chunk(chunk)
        question_pair_chunk = [(str(question), str(list_split_chunk[index])) for index in range(len(list_split_chunk))]
        print(question_pair_chunk)
        scores = list(model_cross_encoder.predict(question_pair_chunk))
        scores = [float(score) for score in scores]
        print(scores)
        final_score = max(scores)
        print(final_score)
        print("==============================")
        list_scores.append(final_score)
    payload = [{"pair": question_chunks_pairs[index], "score": list_scores[index]} for index in range(len(question_chunks_pairs))]
    return payload

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)