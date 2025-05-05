<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  onMount(() => {
    setTimeout(() => {
      goto('/login');
    }, 2000); // 2 seconds
  });
</script>

<!-- src/routes/+page.svelte -->
<div class="min-h-screen bg-[#3a3b4b] text-[#e9e4d3] flex flex-col items-center justify-center font-serif">
  <img src="/logo.png" alt="Logo" class="w-16 h-16 mb-6" />

  <h1 class="text-2xl font-extrabold tracking-wide">Thought Partner</h1>
  <p class="text-sm mt-2">Executive insight in your pocket.</p>
</div>
