<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  import { onAuthStateChanged } from 'firebase/auth';
  import { auth } from '$lib/firebase';

  onMount(() => {
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      setTimeout(() => {
        if (user) {
          goto('/home');
        } else {
          goto('/login');
        }
      }, 2500); // 2.5 seconds delay
    });

    return () => unsubscribe();
  });
</script>


<style>
  .spin {
    animation: spin 2s linear infinite;
  }

  @keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }
</style>

<div class="min-h-screen bg-[#3a3b4b] text-[#e9e4d3] flex flex-col items-center justify-center font-serif">
  <img src="/Logo Beige.png" alt="Logo" class="w-16 h-16 mb-6 spin" />
  <h1 class="text-2xl font-extrabold tracking-wide">Thought Partner</h1>
  <p class="text-sm mt-2">Executive insight in your pocket.</p>
</div>
