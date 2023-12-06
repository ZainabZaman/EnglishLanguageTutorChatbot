import azure.cognitiveservices.speech as speechsdk
import threading 
import wave 
import time
import string

speech_key = "YOUR_AZURE_SPEECH_STUDIO_KEY"
service_region = "eastus"
wrong_pronounce = []
import tts
is_listening = False

def pronunciation_assessment_from_microphone(language, reference):
    """Performs one-shot pronunciation assessment asynchronously with input from microphone.
        See more information at https://aka.ms/csspeech/pa"""

    config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    config.set_property(speechsdk.PropertyId.SpeechServiceConnection_EndSilenceTimeoutMs, "3000")

    # reference_text = ""
    pronunciation_config = speechsdk.PronunciationAssessmentConfig(
        reference_text=reference,
        grading_system=speechsdk.PronunciationAssessmentGradingSystem.HundredMark,
        granularity=speechsdk.PronunciationAssessmentGranularity.Phoneme,
        enable_miscue=True)

    # Creates a speech recognizer, also specify the speech language
    recognizer = speechsdk.SpeechRecognizer(speech_config=config, language=language)
    reference_text = reference

    pronunciation_config.reference_text = reference_text
    pronunciation_config.apply_to(recognizer)

    # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
    # shot evaluation.
    # For long-running multi-utterance pronunciation evaluation, use start_continuous_recognition() instead.
    is_listening = True
    print('Listening...')
    result = recognizer.recognize_once_async().get()
    is_listening = False
    

    # Check the result
    print('Evaluating Results...')
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print('Recognized: {}'.format(result.text))
        print('  Pronunciation Assessment Result:')

        pronunciation_result = speechsdk.PronunciationAssessmentResult(result)
        accuracy = pronunciation_result.accuracy_score
        pronunciation_score = pronunciation_result.pronunciation_score
        completeness_score = pronunciation_result.completeness_score
        fluency_score = pronunciation_result.fluency_score
        print('    Accuracy score: {}, Pronunciation score: {}, Completeness score : {}, FluencyScore: {}'.format(
            accuracy, pronunciation_score, completeness_score, fluency_score
        ))
        print('  Word-level details:')
        for idx, word in enumerate(pronunciation_result.words):
            print('    {}: word: {}, accuracy score: {}, error type: {};'.format(
                idx + 1, word.word, word.accuracy_score, word.error_type
            ))
            # wrong_pronounce.append(word)
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

    return pronunciation_result