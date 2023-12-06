import azure.cognitiveservices.speech as speechsdk

# weatherfilename = 'output.wav'
speech_key = "YOUR_AZURE_SPEECH_STUDIO_KEY"
service_region = "eastus"

# voice_name = 'en-US-JennyMultilingualNeural'
# input_text = "Hi, this is Jenny Multilingual"

def text_to_speech(voice_name, input_text, output_filename):

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_synthesis_voice_name = voice_name

    text = input_text

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    result = speech_synthesizer.speak_text_async(text).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        # Save the audio data to a WAV file
        audio_data = result.audio_data
        with open(output_filename, "wb") as wav_file:
            wav_file.write(audio_data)
        print(f"Audio saved to {output_filename}")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

# Call the function to perform text-to-speech and save to a WAV file
# text_to_speech(voice_name, input_text, weatherfilename)
