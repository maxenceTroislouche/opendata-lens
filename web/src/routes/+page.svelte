<script lang="ts">
	import { onMount } from 'svelte';
	import Map from '@/components/Map.svelte';
	import { type Data } from '@/data';
	import { Select, SelectTrigger, SelectContent, SelectItem } from '@/components/ui/select';
	import { Slider } from '@/components/ui/slider';

	let data = $state<Data>();
	let selectedEventIndex = $state<string>('');
	let distance = $state<number>(100);
	let filteredCommerces = $derived(filterCommerces(data, selectedEventIndex, distance));

	onMount(async () => {
		let response = await fetch('/data.json');
		data = await response.json();
	});

	function filterCommerces(data: Data | undefined, selectedEvent: string, distance: number) {
		if (!data || selectedEvent === '') {
			return [];
		}

		// Only keep commerces that are in the distance from the selected event
		const [longitude, lattitude] = [
			data.evenement[Number.parseInt(selectedEvent)].longitude,
			data.evenement[Number.parseInt(selectedEvent)].latitude
		];
		// The distance is in meter
		const filteredCommerces = data.commerce.filter((commerce) => {
			const distanceFromEvent = Math.sqrt(
				Math.pow(commerce.longitude - longitude, 2) + Math.pow(commerce.latitude - lattitude, 2)
			);
			return distanceFromEvent <= distance / 1000;
		});
		return filteredCommerces;
	}
</script>

{#if data}
	<div>
		<header class="flex items-center justify-between p-4">
			<Select type="single" bind:value={selectedEventIndex}>
				<SelectTrigger class="w-[180px]">
					{data.evenement[Number.parseInt(selectedEventIndex)]?.nom}
				</SelectTrigger>
				<SelectContent>
					{#each data.evenement as event, i}
						<SelectItem value={`${i}`}>{event.nom}</SelectItem>
					{/each}
				</SelectContent>
			</Select>

			<Slider type="single" bind:value={distance} max={100} step={1} />
		</header>

		<Map
			commerces={filteredCommerces}
			selectedEvent={data.evenement[Number.parseInt(selectedEventIndex)]}
			{distance}
		/>
	</div>
{:else}
	<p>Chargement...</p>
{/if}
