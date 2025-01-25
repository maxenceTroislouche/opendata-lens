export const commerceTypes = [
	'employment_agency',
	'laundry',
	'caterer',
	'clothes',
	'cafe',
	'post_office',
	'restaurant',
	'educational_institution',
	'doityourself',
	'shoemaker',
	'florist',
	'pharmacy',
	'bakery',
	'fast_food',
	'supermarket',
	'beauty',
	'fuel',
	'insurance',
	'variety_store',
	'pub',
	'bank',
	'pastry',
	'tool_hire',
	'car_rental',
	'car_repair',
	'ticket',
	'optician',
	'convenience',
	'bar',
	'party',
	'tobacco',
	'alcohol',
	'gift',
	'cosmetics',
	'jewelry',
	'plumber',
	'books',
	'bed',
	'estate_agent',
	'hairdresser',
	'perfumery',
	'cheese',
	'chocolate',
	'car_wash',
	'locksmith',
	'motorcycle',
	'bicycle',
	'brewery',
	'car',
	'hearing_aids',
	'cleaning',
	'window_blind',
	'bathroom_furnishing',
	'mobile_phone'
] as const;

export const eventTypes = ['SPECTACLE', 'MATCH'] as const;

export type Data = {
	commerce: {
		nom: string;
		description: string;
		adresse: string;
		mail: string;
		type: (typeof commerceTypes)[number];
		longitude: number;
		latitude: number;
	}[];
	evenement: {
		date: string;
		heure: string;
		duree: number;
		nom: string;
		type: (typeof eventTypes)[number];
		description: string;
		adresse: string;
		longitude: number;
		latitude: number;
		image: string;
	}[];
};

export function structureCommerceMarkers(commerces: Data['commerce']): {
	lngLat: [number, number];
	label: string;
	name: string;
}[] {
	return commerces.map((commerce) => ({
		lngLat: [commerce.longitude, commerce.latitude],
		label: commerce.nom,
		name: commerce.nom
	}));
}

export function getCommerceBgColor(type: Data['commerce'][0]['type']): string {
	// Programmatic color generation based on the type of commerce
	// Return HSL color but rotate the hue based on the type
	const hue = commerceTypes.indexOf(type) * (360 / commerceTypes.length);
	return `hsl(${hue}, 60%, 70%)`;
}
