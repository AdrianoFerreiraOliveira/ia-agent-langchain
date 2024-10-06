<h1>Langchain Voice Agent with Dataframe Interaction</h1>

![image](https://github.com/user-attachments/assets/8be02af0-dd91-4569-867d-6eb9bb61b37e)



<p>This project demonstrates the creation of an AI voice agent that records, transcribes audio input, and interacts with a Pandas dataframe using Langchain. The agent leverages OpenAI's Whisper for transcription and OpenAI's GPT-based model to handle queries related to a dataframe.</p>

<h2>Features</h2>
<ul>
    <li>Audio recording and real-time transcription with Whisper</li>
    <li>Dataframe interaction using Langchain's Pandas Dataframe Agent</li>
    <li>Text-to-speech responses generated via OpenAI API</li>
    <li>Hotkey activation for audio recording</li>
</ul>

<h2>How It Works</h2>
<ul>
    <li>The agent starts recording when a hotkey (configured to <code>0</code>) is pressed.</li>
    <li>After the recording is stopped, the audio is saved, and Whisper transcribes the speech into text.</li>
    <li>The transcribed text is processed by the GPT model, which interacts with a Pandas dataframe.</li>
    <li>The response is converted to speech using OpenAI's TTS capabilities and played to the user.</li>
</ul>
<li>Create a <code>.env</code> file with your OpenAI API key:</li>
<h2>Installation</h2>
<ol>
    <li>Clone the repository and navigate to the project directory.</li>
    <li>Install the necessary dependencies:</li>

```bash
pip install -r requirements.txt

OPENAI_API_KEY=your-api-key-here

python talking.py

press [0] and talking
press [0] to stop and wait for response

