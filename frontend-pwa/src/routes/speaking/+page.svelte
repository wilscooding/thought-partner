<script>
  import { page } from '$app/stores';
  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';

  let tp = { name: 'Thought Partner', image: '/default-avatar.png' };
  let isListening = false;
  let mediaRecorder;
  let audioChunks = [];
  let mediaStream;

  $: tp.name = $page.url.searchParams.get('name') || 'Thought Partner';
  $: tp.image = $page.url.searchParams.get('image') || `/${tp.name}.png`;

  onMount(() => {});
  
  async function startListening() {
    if (!isListening) {
      isListening = true;
      mediaStream = await navigator.mediaDevices.getUserMedia({ audio: true });

      let requestedMime = '';
      if (MediaRecorder.isTypeSupported('audio/webm;codecs=opus')) {
        requestedMime = 'audio/webm;codecs=opus';  // Chrome/Android
      } else if (MediaRecorder.isTypeSupported('audio/mp4')) {
        requestedMime = 'audio/mp4';               // Safari/iOS (AAC)
      }

      mediaRecorder = new MediaRecorder(
        mediaStream,
        requestedMime ? { mimeType: requestedMime } : undefined
      );

      audioChunks = [];

      mediaRecorder.ondataavailable = (e) => audioChunks.push(e.data);
      mediaRecorder.onstop = async () => {
        // Use the ACTUAL mime the recorder produced
        const actualMime = mediaRecorder.mimeType || requestedMime || 'audio/webm';
        const blob = new Blob(audioChunks, { type: actualMime });

        // Pick extension based on actual mime
        const base = actualMime.split(';', 1)[0];
        let ext = 'webm';
        if (base === 'audio/mp4') ext = 'm4a';
        else if (base === 'audio/mpeg') ext = 'mp3';
        else if (base === 'audio/ogg') ext = 'ogg';

        await handleSpeak(blob, ext);
        mediaStream.getTracks().forEach((t) => t.stop());
      };

      mediaRecorder.start();
    } else if (mediaRecorder && mediaRecorder.state === 'recording') {
      mediaRecorder.stop();
      isListening = false;
    }
  }

  async function handleSpeak(audioBlob, ext) {
    isListening = false;

    const formData = new FormData();
    formData.append('audio', audioBlob, `recording.${ext}`);

    try {
      const sttRes = await fetch('http://localhost:8000/api/stt', { method: 'POST', body: formData });
      if (!sttRes.ok) {
        console.error('STT error:', sttRes.status, await sttRes.text());
        return;
      }
      const { transcript } = await sttRes.json();
      console.log('Transcript:', transcript);

      const converseRes = await fetch('http://localhost:8000/api/converse/text', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: transcript, selected_name: tp.name })
      });
      if (!converseRes.ok) {
        console.error('Converse error:', converseRes.status, await converseRes.text());
        return;
      }
      const data = await converseRes.json();
      console.log('AI Response:', data.ai_response);

      if (data.audio_url) {
        const audio = new Audio(data.audio_url); // should be MP3 from backend
        audio.play();
      } else {
        console.error('No audio URL returned from backend.');
      }
    } catch (err) {
      console.error('Error in handleSpeak:', err);
    }
  }

  const handleEndCall = () => {
    goto(`/call-ended?name=${encodeURIComponent(tp.name)}&image=${encodeURIComponent(tp.image)}`);
  };
</script>

<div class="call-container">
  <h1 class="call-heading">Speaking To<br />{tp.name}</h1>
  <div class="avatar-wrapper"><img src={tp.image} alt={tp.name} class="avatar-img" /></div>
  <button class="speak-btn" on:click={startListening}>
    {isListening ? 'Stop Speaking' : 'Start Speaking'}
  </button>
  <div><img src="/Logo Gold.png" alt="Logo" class="avatar-logo" /></div>
  <button class="call-end-btn" on:click={handleEndCall}>End Call</button>
</div>
