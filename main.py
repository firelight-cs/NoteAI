import time
from textSummarizer import TextSummarizer
from read_write_edit import FileEdit

from extractAudio import AudioExtractor

from speech2text import SpeechToText

def main():

    # ----------------- Audio extraction --------------------------------------------------------
    file_path = 'cache'
    file_name = 'transcribed_text.txt'
    file = FileEdit(f'{file_path}/{file_name}')

    url = "https://youtu.be/YjPg4aft-c4?si=ncJCLmC-Yg1OGqj2"
    download_it = AudioExtractor(output_dir=file_path, audio_format="mp3")
    audio_file = download_it.download_audio(url) # return a path to the audio file
    
    # --------------------------------------------------------------------------------------------

    # ----------------- Speech to text -----------------------------------------------------------

    language = "russian" # it's not neccesary to declare the language, but it will help the model to understand the audio better
    start_t = time.time()
    transcription = SpeechToText(language)
    transcription_to_save = transcription.transcribe_audio(audio_file)
    text_file = 'transcribed_text.txt'
    file.write(transcription_to_save, f'{file_path}/{text_file}')
    end_t = time.time()
    execution_t = end_t - start_t
    print(f"\n\nExecution time: {execution_t} seconds")

    # --------------------------------------------------------------------------------------------

    # ----------------- Text summarization -------------------------------------------------------

    processed_text = TextSummarizer(language='russian', sentences_count=10)
    summary_result = processed_text.summarize_file(f'{file_path}/{text_file}')
    file.write(summary_result, f'{file_path}/summary.txt')

    return None

if __name__ == "__main__":
    main()
