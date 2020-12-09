def sync(schedule_list):
    """This function returns the union of a set of schedules."""
    sync_schedule = set()
    for schedule in schedule_list:
        sync_schedule = sync_schedule | schedule
    return sync_schedule

schedules = [{'1234', '2345', '3456'}, {'4567', '5678', '6789'}, {'7890', '890'}]
union = sync(schedules)
print(union)
