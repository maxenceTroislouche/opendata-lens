db = db.getSiblingDB("opendatalens");

// Création des collections
db.createCollection("evenement");
db.createCollection("commerce");
db.createCollection("transport");

// Insertion de documents de base
// TODO: Retirer les documents suivants
db.evenement.insertMany([
  { name: "Festival de musique", date: "2025-07-20", location: "Lens" },
  { name: "Exposition d'art", date: "2025-08-15", location: "Lens" }
]);

db.commerce.insertMany([
  { name: "Boulangerie Lensoise", type: "Alimentation", revenue: 45000 },
  { name: "Supermarché Lens Centre", type: "Distribution", revenue: 125000 }
]);

db.transport.insertMany([
  { type: "Bus", route: "Lens - Liévin", frequency: "30min" },
  { type: "Train", route: "Lens - Lille", frequency: "1h" }
]);
