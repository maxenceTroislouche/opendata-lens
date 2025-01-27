<script lang="ts">
    import { onMount } from 'svelte';
	import type { Data } from '@/data';
	import EventList from '@/components/EventList.svelte';
	import { base } from '$app/paths';

	let data = $state<Data>();

	onMount(async () => {
		let response = await fetch('/data.json');
		data = await response.json();
	});
</script>

<a
    href="{base}/"
    class="inline-block rounded-lg bg-blue-500 m-4 px-6 py-3 text-center font-bold text-white shadow hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-300"
>
    Retour au menu
</a>

{#if data}
<EventList {data} />
{:else}
<p>Chargement ...</p>
{/if}
