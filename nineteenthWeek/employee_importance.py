class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = {employee.id: employee for employee in employees}
        def helper(employee_id: int) -> int:
            employee = employee_dict[employee_id]
            return employee.importance + sum(helper(sub) for sub in employee.subordinates)
        return helper(id)