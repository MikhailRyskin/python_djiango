SILVER = 500
GOLD = 1000


def change_status(amount_purchases):
    if amount_purchases < SILVER:
        status = 'обычный'
    elif amount_purchases < GOLD:
        status = 'серебряный'
    else:
        status = 'золотой'
    return status


