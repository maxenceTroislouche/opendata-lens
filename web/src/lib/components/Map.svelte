<script lang="ts">
	import { MapLibre, Marker, Popup } from 'svelte-maplibre';
	import { structureCommerceMarkers, structureEvenementMarkers, type Data } from '@/data';

	type Props = {
		data: Data;
	};

	const { data }: Props = $props();
	const commerceMarkers = $derived(structureCommerceMarkers(data));
	const evenementMarkers = $derived(structureEvenementMarkers(data));

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
	{#each commerceMarkers as marker}
		<Marker
			lngLat={marker.lngLat}
			class="grid h-8 w-8 place-items-center rounded-full border border-gray-200 bg-red-300 text-black shadow-2xl focus:outline-2 focus:outline-black"
		>
			<span>
				{marker.label}
			</span>

			<Popup openOn="hover" offset={[0, -10]}>
				<div class="text-sm">{marker.name}</div>
			</Popup>
		</Marker>
	{/each}
</MapLibre>
