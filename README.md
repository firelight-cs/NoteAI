# NoteAI 

A simple utility that will help in the difficult process of studying. The point of this application (in the future) is to organize notes that can be conveniently edited and supplemented using AI as an assistant.

## Features
At the moment the utility is under development and has no basic functionality. Even the functionality that is available is not designed for further contribution (due the architecture issues)
    
### Note maker (from URL link or via local video)
The utility can take a *url link* from YouTube and by audio from the video make a short note with most important information. 

**Pipeline:**

* It basically takes the video and download it using [yt-dlp module](https://github.com/yt-dlp/yt-dlp) and convert into format of mp3 (or any other format).

* Next model transcribe speech to text and store it into file (I use [whiper-large-v3 multilanguage](huggingface.com/openai/whisper-large-v3))

* Then this transcribed text processed with great module [sumy - text summarizer](https://github.com/miso-belica/sumy). But for my program I use [forked version](https://github.com/firelight-cs/sumy) since it has russian language (I don't know why the author didn't add Russian language support)

--------------------
By the way, you can use different summarize algorithms 
```python
# -*- coding: utf-8 -*-
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.kl import KLSummarizer 
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.sum_basic import SumBasicSummarizer
from sumy.summarizers.reduction import ReductionSummarizer

```
[you can read the brief documentation here](https://github.com/miso-belica/sumy/blob/main/docs/summarizators.md)


## Future
1. Organize the file structure and code so functionality can be extended in future
2. Try more light weighted library for S2T translation
3. Package the utility so that it can be downloaded via package manager (with dependencies)
4. Add tests and evaluations for models
5. Write a proper documentation
6. Add basic frontend and GUI
7. Integrate with Obsidian (I just love it)

#### Last update 31.12.2024