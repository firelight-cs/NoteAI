import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

import time

class SpeechToText():
    def __init__(self, language="english", model_id="openai/whisper-large-v3"):
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

        self.model = AutoModelForSpeechSeq2Seq.from_pretrained(
            model_id, torch_dtype=self.torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
        )
        self.model.to(self.device)

        self.processor = AutoProcessor.from_pretrained(model_id)

        self.pipe = pipeline(
            "automatic-speech-recognition",
            model=self.model,
            tokenizer=self.processor.tokenizer,
            feature_extractor=self.processor.feature_extractor,
            # chunk_length_s=30,
            # batch_size=5,
            torch_dtype=self.torch_dtype,
            device=self.device,
        )

        # kwargs for the pipeline (not neccaesary, you can just put the return_timestamps=True to the pipe)
        self.generate_kwargs = {
            "max_new_tokens": 445,
            "num_beams": 1,
            "condition_on_prev_tokens": False,
            "compression_ratio_threshold": 1.35,  # zlib compression ratio threshold (in token space)
            "temperature": (0.0, 0.2, 0.4, 0.6, 0.8, 1.0),
            "logprob_threshold": -1.0,
            "no_speech_threshold": 0.6,
            "return_timestamps": True,
            "language":language, # the variable we put in instance of class
        }

    def transcribe_audio(self, audio_path):
        result = self.pipe(audio_path, generate_kwargs=self.generate_kwargs)
        return result["text"]
