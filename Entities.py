class Apartment():
    def __init__(self, id : str, location_id : str, room_type : str, monthly_rent : str, bedrooms : str, bathrooms: str,occupancy_status : bool):
        self.apartment_id = id
        self.location_id = location_id
        self.room_type = room_type
        self.monthly_rent = monthly_rent
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.occupancy_status = occupancy_status


class Location():
    def __init__(self, location_id : str, location_name : str, location_manager : str):
        self.location_id = location_id
        self.location_name = location_name
        self.location_manager = location_manager
    

class Complaint():
    def __init__(self, complaint_id, tenant_id, tenant_message, created_at, resolved_at):
        self.complaint_id = complaint_id
        self.tenant_id = tenant_id
        self.tenant_message = tenant_message
        self.creationDate = created_at
        self.resolveDate = resolved_at

class Contract():
    def __init__(self,contract_id, apartment_id, tenant_id, start_date, end_date, payment_frequency, early_leave, penalty_amount):
        self.contract_id = contract_id
        self.apartment_id = apartment_id
        self.tenant_id = tenant_id
        self.start_date = start_date
        self.end_date = end_date
        self.payment_frequency = payment_frequency
        self.early_leave = early_leave
        self.penalty_amount = penalty_amount

class Invoices():
    def __init__(self, invoice_id, contract_id, schedule_id, issued_date, due_date, amount, status):
        self.invoice_id = invoice_id
        self.contract_id = contract_id
        self.schedule_id = schedule_id
        self.issued_date = issued_date
        self.due_date = due_date
        self.amount = amount
        self.status = status

class MaintenanceRequest():
    def __init__(self,request_id, tenant_id, apartment_id, description, priority, status, maintenance_notes, scheduled_date, resolved_date, time_taken, cost):
        self.request_id = request_id
        self.tenant_id = tenant_id
        self.apartment_id = apartment_id
        self.description = description
        self.priority = priority
        self.status = status
        self.maintenance_notes = maintenance_notes
        self.scheduled_date = scheduled_date
        self.resolved_date = resolved_date
        self.time_taken = time_taken
        self.cost = cost

class MaintanenceSchedule():
    def __init__(self,schedule_id, request_id, user_id, scheduled_start, scheduled_end):
        self.schedule_id = schedule_id
        self.request_id = request_id
        self.user_id = user_id
        self.scheduled_start = scheduled_start
        self.scheduled_end = scheduled_end

class Notification():
    def __init__(self,notification_id, tenant_id, type, message, is_read, created_at):
        self.notification_id = notification_id
        self.tenant_id = tenant_id
        self.type = type
        self.message = message
        self.is_read = is_read
        self.created_at = created_at

class Payment():
    def __init__(self,payment_id, schedule_id, payment_date, amount_paid, payment_status, method, reference):
        self.payment_id = payment_id
        self.schedule_id = schedule_id
        self.payment_date = payment_date
        self.amount_paid = amount_paid
        self.payment_status = payment_status
        self.method = method
        self.reference = reference

class Tenant():
    def __init__(self,tenant_id, first_name, last_name, national_insurance, email, password, phone_number, occupation, references ):
        self.tenant_id = tenant_id
        self.first_name = first_name
        self.last_name = last_name
        self.national_insurance = national_insurance
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.occupation = occupation
        self.references = references

class User():
    def __init__(self, user_id, firstName, lastName, email, password, role, location_id):
        self.user_id = user_id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.role = role
        self.location_id = location_id


