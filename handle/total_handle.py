import handle


#统一动作类入口

class TotalHandle:

    def __init__(self, driver):
        self.driver = driver

    def init_login(self):
        return handle.PageHandle(self.driver)

    def init_home(self):
        return handle.HomeHandle(self.driver)

    def init_volunteer_team(self):
        return handle.VolunteerTeamHandle(self.driver)

    def init_add_team(self):
        return handle.AddTeamHandle(self.driver)

    def init_check_activity(self):
        return handle.ActivityCheckHandle(self.driver)

    def init_actually_activity(self):
        return handle.ActuallyActivityAuditHandle(self.driver)

    def init_volunteer_project(self):
        return handle.VolunteerProjectHandle(self.driver)

    def init_create_activity(self):
        return handle.CreateActivityHandle(self.driver)

    def init_home_team_list(self):
        return handle.HomeTeamListHandle(self.driver)

    def init_home_team_details(self):
        return handle.HomeTeamDetailsHandle(self.driver)