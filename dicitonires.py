# dictionaries is mutable(can change)
data={
    "name":"ALi Hassnain",
    "age": 19,
    "Phone NUmber": "0302-3329571",
    "siblings":4,
    "siblingdata":["umair",19,"Sameer",22,"Zeeshan",26],
    "siblingPhone":("Available","Available","Not Available")
}
# print(data)
# print(data["siblingdata"])
# data["siblingdata"]="None"     #mutable
# print(data)
# print(data["age"])
# nested dictanories
info={
    "name": "Gudu",
    "subject" :{
        "phy" : 'F',
         "chem" : 'A',
         "Math" : 'f'
    }
}
print(info)
# print(info["subject"]["Math"])
                      

                                      # dictanories method

# print(info.keys())
# print(info.values())
print(list(info.items())) #give values inthe form of pairs
print(info.get("name2"))  #.get method is liye use krty hain k agr ham variable mean k ("name") ki jga ("name2") likh deun to ye error ki bjaye none value de ga or error k baad wali lines b execute hoge 
info.update({"follower" : "None"})
print(info)