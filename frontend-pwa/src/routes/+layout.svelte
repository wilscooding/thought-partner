<script lang="ts">
	import { currentUser } from '$lib/stores/userStore';
	import '../app.css';

	let { children } = $props();
</script>
{#if $currentUser}
	{@render children()}

{:else}
   <p> Loading...</p>

{/if}