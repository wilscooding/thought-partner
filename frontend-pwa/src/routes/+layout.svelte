<script lang="ts">
	import { onMount } from 'svelte';
	import { currentUser } from '$lib/stores/userStore';
	import { userContacts } from '$lib/stores/userContacts';
	import { db } from '$lib/firebase';
	import { collection, getDocs } from 'firebase/firestore';

	import '../app.css';
	let { children } = $props();

	// onMount(async () => {
	// 	if ($currentUser) {
	// 		try {
	// 			const ref = collection(db, 'users', $currentUser.uid, 'thoughtPartners');
	// 			const snapshot = await getDocs(ref);
	// 			const contacts = snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
	// 			userContacts.set(contacts);
	// 			console.log('✅ Preloaded contacts:', contacts);
	// 		} catch (err) {
	// 			console.error('❌ Failed to preload contacts:', err);
	// 		}
	// 	}
	// });

	onMount(async () => {
	console.log('🏁 Layout mounted. Checking current user...');
	if ($currentUser) {
		console.log('👤 Current user:', $currentUser.uid);
		try {
			const ref = collection(db, 'users', $currentUser.uid, 'thoughtPartners');
			const snapshot = await getDocs(ref);
			const contacts = snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
			userContacts.set(contacts);
			console.log('✅ Preloaded contacts:', contacts);
		} catch (err) {
			console.error('❌ Failed to preload contacts:', err);
		}
	} else {
		console.log('⚠️ No user found when trying to preload.');
	}
});

</script>

{#if $currentUser}
	{@render children()}
{:else}
	<p>Loading...</p>
{/if}
