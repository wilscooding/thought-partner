<script>
  import { onMount } from 'svelte';
  import { db } from '$lib/firebase';
  import { collection, getDocs } from 'firebase/firestore';
  import { currentUser } from '$lib/stores/userStore';
  import MenuWrapper from '$lib/components/MenuWrapper.svelte';
  import { goto } from '$app/navigation';

  let contacts = [];
  let error = null;

  onMount(async () => {
    if ($currentUser?.uid) {
      try {
        const thoughtPartnersRef = collection(db, 'users', $currentUser.uid, 'thoughtPartners');
        const querySnapshot = await getDocs(thoughtPartnersRef);
        contacts = querySnapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
      } catch (err) {
        error = err.message;
        console.error('Failed to load contacts:', err);
      }
    }
  });

  const goToMatch = () => goto('/match');

  const navigateToProfile = (name) => {
    const slug = name.toLowerCase().replace(/\s+/g, '-');
    goto(`/tp-profiles/${slug}`);
  };
</script>

<MenuWrapper>
  <div class="tp-container">
    <h2 class="tp-title">My Thought Partner Contacts</h2>

    {#if contacts.length > 0}
      <div class="tp-grid">
        {#each contacts as tp}
          <div
            class="tp-card"
            on:click={() => navigateToProfile(tp.name)}
            style="cursor: pointer;"
          >
            <img src={`/${tp.name}.png`} alt={tp.name} class="tp-avatar" />
            <span class="tp-name">{tp.name}</span>
          </div>
        {/each}
      </div>
    {:else}
      <p>You haven't connected to any Thought Partners yet.</p>
    {/if}

    <button class="tp-connect-button" on:click={goToMatch}>
      Find New Partner
    </button>
  </div>
</MenuWrapper>
