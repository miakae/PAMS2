# from models.domain_models import *
# location = Location(1, "Location 1", "Manager 1")
# apartment = Apartment(1, location, "Studio", 1200.0, 1, 1, True)
# tenant = Tenant(1, "John", "Doe", "test@gmail.com")
# contract = Contract(1, apartment, tenant, "2026-01-01", "2026-12-31", "Monthly", False, 0.0)
# tenant.contracts.append(contract)
# print(tenant.get_location())

from models import domain_models
from services.maintenanceService import MaintenanceService
from PySide6.QtWidgets import QApplication
from components.frontDeskPage import FrontDeskPendingMaintenance
from components.frontDeskPage import FrontDeskScheduledMaintenance

current_location = domain_models.Location(location_id=1, name="Main Building", manager=None)
current_user = domain_models.User(user_id=1, first_name="Max", last_name = "Jones", email="max.jones@example.com", location = current_location, role="FrontDesk")
maintenance_service = MaintenanceService()
# print(maintenance_service.get_pending_requests(current_user))
# print(maintenance_service.get_available_workers("2026-04-01 09:00:00", "2026-04-01 17:00:00", current_user))
# maintenance_service.assign_worker_to_request(request_id=2, worker_id=5, start="2026-04-01 09:00:00", end="2026-04-01 17:00:00")
# print(maintenance_service.get_available_workers("2026-04-01 09:00:00", "2026-04-01 17:00:00", current_user))
# print(maintenance_service.get_request_details(2))
app = QApplication()
mainWindow =FrontDeskScheduledMaintenance(maintenance_service)
mainWindow.show()
app.exec()

