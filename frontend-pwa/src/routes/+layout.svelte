<!-- <script lang="ts">
	import { currentUser, userLoaded } from '$lib/stores/userStore';
	import { userContacts } from '$lib/stores/userContacts';
	import { db } from '$lib/firebase';
	import { collection, getDocs } from 'firebase/firestore';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { get } from 'svelte/store';
	import { onMount } from 'svelte';

	import '../app.css';

	// Define routes that don’t require auth
	const publicRoutes = ['/login', '/create-account', '/create-account/intro'];

	
	// Wait for mount, then handle redirect logic
	onMount(() => {
		const unsubscribe = page.subscribe(($page) => {
			const isPublic = publicRoutes.includes($page.url.pathname);
			const loaded = get(userLoaded);
			const user = get(currentUser);

			if (loaded && !user && !isPublic) {
				console.log('🔁 Redirecting to login page...');
				goto('/login');
			}
		});

		return () => unsubscribe();
	});

	// Preload contacts once user is available
	$: if ($userLoaded && $currentUser) {
		console.log('🏁 Preloading contacts for:', $currentUser.uid);
		(async () => {
			try {
				const ref = collection(db, 'users', $currentUser.uid, 'thoughtPartners');
				const snapshot = await getDocs(ref);
				const contacts = snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
				userContacts.set(contacts);
				console.log('✅ Contacts loaded:', contacts);
			} catch (e) {
				console.error('❌ Failed to load contacts:', e);
			}
		})();
	}
</script> -->

<!-- Layout rendering -->
<!-- {#if !$userLoaded}
	<p>Loading user data...</p>
{:else if $currentUser || publicRoutes.includes($page.url.pathname)}
	<slot />
{/if} -->

<svelte:head>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="manifest" href="/manifest.json" />
  <meta name="theme-color" content="#0f172a" />
</svelte:head>


<script lang="ts">
    import { currentUser, userLoaded } from '$lib/stores/userStore';
    import { userContacts } from '$lib/stores/userContacts';
    import { db } from '$lib/firebase';
    import { collection, getDocs } from 'firebase/firestore';
    import { goto } from '$app/navigation';
    import { page } from '$app/stores';

	import '../app.css';

    const publicRoutes = ['/login', '/create-account', '/create-account/intro'];

    $: if ($userLoaded && !$currentUser && !publicRoutes.includes($page.url.pathname)) {
        console.log('🛑 No user — redirecting from layout...');
        goto('/login');
    }

    $: if ($userLoaded && $currentUser) {
        console.log('🏁 Preloading contacts for:', $currentUser.uid);
        (async () => {
            try {
                const ref = collection(db, 'users', $currentUser.uid, 'thoughtPartners');
                const snapshot = await getDocs(ref);
                const contacts = snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
                userContacts.set(contacts);
                console.log('✅ Contacts loaded:', contacts);
            } catch (e) {
                console.error('❌ Failed to load contacts:', e);
            }
        })();
    }
</script>

{#if !$userLoaded}
    <p>Loading user data...</p>
{:else if $currentUser || publicRoutes.includes($page.url.pathname)}
    <slot />
{/if}

