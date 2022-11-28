def searchProduct(arr,value):
    for i in arr:
        if (i["id"] == value):
            return i;
    return ("error");

def searchPostalCode(arr,value):
    for x in arr : 
        if ( x["postal_code"] == value):
            return x["distance_in_kilometers"];        
    return ("error");

def getAllProducts(arr):
    if (arr):
        return arr;
    return ("error")

def getAllCategories(arr):
    if (arr):
        return arr;
    return ("error")

def getCategoryProducts(arr,value):
    result = []
    for i in arr:
        if (i["category"] == value):
            result.append( i);
    if (len(result)>0):
        return result;
    return ("error"); 

def authUser(username,password):
    if (username == "admin") and (password == "admin"):
        return "Success";
    else:
        return "Not Allowed"
    return ("error")
