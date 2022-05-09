
                            # Example of arges

# def him(ban):
#     for item in ban:
#         print(item)
# ban=["himanshu","bansal","manoj",56,78,65,5,4,4]
# him(ban)


                           # Example of kwargs

def dhee(**manoj):
    for key, value in manoj.items():
        print(f"{key} is a {value}")
manoj = {"raju":"chor","mohan":"admin"}
dhee(**manoj)