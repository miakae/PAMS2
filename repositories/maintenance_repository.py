from .base_repository import BaseRepository


class MaintenanceRepository(BaseRepository):

    def get_by_apartment(self, apartment_id: int):
        query = "SELECT * FROM maintenance_requests WHERE apartment_id = %s"
        return self.fetch_all(query, (apartment_id,))