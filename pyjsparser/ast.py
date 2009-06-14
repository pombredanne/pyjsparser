


class Node(object):
    def __init__(self):
        self._fields = []
        self._repr_args = []
        
    def __repr__(self):
        args_string = ", ".join(("%s=%r" % (arg, getattr(self, arg, None)))
            for arg in self._repr_args)
        return "<ast.%s(%s)>" % (self.__class__.__name__, args_string)
            
    def __iter__(self):
        for field in self._fields:
            yield field

class BlockComment(Node):
    def __init__(self, data):
        Node.__init__(self)
        self.data = data
        self._repr_args = ['data']
        

class LineComment(Node):
    def __init__(self, data):
        Node.__init__(self)
        self.data = data
        self._repr_args = ['data']

class String(Node):
    def __init__(self, data):
        Node.__init__(self)
        self.data = data
        self._repr_args = ['data']
        
class Program(Node):
    def __init__(self, statements):
        Node.__init__(self)
        self.statements = statements or []
        self._fields = [self.statements]
    
        
class Assign(Node):
    def __init__(self, node, operator, expression):
        Node.__init__(self)
        self.node = node
        self.operator = operator
        self.expr = expression
        self._fields = [expression]
        self._repr_args = ['node', 'operator']
        
class VariableDeclaration(Node):
    def __init__(self, node, expression):
        Node.__init__(self)
        self.node = node
        self.expr = expression
        self._fields = [expression]
        self._repr_args = ['node']
        


class Or(Node):
    def __init__(self, left, right):
        Node.__init__(self)
        self.left = left
        self.right = right
        self._fields = [left, right]
    
class And(Node):
    def __init__(self, left, right):
        Node.__init__(self)
        self.left = left
        self.right = right
        self._fields = [left, right]
        
class Number(Node):
    def __init__(self, value):
        Node.__init__(self)
        self.value = value
        self._fields = [value]
        
class Object(Node):
    def __init__(self, properties):
        Node.__init__(self)
        self.properties = properties
        self._fields = [properties]
    
class UnaryOp(Node):
    def __init__(self, operator, value, postfix):
        Node.__init__(self)
        self.operator = operator
        self.value = value
        self.postfix = postfix
        self._repr_args = ['value', 'operator', 'postfix']

class Boolean(Node):
    def __init__(self, value):
        Node.__init__(self)
        self.value = value
        self._repr_args = ['value']
    
class If(Node):
    def __init__(self, expression, true, false):
        Node.__init__(self)
        self.expr = expression
        self.true = true
        self.false = false
        self._fields = [true, false]
        
class Identifier(Node):
    def __init__(self, name):
        Node.__init__(self)
        self.name = name
        self._repr_args = ['name']
    
class BinOp(Node):
    def __init__(self, operator, left, right):
        Node.__init__(self)
        self.operator = operator
        self.left = left
        self.right = right
        self._fields = [left, right]
        self._repr_args = ['operator']


class With(Node):
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement
        self._fields = [expression, statement]

        
class LabelledStatement(Node):
    def __init__(self, identifier, statement):
        Node.__init__(self)
        self.identifier = identifier
        self.statement = statement
        self._fields = [statement]
        self._repr_args = ['indentifier']


class Throw(Node):
    def __init__(self, expression):
        Node.__init__(self)
        self.expression = expression
        self._fields = [expression]
        
class ElementGet(Node):
    def __init__(self, node, element):
        Node.__init__(self)
        self.node = node
        self.element = element
        self._repr_args = ['node', 'element']

class Try(Node):
    def __init__(self, statements, catch, finally_):
        Node.__init__(self)
        self.statements = statements
        self.catch = catch
        self.finally_ = finally_
        self._fields = [statements, catch, finally_]

class Catch(Node):
    def __init__(self, identifier, statements):
        Node.__init__(self)
        self.identifier = identifier
        self.statements = statements
        self._fields = [statements]
        self._repr_args = ['identifier']

class Finally(Node):
    def __init__(self, statements):
        Node.__init__(self)
        self.statements = statements
        self._fields = [statements]

        
class Return(Node):
    def __init__(self, expression):
        Node.__init__(self)
        self.expression = expression
        self._fields = [expression]
        
class FuncDecl(Node):
    def __init__(self, name, parameters, statements):
        Node.__init__(self)
        self.parameters = parameters
        self.statements = statements
        self._fields = [statements]
        self._repr_args = ['name', 'parameters']

class Switch(Node):
    def __init__(self, expression, cases, default=None):
        Node.__init__(self)
        self.expression = expression
        self.cases = cases or []
        self.default = default
        self._fields = [self.cases, self.default]
        self._repr_args = ['expression']

class Case(Node):
    def __init__(self, identifier, statements):
        Node.__init__(self)
        self.identifier = identifier
        self.statements = statements
        self._fields = [statements]
        self._repr_args = ['identifier']
        print statements

class For(Node):
    def __init__(self, initialisers, conditions, increments, statement):
        Node.__init__(self)
        self.initialisers = initialisers
        self.conditions = conditions
        self.increments = increments
        self.statement = statement
        
        self._fields = [statement]
        self._repr_args = ['initialisers', 'conditions', 'increments']

class ForIn(Node):
    def __init__(self, item, iterator, statement):
        Node.__init__(self)
        self.item = item
        self.iterator = iterator
        self.statement = statement
        self._fields = [statement]
        self._repr_fields = ['item', 'iterator']
        
class DoWhile(Node):
    def __init__(self, condition, statement):
        Node.__init__(self)
        self.condition = condition
        self.statement = statement
        self._fields = [statement]
        self._repr_args = ['condition']
        
class While(Node):
    def __init__(self, condition, statement):
        Node.__init__(self)
        self.condition = condition
        self.statement = statement
        self._fields = [statement]
        self._repr_args = ['condition']
    
        
class DefaultCase(Case):
    pass

class FuncCall(Node):
    def __init__(self, node, arguments):
        Node.__init__(self)
        self.node = node
        self.arguments = arguments
        self._repr_args = ['node', 'arguments']
    
class New(Node):
    def __init__(self, identifier, arguments=None):
        Node.__init__(self)
        self.identifier = identifier
        self.arguments = arguments or []
        self._repr_args = ['identifier', 'arguments']

class Continue(Node):
    def __init__(self, identifier):
        Node.__init__(self)
        self.identifier = identifier
        self._repr_args = ['name']
        
    
class Break(Node):
    def __init__(self, identifier):
        Node.__init__(self)
        self.identifier = identifier
        self._repr_args = ['name']
        