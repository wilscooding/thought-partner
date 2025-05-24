<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
    import { page } from '$app/stores';
    import { onMount } from 'svelte';

    let tp = null;
    let error = null;
    let industry = "";
    let guidance = "";

    const userOptions = {
        industry: [
            "Construction", "Education Services", "Entertainment", "Finance & Insurance",
            "Healthcare & Social Assistance", "Hospitality & Food Services", "Manufacturing",
            "Professional & Business Services", "Real Estate", "Retail & E-commerce", "Transportation & Logistics"
        ],
        guidance: [
            "Customer Experience", "Finance", "Marketing & Sales", "Operations", "People & Culture",
            "Product & Innovation", "Risk & Compliance", "Strategy & Vision", "Sustainability & Social Impact", "Technology & Data"
        ]
    };

    $: name = $page.params.name;

    onMount(async () => {
        try {
            const response = await fetch(`http://localhost:8000/api/tp-profiles/${name}`);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            tp = await response.json();
        } catch (err) {
            error = err.message;
        }
    });

    const connect = () => {
        console.log(`Connecting with ${tp.name}, industry: ${industry}, guidance: ${guidance}`);
        // Here you can navigate or trigger the backend connection
    };

    const changeThoughtPartner = () => {
        window.location.href = '/tp-profiles';
    };
</script>

<MenuWrapper>
    {#if error}
        <p class="text-center text-red-600 p-6">{error}</p>
    {:else if tp}
        <div class="tp-connect-container">
            <h2 class="tp-connect-title">Before We Connect You</h2>
            <hr class="tp-divider" />
            <p class="tp-context"><strong>{tp.name}</strong> is one of your contacts!</p>
            <p class="tp-last">
                The last time you spoke with this thought partner you chose to focus on 
                <a href="#" class="tp-link">Operations</a> in the <a href="#" class="tp-link">Construction industry</a>.
            </p>
            <p class="tp-prompt">Make the selections below so that {tp.name} knows what you want to partner on today.</p>
            <hr class="tp-divider" />

            <label class="tp-label">What industry are you working in or thinking about today?</label>
            <select bind:value={industry} class="tp-select">
                <option disabled selected value="">Select an industry</option>
                {#each userOptions.industry as option}
                    <option>{option}</option>
                {/each}
            </select>

            <label class="tp-label">What kind of guidance are you looking for today?</label>
            <select bind:value={guidance} class="tp-select">
                <option disabled selected value="">Select guidance</option>
                {#each userOptions.guidance as option}
                    <option>{option}</option>
                {/each}
            </select>

            <button class="tp-connect-button" on:click={handleConnect}>Connect Me</button>
            <button class="tp-change-button" on:click={() => goto('/tp-profiles')}>Change Thought Partner</button>
        </div>
    {:else}
        <p class="text-center p-6">Loading...</p>
    {/if}
</MenuWrapper>
