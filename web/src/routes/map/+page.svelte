<script lang="ts">
	import { onMount } from 'svelte';
	import Map from '@/components/Map.svelte';
	import type { Data } from '@/data';

	let data = $state<Data>();

	onMount(async () => {
		let response = await fetch('/data.json');
		data = await response.json();
	});
</script>

{#if data}
	<Map {data} />
{:else}
	<p>Chargement...</p>
{/if}
