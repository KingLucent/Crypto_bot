import pickle
import os

approved_users_path=os.path.abspath(__file__).replace('.py','_data')

def load_users():
	try:
		loaded_approved_users=pickle.load(open(approved_users_path,"rb"))
	except:
		loaded_approved_users=['your user id here']
		pickle.dump(loaded_approved_users,open(approved_users_path,"wb"))
	return loaded_approved_users

def add_user(user_id):
	approved_users=load_users()
	approved_users.append(int(user_id))
	pickle.dump(approved_users,open(approved_users_path,"wb"))

def remove_user(user_id_remove):
	approved_users=load_users()
	index_user=approved_users.index(user_id_remove)
	approved_users.pop(index_user)
	pickle.dump(approved_users,open(approved_users_path,"wb"))