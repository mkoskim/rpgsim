################################################################################
#
#
#
################################################################################

#-------------------------------------------------------------------------------
#
#
#
#-------------------------------------------------------------------------------

class Item(object):

    def __init__(self, ID): self.ID = ID

    def __repr__(self): return str(self.ID)

    def __mul__(self, count):  return Item.Stack(self, count)
    def __rmul__(self, count): return Item.Stack(self, count)

    def __add__(self, item):   return Item.Bag(self, item)
    def __radd__(self, item):  return Item.Bag(self, item)

    #---------------------------------------------------------------------------
    # Item.Stack: stack of items
    #---------------------------------------------------------------------------
    
    class Stack(object):

        def __init__(self, item, count = 1):
            self.ID = isinstance(item, Item) and item.ID or item
            self.count = count

        def __repr__(self): return "%s x %d" % (self.ID, self.count)

        def __add__(self, item):  return Item.Bag(self, item)
        def __radd__(self, item): return Item.Bag(self, item)
        
    #---------------------------------------------------------------------------
    # Bag: bag of stacks of items
    #---------------------------------------------------------------------------

    class Bag(object):

        def __init__(self, *items):
            self.items = { }
            self.add(*items)

        def __repr__(self): return str(self.items)
    
        def add(self, *items):

            def additem(item, count = 1):
                if isinstance(item, Item):
                    ID = item.ID
                elif isinstance(item, Item.Stack):
                    ID = item.ID
                    count = item.count
                else:
                    ID = item
                if ID in self.items: count = count + self.items[ID]
                self.items[ID] = count

            for item in items:
                if isinstance(item, list):
                    for i in item: self.add(i)
                elif isinstance(item, tuple):
                    for i in item: self.add(i)
                elif isinstance(item, dict):
                    for ID, count in item.iteritems(): additem(ID, count)
                else:
                    additem(item)

    #---------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Actions: These convert items to other items
#
#-------------------------------------------------------------------------------

actions = []

class Action(object):

    def __init__(self, consumes, produces):
        self.consumes = Item.Bag(consumes)
        self.produces = Item.Bag(produces)
        actions.append(self)

    def __repr__(self): return "%s -> %s" % (str(self.consumes), str(self.produces))

#-------------------------------------------------------------------------------

Action("Time", "Gather")
Action("Gather", "Berries")
Action("Gather", "Vegetables")

#-------------------------------------------------------------------------------
#
# Actor
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
#
#
#-------------------------------------------------------------------------------

#print Item("Eggs")
#print Item("Eggs") * 5
#print Item("Eggs") * 5 + "Bacon"
#print "Eggs" + Item("Bacon")
#print { "Bacon": 1, "Butter": 1 } + 5 * Item("Eggs")

for action in actions: print action
