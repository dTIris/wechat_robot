

class Informer(object):
    def __init__(self):
        self.sm = {} #维护状态机
        self.history_op = {}
        self.history_output = {}
		#{page_id:{proc，sm_id, father_page_id，child_page_list:[,...]},}  sm_id=0-->公用
		#{sm_id:[op,...]
		#{sm_id:[{page_id},...]
    def add_sm(self, sm_id):
        pass
	def register_page(self, page_id, father_page_id, proc):
		#在sm_id=0的sm里添加
		pass
	def register_private_page(self, sm_id, page_id, father_page_id, proc):
		pass
	def operator(self, sm_id, op):
		last_page_id = self.history_output[sm_id][0]
		curre_page_list = self.sm[last_page_id]["child_page_list"]
		for iter in curre_page_list:
			if op == iter["proc"].get_name()
			if op == iter["proc"].get_index()
			if not:
				return "无效操作"
			return iter["proc"]handler()
		pass

class proc:
	def get_sub_menu()
	def handler()
# 构建公用界面
register_page(0, -1, classA)
register_page(1, 0, classA)
register_page(2, 0, classA)
register_page(3, 0, classA)
register_page(4, 1, classA)
register_page(5, 1, classA)
register_page(60, 2, classA)
# 
operator(user_id, "菜单")
