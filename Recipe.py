
pasta = ("Pasta Arraabiata" , "Italian" , 20 , "Medium")

biryani = ("Chicken Biryani" , "Indian" , 45 , "Easy")



print("Recipei 1" , pasta)

print("Nmae:" , pasta[0])

print("Cusine:" , pasta[1])

print("Difficylty:" , pasta[-1])



all_recipes = (pasta , biryani)

print("First recipe name:" , all_recipes[0][0])

print("Second recipe name" , all_recipes[1][2] , "mins")

print("Pasta details (sliced):" , pasta[1:3])




print("Pasta Recipe Details")

for details in pasta:
    print("" , details)



pasta_ingreddients = {"tomato" , "garlic" , "olive oil" , "chilli" , "pasta" , "garlic"}

biryani_ingredients = {"rice" , "chicken" , "garlic" , "onion" , "spices" , "curd"}


print("Pasta Ingredients:" , pasta_ingreddients)

print("Biryani Ingredients" , biryani_ingredients)

print("Total pasta ingredients", pasta_ingreddients)




all_ingredients = pasta_ingreddients.union(biryani_ingredients)

common = pasta_ingreddients.intersection(biryani_ingredients)

only_pasta = pasta_ingreddients.difference(biryani_ingredients)

unique_to_each = pasta_ingreddients.symmetric_difference(biryani_ingredients)





print("All ingredients union" , all_ingredients)

print("Common ingredients (intersectipn)" , common)

print("only in pasta (difference):" , only_pasta)

print("NOT shared (sym.diifference):" , unique_to_each)












