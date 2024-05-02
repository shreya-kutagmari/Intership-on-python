from datetime import datetime

class TimelineItem:
    def __init__(self, start_date, end_date):
        self._start_date = start_date
        self._end_date = end_date

    def get_start_date(self):
        return self._start_date

    def get_end_date(self):
        return self._end_date

class Schedule(TimelineItem):
    def __init__(self, schedule_id, start_date, end_date):
        super().__init__(start_date, end_date)
        self._schedule_id = schedule_id

    def get_schedule_id(self):
        return self._schedule_id

    def update_schedule(self, new_start_date, new_end_date):
        self._start_date = new_start_date
        self._end_date = new_end_date

class ProjectTimeline:
    def __init__(self, project_name, end_date):
        self.project_name = project_name
        self.end_date = end_date
        self.schedules = []

    def add_schedule(self, schedule):
        self.schedules.append(schedule)

    def remove_schedule(self, schedule_id):
        self.schedules = [s for s in self.schedules if s.get_schedule_id() != schedule_id]

    def update_schedule(self, schedule_id, new_start_date, new_end_date):
        for schedule in self.schedules:
            if schedule.get_schedule_id() == schedule_id:
                schedule.update_schedule(new_start_date, new_end_date)
                break
        else:
            print("Schedule not found.")

class ProjectScheduler:
    def __init__(self):
        self.timelines = {}

    def create_timeline(self, project_name, end_date):
        if project_name not in self.timelines:
            current_date = self.get_current_date()
            if datetime.strptime(end_date, '%Y-%m-%d') < datetime.strptime(current_date, '%Y-%m-%d'):
                print("project is not ready")
                return
            self.timelines[project_name] = ProjectTimeline(project_name, end_date)
            print("timeline created")
        else:
            print("Timeline for this project already exists.")

    def adjust_schedule(self, project_name, schedule_id, new_start_date, new_end_date):
        if project_name in self.timelines:
            current_date = self.get_current_date()
            if datetime.strptime(new_end_date, '%Y-%m-%d') > datetime.strptime(self.timelines[project_name].end_date,
                                                                              '%Y-%m-%d'):
                print("end date extended")
                self.timelines[project_name].end_date = new_end_date
            self.timelines[project_name].update_schedule(schedule_id, new_start_date, new_end_date)
        else:
            print("Project timeline not found.")

    def delete_timeline(self, project_name):
        if project_name in self.timelines:
            del self.timelines[project_name]
        else:
            print("Project timeline not found.")

    def display_schedule(self, project_name):
        if project_name in self.timelines:
            for schedule in self.timelines[project_name].schedules:
                print(
                    f"Schedule ID: {schedule.get_schedule_id()}, Start Date: {schedule.get_start_date()}, End Date: {schedule.get_end_date()}")
        else:
            print("Project timeline not found.")

    def get_current_date(self):
        return "2024-04-29"

if __name__ == "__main__":
    # Create ProjectScheduler instance
    scheduler = ProjectScheduler()

    while True:
        print("\n1. Create Project Timeline\n2. Add Schedule\n3. Adjust Schedule\n4. Delete Project Timeline\n5. Display Schedule\n6. Update Schedule\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            project_name = input("Enter project name: ")
            end_date = input("enter end date(YYY-MM-DD):")
            scheduler.create_timeline(project_name, end_date)

        elif choice == "2":
            project_name = input("Enter project name: ")
            schedule_id = int(input("Enter schedule ID: "))
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            schedule = Schedule(schedule_id, start_date, end_date)
            scheduler.timelines[project_name].add_schedule(schedule)
            print("Schedule added.")

        elif choice == "3":
            project_name = input("Enter project name: ")
            schedule_id = int(input("Enter schedule ID: "))
            new_start_date = input("Enter new start date (YYYY-MM-DD): ")
            new_end_date = input("Enter new end date (YYYY-MM-DD): ")
            scheduler.adjust_schedule(project_name, schedule_id, new_start_date, new_end_date)
            print("Schedule adjusted.")

        elif choice == "4":
            project_name = input("Enter project name: ")
            scheduler.delete_timeline(project_name)
            print("Project timeline deleted.")

        elif choice == "5":
            project_name = input("Enter project name: ")
            scheduler.display_schedule(project_name)

        elif choice == "6":
            project_name = input("Enter project name: ")
            schedule_id = int(input("Enter schedule ID: "))
            new_start_date = input("Enter new start date (YYYY-MM-DD): ")
            new_end_date = input("Enter new end date (YYYY-MM-DD): ")
            scheduler.timelines[project_name].update_schedule(schedule_id, new_start_date, new_end_date)
            print("Schedule updated.")

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
