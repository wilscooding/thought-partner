<script lang="ts">
  let loading = false;
  let error: string | null = null;
  let transcript = '';
  let responseText = '';
  let audioUrl = '';

  async function handleUpload(event: Event) {
    loading = true;
    error = null;

    const file = (event.target as HTMLInputElement).files?.[0];
    if (!file) {
      error = 'No audio selected';
      loading = false;
      return;
    }

    const formData = new FormData();
    formData.append('audio', file);

    const BASE_URL = import.meta.env.DEV
    ? 'http://localhost:8000'
    : 'https://tp-backend-ds4h.onrender.com';

    try {
      const res = await fetch( `${BASE_URL}/api/stt`, {
        method: 'POST',
        body: formData
      });
      const json = await res.json();
      transcript = json.transcript;
      responseText = json.response_text;
      audioUrl = json.audio_url;
    } catch (e) {
      error = 'Error processing audio';
      console.error(e);
    }

    loading = false;
  }
</script>

<h1>🎤 Audio Conversational Interface</h1>

<input type="file" accept="audio/*" on:change="{handleUpload}" />

{#if loading}
  <p>⏳ Processing...</p>
{:else if error}
  <p style="color: red;">❌ {error}</p>
{:else if transcript}
  <div>
    <h2>User Transcript</h2>
    <p>{transcript}</p>
    <h2>AI Response</h2>
    <p>{responseText}</p>
    {#if audioUrl}
      <h3>🎧 Voice Playback</h3>
      <audio src="{audioUrl}" autoplay controls />
    {/if}
  </div>
{/if}
