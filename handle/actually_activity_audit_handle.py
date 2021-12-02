import page



class ActuallyActivityAuditHandle(page.ActuallyActivityAuditPage):

    def tap_activity_audit_pass(self):
        self.execute_tap(self.get_activity_audit_pass_ele())

    def tap_activity_audit_fail(self):
        self.execute_tap(self.get_activity_audit_fail_ele())

    def input_activity_audit_fail_reason(self, fail_reason):
        self.execute_input(self.get_activity_audit_fail_reason_ele(), fail_reason)

    def tap_activity_audit_fail_confirm(self):
        self.execute_tap(self.get_activity_audit_fail_confirm_ele())

    def tap_activity_audit_reject(self):
        self.execute_tap(self.get_activity_audit_reject_ele())

    def input_activity_audit_reject_reason(self, reject_reason):
        self.execute_input(self.get_activity_audit_reject_reason_ele(), reject_reason)

    def tap_activity_audit_reject_confirm(self):
        self.execute_tap(self.get_activity_audit_reject_confirm_ele())