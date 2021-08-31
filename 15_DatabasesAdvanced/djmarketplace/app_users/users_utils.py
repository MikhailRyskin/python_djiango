def find_status(balance):
    if balance < 100:
        status = 'обычный'
    elif balance < 500:
        status = 'серебряный'
    else:
        status = 'золотой'
    return status


def increase_balance(profile, add_to_balance):
    profile.balance += add_to_balance
    new_status = find_status(profile.balance)
    profile.status = new_status
    profile.save()
