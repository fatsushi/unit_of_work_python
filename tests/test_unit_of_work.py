import pytest
from src.unit_of_work import unit_of_work

class dummy_customer:
  def __init__(self, name):
    self.name = name


def test_constructor():
  uow = unit_of_work()
  assert uow.new_objects == []
  assert uow.dirty_obuects == []
  assert uow.remove_objects == []


def test_register_new_assert():
  uow = unit_of_work()
  with pytest.raises(AssertionError) as e:
    uow.register_new(None)  
  assert str(e.value) == "registered new object is None"

  uow = unit_of_work()
  customer = dummy_customer("taro")
  uow.dirty_obuects.append(customer)
  with pytest.raises(AssertionError) as e:
    uow.register_new(customer)  
  assert str(e.value) == "registered new object is dirty"

  uow = unit_of_work()
  customer = dummy_customer("taro")
  uow.remove_objects.append(customer)
  with pytest.raises(AssertionError) as e:
    uow.register_new(customer)  
  assert str(e.value) == "registered new object is removed"

  uow = unit_of_work()
  customer = dummy_customer("taro")
  uow.new_objects.append(customer)
  with pytest.raises(AssertionError) as e:
    uow.register_new(customer)  
  assert str(e.value) == "registered new object is already exist"


def test_register_new():
  uow = unit_of_work()
  customer = dummy_customer("taro")
  uow.register_new(customer)
  assert len(uow.new_objects) == 1


def test_register_dirty_assert():
  uow = unit_of_work()
  with pytest.raises(AssertionError) as e:
    uow.register_dirty(None)  
  assert str(e.value) == "registered dirty object is None"

  uow = unit_of_work()
  customer = dummy_customer("taro")
  uow.remove_objects.append(customer)
  with pytest.raises(AssertionError) as e:
    uow.register_dirty(customer)  
  assert str(e.value) == "registered dirty object is removed"


def test_register_dirty():
  uow = unit_of_work()
  customer = dummy_customer("taro")
  uow.register_dirty(customer)
  assert len(uow.dirty_obuects) == 1


def test_register_remove_assert():
  uow = unit_of_work()
  with pytest.raises(AssertionError) as e:
    uow.register_remove(None)  
  assert str(e.value) == "registered remove object is None"


def test_register_remove():
  uow = unit_of_work()
  customer = dummy_customer("taro")
  uow.register_remove(customer)
  assert len(uow.remove_objects) == 1


def test_register_clean_assert():
  uow = unit_of_work()
  with pytest.raises(AssertionError) as e:
    uow.register_clean(None)  
  assert str(e.value) == "clean object is None"

