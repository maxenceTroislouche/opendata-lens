<script lang="ts">
	let L: typeof import('leaflet');
	let map: L.Map;

	async function importLeaflet() {
		L = await import('leaflet');
	}

	async function initMap(element: HTMLElement) {
		await importLeaflet();

		map = L.map(element).setView([51.505, -0.09], 13);

		L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
			attribution:
				'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
		}).addTo(map);

		// L.marker([51.5, -0.09])
		// 	.addTo(map)
		// 	.bindPopup('A pretty CSS popup.<br> Easily customizable.')
		// 	.openPopup();
	}

	function mapAction(element: HTMLElement) {
		$effect(() => {
			initMap(element);

			return () => {
				map.remove();
			};
		});
	}
</script>

<!-- Map -->
<div use:mapAction class="size-full"></div>
