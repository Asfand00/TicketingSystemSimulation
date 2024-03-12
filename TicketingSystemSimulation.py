import queue
import threading
import time
import random

class Ticket:
    def __init__(self, ticket_number, timestamp):
        self.ticket_number = ticket_number
        self.timestamp = timestamp

def generate_ticket(queue, ticket_limit):
    ticket_number = 1
    while ticket_number <= ticket_limit:
        ticket = Ticket(ticket_number, time.time())
        queue.put(ticket)
        print(f"Ticket {ticket.ticket_number} issued at {time.strftime('%H:%M:%S', time.localtime(ticket.timestamp))}")
        ticket_number += 1
        time.sleep(random.randint(1, 5))  # Random interval for generating tickets

def process_tickets(queue, ticket_limit):
    tickets_processed = 0
    while tickets_processed < ticket_limit:
        if not queue.empty():
            ticket = queue.get()
            print(f"Ticket {ticket.ticket_number} is being processed...")
            tickets_processed += 1
            time.sleep(random.randint(1, 3))  # Simulate processing time
        else:
            print("No tickets to process at the moment...")
            time.sleep(1)  # Wait for some time before checking again

if __name__ == "__main__":
    
    # Ticket limit to stop queue when the limit is reached and initialize queue
    ticket_limit = 10 
    ticket_queue = queue.Queue()

    # Start generating tickets in a separate thread
    ticket_generator_thread = threading.Thread(target=generate_ticket, args=(ticket_queue, ticket_limit), daemon=True)
    ticket_generator_thread.start()

    # Process tickets in the main thread
    process_tickets(ticket_queue, ticket_limit)
