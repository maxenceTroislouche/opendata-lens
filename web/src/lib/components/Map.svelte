<script lang="ts">
	import { MapLibre } from 'svelte-maplibre';

	const defaultLattitude = 50.432649;
	const defaultLongitude = 2.81951;
</script>

<MapLibre
	center={[defaultLongitude, defaultLattitude]}
	zoom={15}
	standardControls
	style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json"
	class="relative aspect-[9/16] max-h-[70vh] w-full sm:aspect-video sm:max-h-full"
/>
