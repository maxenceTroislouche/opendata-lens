<script lang="ts">
	import { DefaultMarker, MapLibre, Marker, Popup } from 'svelte-maplibre';
	import { getCommerceBgColor, structureCommerceMarkers, type Data } from '@/data';

	type Props = {
		commerces: Data['commerce'];
		selectedEvent: Data['evenement'][number] | null;
		distance: number;
	};

	const { commerces, selectedEvent }: Props = $props();
	const commerceMarkers = $derived(structureCommerceMarkers(commerces));

	const defaultLattitude = 50.432649;
	const defaultLongitude = 2.81951;
</script>

<MapLibre
	center={[defaultLongitude, defaultLattitude]}
	zoom={15}
	standardControls
	style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json"
	class="relative aspect-[9/16] max-h-[70vh] w-full sm:aspect-video sm:max-h-full"
>
	{#if selectedEvent}
		<DefaultMarker lngLat={[selectedEvent.longitude, selectedEvent.latitude]}>
			<Popup offset={[0, -10]}>
				<div class="text-lg font-bold">{selectedEvent.nom}</div>
			</Popup>
		</DefaultMarker>
	{/if}

	{#each commerceMarkers as marker, i}
		<Marker lngLat={marker.lngLat}>
			<div
				class="grid size-8 place-items-center rounded-full border border-gray-200 text-black shadow-2xl focus:outline-2 focus:outline-black"
				style="background-color: {getCommerceBgColor(commerces[i].type)}"
			>
				<span>
					{marker.label.slice(0, 3).toUpperCase()}
				</span>

				<Popup openOn="hover" offset={[0, -10]}>
					<div class="text-sm">{marker.name}</div>
				</Popup>
			</div>
		</Marker>
	{/each}
</MapLibre>
