class unit_of_work:
  def __init__(self):
    self.new_objects = []
    self.dirty_obuects = []
    self.remove_objects = []

  def register_new(self, obj):
    assert obj != None, "registered new object is None"
    assert obj not in self.dirty_obuects, "registered new object is dirty"
    assert obj not in self.remove_objects, "registered new object is removed"
    assert obj not in self.new_objects, "registered new object is already exist"

    self.new_objects.append(obj)


  def register_dirty(self, obj):
    assert obj != None, "registered dirty object is None"
    assert obj not in self.remove_objects, "registered dirty object is removed"

    if obj not in self.dirty_obuects and obj not in self.new_objects:
      self.dirty_obuects.append(obj)


  def register_remove(self, obj):
    assert obj != None, "registered remove object is None"
    if obj in self.new_objects: 
      self.new_objects.remove(obj)
      return
    if obj in self.dirty_obuects:
      self.dirty_obuects.remove(obj)    
    self.remove_objects.append(obj)


  def register_clean(self, obj):
    assert obj != None, "clean object is None"

  
  def commit(self):
    None
    # repository.commit(self)
    # class repository::commit
    # @transaction.atomic
    # def commit(uow: unit_of_work):
    #   store_new(uow.new_objects)
    #   store_update(uow.dirty_objects)
    #   store_delete(uow.remove_objects)

