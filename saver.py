import pickle


'''
- Tested the Save function and working fine 
- Couldn't test the restore function as it need the model to be implemented from scartch and not keras model
'''
class Saver:
    @staticmethod
    def save(model, path):
        vars = {name: p["vars"] for name, p in model.params.items()}
        with open(path, "wb") as f:
            pickle.dump(vars, f)

    @staticmethod
    def restore(model, path):
        with open(path, "rb") as f:
            params = pickle.load(f)
        for name, param in params.items():
            for p_name in model.params[name]["vars"].keys():
                model.params[name]["vars"][p_name][:] = param[p_name]
                model.params[name]["vars"][p_name][:] = param[p_name]