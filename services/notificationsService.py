from repositories.notification_repository import NotificationRepository
from database.db_connection import DatabaseConnection

class NotificationService:

    def __init__(self, tenant_id, location_id):
        self.tenant_id = tenant_id
        self.location_id = location_id
        self.last_notification_id = 0
        db_connection = DatabaseConnection()
        self.notification_repo = NotificationRepository(db_connection)

    def get_notifications(self, personal, public):

        tenant = self.tenant_id if personal else None
        location = self.location_id if public else None

        notifications = self.notification_repo.fetch_notifications(tenant, location)

        return notifications

    def mark_as_read(self, notification_id):
        self.notification_repo.mark_as_read(notification_id)