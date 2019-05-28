# def func(data):

#     for k,v in data.items():
#         print(k,v)

#     if isinstance(v,dict):
#         func(v)

#     return



# data = {
#     'zack':{
#         'Chinese':{'teacher':'zhang'},
#     }
# }
# func(data)


in_data = {
    "frank": {
        "Math": {"teacher": "zhang", "score": "75"},
        "English": {"teacher": "xu", "score": "65"},
        "height": "162"
 
    }
}
 
 
def format_dict(var, str_key):
    if type(var) == type({}):
        for key in var:
            tmp_key = str_key + "_" + key
            format_dict(var[key], tmp_key)
    else:
        print(str_key[2:] + ":" + var)
        return 0
 
format_dict(in_data, " ")