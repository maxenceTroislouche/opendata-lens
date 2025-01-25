export type Data = {
	commerce: {
		nom: string;
		description: string;
		adresse: string;
		mail: string;
		type: string;
		longitude: number;
		latitude: number;
	}[];
	evenement: {
		date: string;
		heure: string;
		duree: number;
		nom: string;
		type: string;
		description: string;
		adresse: string;
		longitude: number;
		latitude: number;
		image: string;
	}[];
};

export function structureCommerceMarkers(data: Data): {
	lngLat: [number, number];
	label: string;
	name: string;
}[] {
	return data.commerce.map((commerce) => ({
		lngLat: [commerce.longitude, commerce.latitude],
		label: commerce.nom,
		name: commerce.nom
	}));
}

export function structureEvenementMarkers(data: Data): {
	lngLat: [number, number];
	label: string;
	name: string;
}[] {
	return data.evenement.map((evenement) => ({
		lngLat: [evenement.longitude, evenement.latitude],
		label: evenement.nom,
		name: evenement.nom
	}));
}
