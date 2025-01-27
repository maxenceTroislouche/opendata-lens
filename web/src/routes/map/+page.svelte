<script lang="ts">
	import { onMount } from 'svelte';
	import Map from '@/components/Map.svelte';
	import { type Data } from '@/data';
	import { Slider } from '@/components/ui/slider';
	import { base } from '$app/paths';

	let data = $state<Data>();
	let selectedEventIndex = $state<string>('');
	let distance = $state<number>(100);
	let filteredCommerces = $derived(filterCommerces(data, selectedEventIndex, distance));

	onMount(async () => {
		let response = await fetch(`${base}/data.json`);
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
	<div class="flex h-screen">
		<div class="flex h-screen w-72 flex-col gap-4">
			<div class="mt-2 px-4 space-y-2">
				<h2>Distance</h2>
				<Slider type="single" bind:value={distance} max={100} step={1} />
			</div>

			<div class="grow overflow-auto">
				<h2 class="px-4">Evenements</h2>

				<div class="overflow-auto px-4">
					{#each data.evenement as event, i}
						<button
							onclick={() => (selectedEventIndex = `${i}`)}
							data-selected={selectedEventIndex === `${i}`}
							class="w-full border-b rounded-md text-left p-2 data-[selected=true]:bg-gray-100 overflow-hidden"
						>
							<p>{event.nom}</p>
							<p class="text-nowrap text-ellipsis">{event.description}</p>
							<p>{event.duree}</p>
							<p>{event.date} à {event.heure}</p>
							<p>{event.adresse}</p>
						</button>
					{/each}
				</div>
			</div>
		</div>

		<Map
			commerces={filteredCommerces}
			selectedEvent={data.evenement[Number.parseInt(selectedEventIndex)]}
			{distance}
		/>
	</div>
{:else}
	<p>Chargement...</p>
{/if}
