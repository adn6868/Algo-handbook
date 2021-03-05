import re

class BST():
	def __init__(self, data=None):
		self.data  = data
		self.left  = None
		self.right = None

	def add(self, new_data):
		if self.data == None:
			self.data = new_data
			return 

		new_node = BST(new_data)
		self._add(new_node)

	def _add(self, new_node):
		if new_node.data >= self.data:
			if self.left == None:
				self.left = new_node
			else:
				self.left._add(new_node)
		else:
			if self.right == None:
				self.right = new_node
			else:
				self.right._add(new_node)
	def __str__(self):
		if self.left == self.right == None:
			return str([self.data])#+'['+'None'+','+'None'+']'
		elif self.right == None:
			return str(self.data)+'['+'None'+','+str(self.left)+']'
		elif self.left == None:
			return str(self.data)+'['+str(self.right)+','+'None'+']'
		else:
			return str(self.data)+'['+str(self.right)+','+str(self.left)+']'


def constructFromString(data):
	data_list = re.split(',|\[|\]',data)
	data_list = [v for v in data_list if v != '']
	data_list = [v for v in data_list if v != 'None']
	new_bst = BST()
	for d in data_list:
		new_bst.add(int(d))
	return new_bst



def main():
	bst = BST(3)
	bst.add(2)
	bst.add(1)
	bst.add(4)
	print(bst)
	bst_2 = constructFromString(str(bst))
	print(bst_2)



if __name__ == '__main__':
	main()
