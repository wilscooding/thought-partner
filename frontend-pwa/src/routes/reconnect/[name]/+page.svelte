<script lang="ts">
  import { page } from '$app/stores';
  import { onMount } from 'svelte';
  import { db } from '$lib/firebase';
  import { doc, getDoc } from 'firebase/firestore';
  import MenuWrapper from '$lib/components/MenuWrapper.svelte';
	import { currentUser } from '$lib/stores/userStore';
  import { goto } from '$app/navigation';
  
    let tp = null;
    let error = null;
    let loading = true;

    $: slug= $page.params.name;

  onMount(async () => {
    try {
      const uid = $currentUser?.uid;
      if (!uid) {
        throw new Error('User not authenticated');
      }

      const tpRef = doc(db, 'users', uid, 'thoughtPartners', slug);
      const tpSnap = await getDoc(tpRef);

      if (!tpSnap.exists()) {
        error = "Thought partner not found";
        return;
      }
      tp = tpSnap.data();

    } catch (err) {
      error = err.message;
      console.error('Failed to load Thought Partner:', err);
    } finally {
      loading = false;
    }
  });
  </script>
  
  <MenuWrapper>
  <div class="reconnect-container">
    {#if loading}
      <p class="text-sm text-[#3a3b4b] text-center">Loading partner profile...</p>
    {:else if error}
      <p class="text-sm text-red-500 text-center">{error}</p>
    {:else if tp}
      <!-- Avatar & Name -->
      <div class="flex items-center justify-center gap-14 mt-4">
        <img
          src={`/${tp.name}.png`}
          alt={tp.name}
          class="w-20 h-20 rounded-full object-cover object-top"
        />
        <h2 class="text-lg font-bold text-[#141420]">{tp.name}</h2>
      </div>

      <!-- Bio -->
      <p class="text-sm mt-4 max-w-xs text-center text-[#3a3b4b]">{tp.avatar_blurb}</p>

      <!-- Divider -->
      <hr class="w-full max-w-xs border-t-2 border-[#3a3b4b] my-6" />

      <!-- Last focus -->
      <p class="text-sm max-w-xs text-center text-[#3a3b4b]">
        The last time you spoke with this thought partner you chose to focus on
        <span class="font-semibold">{tp.focusArea}</span> in the
        <span class="font-semibold">{tp.industry}</span>.
      </p>

      <p class="text-sm mt-2 text-center text-[#3a3b4b]">
        Before we connect you do you want to change either of these?
      </p>

      <!-- Buttons -->
      <div class="mt-6 flex flex-col gap-4 w-full max-w-xs">
        <button class="reconnect-btn" on:click={() => {
          goto(`/dialing?name=${encodeURIComponent(tp.name)}&image=${encodeURIComponent(`/${tp.name}.png`)}`);
        }}>
          No, connect me.
        </button>

        <button class="reconnect-btn" on:click={() => {
          goto(`/change-industry?name=${encodeURIComponent(tp.name)}`);
        }}>
          Yes, I want to change.
        </button>

      </div>
    {/if}
  </div>
</MenuWrapper>