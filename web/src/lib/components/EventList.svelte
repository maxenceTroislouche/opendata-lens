<script lang="ts">
	import { structureEventsData, type Data } from '@/data';

	type Props = {
		data: Data;
	};

	const { data }: Props = $props();

    const eventsList = $derived(structureEventsData(data));
</script>

<div class="p-6">
    <h1 class="text-2xl font-bold text-center mb-8">Événements à venir</h1>
    
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {#each eventsList as evenement}
            <div class="bg-white shadow-md rounded-lg overflow-hidden">
                <img 
                    src={evenement.image} 
                    alt={evenement.nom} 
                    class="w-full h-48 object-cover"
                />
                <div class="p-4">
                    <h2 class="text-xl font-bold mb-2">{evenement.nom}</h2>
                    <p class="text-gray-700 mb-2"><strong>Type :</strong> {evenement.type}</p>
                    <p class="text-gray-700 mb-2"><strong>Date :</strong> {evenement.date} à {evenement.heure}</p>
                    <p class="text-gray-700 mb-2"><strong>Adresse :</strong> {evenement.adresse}</p>
                    <!-- <p class="text-gray-600 text-sm">{evenement.description}</p> -->
                </div>
            </div>
        {/each}
    </div>
</div>