import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові','дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check sructure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'

@pytest.mark.database
def test_find_address_by_id():
    db = Database()
    user = db.get_address_by_id(3)

    print(user)

@pytest.mark.database
def test__can_not_set_str_in_quantity():
    db = Database()
    db.set_str_in_quantity_field(1, "333")
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] != "333"

@pytest.mark.database
def test_customer_insert():
    db = Database()
    db.insert_customer(3, 'Alina', 'Holosiivska 13', 'Kyiv', 23451, 'Ukraine')
    check_address = db.get_address_by_id(3)

    assert check_address[0][0] == 'Holosiivska 13'

@pytest.mark.database
def test_customer_delete():
    db = Database()
    db.insert_customer(4, 'Nazarii', 'Antonovicha 67', 'Kyiv', 4332, 'Ukraine')
    all_users = db.get_all_users()
    assert all_users [3][0] == "Nazarii"
    db.delete_customer_by_name("Nazarii")
    assert all_users [3][0] == "Nazarii"

@pytest.mark.database
def test_customer_delete():
    db = Database()
    db.insert_customer(4, 'Nazarii', 'Antonovicha 67', 'Kyiv', 4332, 'Ukraine')
    all_users = db.get_all_users()
    assert all_users[3][0] == "Nazarii"
    db.delete_customer_by_name("Nazarii")
    all_users_after_deletion = db.get_all_users()
    assert "Nazarii" not in [user[0] for user in all_users_after_deletion]

@pytest.mark.database
def test_product_qnt_update_negative():
    db = Database()
    db.update_product_qnt_by_id(1, 922337203685477580806456456)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] != 922337203685477580806456456