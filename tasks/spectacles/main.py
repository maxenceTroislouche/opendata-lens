from database import MongoDatabase
from api import RCLEventGetter, TicketMasterEventGetter

def main():
    print("Début tâche spectacles ...")

    events = []

    ticket_master_event_getter = TicketMasterEventGetter()
    rcl_event_getter = RCLEventGetter()

    events.extend(ticket_master_event_getter.run())
    events.extend(rcl_event_getter.run())

    db = MongoDatabase()
    db.insert_events(events)
    db.close()

    print("Fin tâche spectacles")


if __name__ == "__main__":
    main()
